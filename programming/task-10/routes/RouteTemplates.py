from flask import request

from apiFeatures import sort, filter, paginate
from Validation import Validation as v

class RouteTemplate:
    @staticmethod
    def getAll(query, schema, sortBy, filterBy, limit, page):
        # Handling sort query
        query = sort(query, sortBy)

        # Handling filter/find query
        query = filter(query, filterBy)

        # Handling pagination
        units = paginate(query, page, limit)

        result = schema.dump(units)
        return result


    @staticmethod
    def getSingle(id, model, schema):
        v.validateID(id)
        unit = model.query.filter(model.id == id).first()
        v.validateNotNoneObject(unit)

        result = schema.dump(unit)
        return result


    @staticmethod
    def deleteSingle(id, model, schema):
        v.validateID(id)
        unit = model.query.filter(model.id == id).first()
        v.validateNotNoneObject(unit)
        return unit


    @staticmethod
    def patchSingle(id, model, schema):
        v.validateID(id)
        unit = model.query.filter(model.id == id).first()
        v.validateNotNoneObject(unit)

        field = None
        attr = None

        for attr in model.attributes():
            try:
                field = request.json[attr]
                break
            except KeyError: pass

        getattr(unit, 'set'+attr[0].upper()+attr[1:])(field)

        result = schema.dump(unit)
        return result