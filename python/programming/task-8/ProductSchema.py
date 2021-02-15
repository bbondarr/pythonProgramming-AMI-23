from app import ma

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('_Product__iD', 
                  '_Product__title', 
                  '_Product__imageURL', 
                  '_Product__price', 
                  '_Product__createdAt', 
                  '_Product__updatedAt', 
                  '_Product__description')