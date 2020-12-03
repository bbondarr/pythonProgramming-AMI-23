import json

from flask import Flask, request, jsonify
from flask_login import login_required, current_user

from app import app, db, ma
from models.OrderModel import Order
from models.ProductModel import Product
from schemas.OrderSchema import OrderSchema
from routes.RouteManager import RouteManager
from Validation import Validation as v


orderSchema = OrderSchema()
ordersSchema = OrderSchema(many=True)

orderRouteManager = RouteManager(Order, orderSchema, ordersSchema)

# SQLALCHEMY DOESN'T ALLOW ME TO MAKE A DECORATOR ON A ROUTE ==============
# SO THAT'S WHY THIS IF ROLE == ADMIN IS EVERYWHERE =======================

@app.route('/api/orders', methods=['POST'])
@login_required
def makeOrder():
    try:
        order = Order(**
            {a:request.json[a] for a in Order.attributes() 
            if a != 'id'and a != 'date' and a != 'userID'}
        )
        order.setUserID(current_user.id)
        product = Product.query.filter(Product.id == order.productID).first()
        product.setQuantity(product.quantity - order.amount)
        
        db.session.add(order)
        db.session.commit()

        return jsonify({'status': 'success'}, 
                       {'message': (f'Thanks for making an order, {order.user.firstName}!'+
                                    'You can see it in your GET menu now')}), 201
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/api/orders', methods=['GET'])
@login_required
def getAllOrders():
    try:
        sortBy = request.args.get('sort', default=None, type=str)
        filterBy = request.args.get('filter', default=None, type=str)
        limit = request.args.get('limit', default=None, type=int)
        page = request.args.get('page', default=None, type=int)

        orderQuery = Order.query.filter(Order.userID == current_user.id)
        orders = orderRouteManager.getAll(sortBy, filterBy, limit, page, orderQuery)
        return jsonify({'status': 'success'},
                        {'count': len(orders)}, 
                        {'orders': orders}), 200
    except Exception as e:
        return jsonify({'status': 'fail'}, {'message': str(e)}), 404


@app.route('/api/orders/<id>', methods=['GET'])
@login_required
def getOrder(id):
        try:
            orderQuery = Order.query.filter(Order.userID == current_user.id)
            result = orderRouteManager.getSingle(id)
            return jsonify({'status': 'success'}, 
                        {'product': result}), 200
        except Exception as e:
            return jsonify({'status': 'fail'}, {'message': str(e)}), 404
