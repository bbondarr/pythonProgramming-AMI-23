from app import ma


class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 
                  'product.title', 
                  'product.price', 
                  'amount', 
                  'date')