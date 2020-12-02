from sqlalchemy import desc, cast

from app import db
from models.ProductModel import Product

def sort(query, sortBy):
    if sortBy:
        if sortBy in Product.attributes(): 
            query = query.order_by(sortBy)
            
        if (sortBy[0] == '-' and 
            sortBy[1:] in Product.attributes()):
            query = query.order_by(desc(sortBy[1:]))

    return query


def filter(query, filterBy):
    if filterBy:
        query = query.filter(
                    Product.title.like('%'+filterBy+'%') |
                    Product.imageURL.like('%'+filterBy+'%') |
                    Product.description.like('%'+filterBy+'%') |
                    cast(Product.id, db.String).like('%'+filterBy+'%') |
                    cast(Product.price, db.String).like('%'+filterBy+'%') |
                    cast(Product.createdAt, db.String).like('%'+filterBy+'%') |
                    cast(Product.updatedAt, db.String).like('%'+filterBy+'%'))
    return query


def paginate(query, page, per_page):
    return query.paginate(page, per_page).items