import json

from flask import Flask, request, jsonify
from sqlalchemy import desc

from app import app, db, ma
from ProductModel import Product
from ProductSchema import ProductSchema
from Validation import Validation as v


productSchema = ProductSchema()
productsSchema = ProductSchema(many=True)

@app.route('/product', methods=['GET'])
def getAll():
    try:
        sortBy = request.args.get('sort', default=None, type=str)
        _filter = request.args.get('filter', default=None, type=str)

        productQuery = Product.query

        if sortBy in Product.getAttributes(): 
            if sortBy.startswith('-'):
                productQuery = productQuery.order_by(desc(sortBy[1:]))
            else:
                productQuery = productQuery.order_by(sortBy)

        # if _filter:
        #     query = Product.query.filter(
        #                 Product._Product__iD.like('%'+_filter+'%'))

        #     for attr in Product.getAttributes():
        #         subquery = productQuery.filter(
        #                 getattr(Product, '_Product__'+attr).like('%'+_filter+'%'))
        #         print(subquery)
        #         query.union(subquery)

            productQuery = query
                
        

        products = productQuery.all()
        result = productsSchema.dump(products)
        return jsonify({'status': 'success'}, 
                        {'products': result}), 200
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/product', methods=['POST'])
def post():
    try:
        newProduct = Product(**
            {a:request.json[a] for a in Product.getAttributes() if a != 'iD'}
        )
        db.session.add(newProduct)
        db.session.commit()

        result = productSchema.dump(newProduct)
        return jsonify({'status': 'success'}, 
                        {'new product': result}), 201
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/product/<id>', methods=['GET'])
def get(id):
    try:
        v.validateID(id)
        product = Product.query.filter(Product._Product__iD == id).first()
        v.validateNotNoneProduct(product)

        result = productSchema.dump(product)
        return jsonify({'status': 'success'}, 
                        {'product': result}), 200
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/product/<id>', methods=['DELETE'])
def delete(id):
    try:
        v.validateID(id)
        product = Product.query.filter(Product._Product__iD == id).first()
        v.validateNotNoneProduct(product)

        db.session.delete(product)
        db.session.commit()

        result = productSchema.dump(product)
        return jsonify({'status': 'success'}, 
                        {'deleted product': result}), 204
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/product/<id>', methods=['PATCH'])
def patch(id):
    try:
        v.validateID(id)
        product = Product.query.filter(Product._Product__iD == id).first()
        v.validateNotNoneProduct(product)

        field = None
        attr = None

        for attr in Product.getAttributes():
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