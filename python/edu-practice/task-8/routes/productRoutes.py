import json

from flask import Flask, request, jsonify
from flask_login import login_required, current_user

from app import app, db, ma
from models.ProductModel import Product
from schemas.ProductSchema import ProductSchema
from Validation import Validation as v
from apiFeatures import sort, filter, paginate

productSchema = ProductSchema()
productsSchema = ProductSchema(many=True)


# =================================PRODUCT ROUTES===========================================
@app.route('/api/products', methods=['GET'])
@login_required
def getAll():
    try:
        sortBy = request.args.get('sort', default=None, type=str)
        filterBy = request.args.get('filter', default=None, type=str)
        limit = request.args.get('limit', default=None, type=int)
        page = request.args.get('page', default=None, type=int)

        productQuery = Product.query.filter(Product.userID == current_user.id)

        # Handling sort query
        productQuery = sort(productQuery, sortBy)

        # Handling filter/find query
        productQuery = filter(productQuery, filterBy)

        # Handling pagination
        products = paginate(productQuery, page, limit)

        result = productsSchema.dump(products)
        return jsonify({'status': 'success'},
                       {'count': len(products)}, 
                       {'products': result}), 200
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/api/products', methods=['POST'])
@login_required
def post():
    try:
        newProduct = Product(**
            {a:request.json[a] for a in Product.attributes() 
                if a != 'iD' and a != 'user' and a != 'userID'}
        )
        newProduct.userID = current_user.id
        db.session.add(newProduct)
        db.session.commit()

        result = productSchema.dump(newProduct)
        return jsonify({'status': 'success'}, 
                       {'new product': result}), 201
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/api/products/<id>', methods=['GET'])
@login_required
def get(id):
    try:
        v.validateID(id)
        product = Product.query.filter(Product.userID == current_user.id).filter(Product.iD == id).first()
        v.validateNotNoneProduct(product)

        result = productSchema.dump(product)
        return jsonify({'status': 'success'}, 
                       {'product': result}), 200
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/api/products/<id>', methods=['DELETE'])
@login_required
def delete(id):
    try:
        v.validateID(id)
        product = Product.query.filter(Product.userID == current_user.id).filter(Product.iD == id).first()
        v.validateNotNoneProduct(product)

        db.session.delete(product)
        db.session.commit()

        result = productSchema.dump(product)
        return jsonify({'status': 'success'}, 
                       {'deleted product': result}), 204
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/api/products/<id>', methods=['PATCH'])
@login_required
def patch(id):
    try:
        v.validateID(id)
        product = Product.query.filter(Product.userID == current_user.id).filter(Product.iD == id).first()
        v.validateNotNoneProduct(product)

        field = None
        attr = None

        for attr in Product.attributes():
            try:
                field = request.json[attr]
                break
            except KeyError: pass

        getattr(product, 'set'+attr[0].upper()+attr[1:])(field)

        result = productSchema.dump(product)
        db.session.commit()
        return jsonify({'status': 'success'}, 
                       {'patched product': result}), 204
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404