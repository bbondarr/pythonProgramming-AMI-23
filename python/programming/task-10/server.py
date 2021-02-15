from app import app
from routes.productRoutes import *
from routes.userRoutes import *
from routes.orderRoutes import *


if __name__ == '__main__':
    app.run(debug=True)