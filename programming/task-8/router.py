import json

from flask import Flask, request, jsonify

from app import app, db, ma
from ProductModel import Product
from ProductSchema import ProductSchema

productSchema = ProductSchema()
productsSchema = ProductSchema(many=True)

@app.route('/product', methods=['GET'])
def getAll():
    try:
        products = Product.query.all()
        result = productsSchema.dump(products)

        return jsonify({'status': 'success'}, 
                        {'products': result}), 200
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/product', methods=['POST'])
def post():
    try:
        id = request.json['id']
        title = request.json['title']
        imageURL = request.json['imageURL']
        price = request.json['price']
        createdAt = request.json['createdAt']
        updatedAt = request.json['updatedAt']
        description = request.json['description']

        newProduct = Product(title, imageURL, price, createdAt, updatedAt, description, id)
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
        product = Product.query.filter(Product._Product__iD == id).first()
        
        result = productSchema.dump(product)
        return jsonify({'status': 'success'}, 
                        {'product': result}), 200
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/product/<id>', methods=['DELETE'])
def delete(id):
    try:
        product = Product.query.filter(Product._Product__iD == id).first()

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
        product = Product.query.filter(Product._Product__iD == id).first()
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