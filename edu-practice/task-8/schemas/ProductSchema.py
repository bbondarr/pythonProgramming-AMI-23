from app import ma

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('iD', 
                  'title', 
                  'imageURL', 
                  'price', 
                  'createdAt', 
                  'updatedAt', 
                  'description')