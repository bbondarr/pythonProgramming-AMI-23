import json

from flask import Flask, request, jsonify
from flask_login import login_required, current_user

from app import app, db, ma
from models.ProductModel import Product
from schemas.ProductSchema import ProductSchema
from routes.RouteManager import RouteManager
from Validation import Validation as v

productSchema = ProductSchema()
productsSchema = ProductSchema(many=True)

productRouteManager = RouteManager(Product, productSchema, productsSchema)


# SQLALCHEMY DOESN'T ALLOW ME TO MAKE A DECORATOR ON A ROUTE ==============
# SO THAT'S WHY THIS IF ROLE == ADMIN IS EVERYWHERE =======================

@app.route('/api/products', methods=['GET'])
@login_required
def getAllProducts():
    try:
        sortBy = request.args.get('sort', default=None, type=str)
        filterBy = request.args.get('filter', default=None, type=str)
        limit = request.args.get('limit', default=None, type=int)
        page = request.args.get('page', default=None, type=int)

        products = productRouteManager.getAll(sortBy, filterBy, limit, page)
        return jsonify({'status': 'success'},
                        {'count': len(products)}, 
                        {'products': products}), 200
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/api/products', methods=['POST'])
@login_required
def postProduct():
    if current_user.role == 'admin':
        try:
            newProduct = Product(**
                {a:request.json[a] for a in Product.attributes() 
                    if a != 'id' and a != 'user' and a != 'userID'}
            )
            newProduct.userID = current_user.id
            db.session.add(newProduct)
            db.session.commit()

            result = productSchema.dump(newProduct)
            return jsonify({'status': 'success'}, 
                        {'new product': result}), 201
        except Exception as e:
            return jsonify({'status': 'fail'}, {'message': str(e)}), 404
    else:
         return jsonify({'status': 'fail'}, {'message': 'access denied'}), 404


@app.route('/api/products/<id>', methods=['GET'])
@login_required
def getProduct(id):
    try:
        result = productRouteManager.getSingle(id)
        return jsonify({'status': 'success'}, 
                       {'product': result}), 200
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/api/products/<id>', methods=['DELETE'])
@login_required
def deleteProduct(id):
    if current_user.role == 'admin':
        try:
            product = productRouteManager.deleteSingle(id)
            db.session.delete(product)
            db.session.commit()
            return jsonify({'status': 'success'}), 204
        except Exception as e:
            return jsonify({'status': 'fail'}, {'message': str(e)}), 404
    else:
         return jsonify({'status': 'fail'}, {'message': 'access denied'}), 404



@app.route('/api/products/<id>', methods=['PATCH'])
@login_required
def patchProduct(id):
    if current_user.role == 'admin':
        try:
            result = productRouteManager.patchSingle(id)
            db.session.commit()
            return jsonify({'status': 'success'}), 204
        except Exception as e:
            return jsonify({'status': 'fail'}, {'message': str(e)}), 404
    else:
         return jsonify({'status': 'fail'}, {'message': 'access denied'}), 404