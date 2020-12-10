from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 
                  'firstName', 
                  'lastName', 
                  'email', 
                  'role')