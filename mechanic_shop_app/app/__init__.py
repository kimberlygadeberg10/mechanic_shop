from flask import Flask
from extensions import db
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Phoenix0350*@127.0.0.1:3306/mechanic_shop_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    from models import Customer, Vehicle, ServiceTicket, Mechanic, ServiceMechanic
    
    with app.app_context():
        db.create_all()
        
    register_routes(app)
        
    return app