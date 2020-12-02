from app import ma

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 
                  'title', 
                  'imageURL', 
                  'price', 
                  'quantity',
                  'createdAt', 
                  'updatedAt', 
                  'description')