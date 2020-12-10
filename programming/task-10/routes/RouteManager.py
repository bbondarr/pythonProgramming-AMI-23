from flask import request

from apiFeatures import sort, filter, paginate
from Validation import Validation as v


class RouteManager:
    def __init__(self, model, schema, schemaMany):
        self.model = model
        self.schema = schema
        self.schemaMany = schemaMany

        
    def getAll(self, sortBy, filterBy, limit, page, query=None):
        if not query:
            query = self.model.query
        # Handling sort query
        query = sort(query, sortBy)

        # Handling filter/find query
        query = filter(query, filterBy)

        # Handling pagination
        units = paginate(query, page, limit)

        result = self.schemaMany.dump(units)
        return result


    @v.validateID
    def getSingle(self, id):
        unit = self.model.query.filter(self.model.id == id).first()
        v.validateNotNoneObject(unit)

        result = self.schema.dump(unit)
        return result


    @v.validateID
    def deleteSingle(self, id):
        unit = self.model.query.filter(self.model.id == id).first()
        v.validateNotNoneObject(unit)
        return unit


    @v.validateID
    def patchSingle(self, id):
        unit = self.model.query.filter(self.model.id == id).first()
        v.validateNotNoneObject(unit)

        field = None
        attr = None

        for attr in self.model.attributes():
            try:
                field = request.json[attr]
                break
            except KeyError: pass

        getattr(unit, 'set'+attr[0].upper()+attr[1:])(field)

        result = self.schema.dump(unit)
        return result