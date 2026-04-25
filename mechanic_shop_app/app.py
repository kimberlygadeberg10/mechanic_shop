from flask import Flask, jsonify, request
from extensions import db
from marshmallow import ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Phoenix0350*@127.0.0.1:3306/mechanic_shop_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

from models import Customer, Vehicle, ServiceTicket, Mechanic, ServiceMechanic
from schemas import CustomerSchema

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


@app.post("/customers")
def create_customer():
    customer_data = customer_schema.load(request.get_json())
    new_customer = Customer(**customer_data)
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.dump(new_customer), 201


@app.get("/customers")
def get_customers():
    customers = Customer.query.all()
    return customers_schema.dump(customers), 200


@app.get("/customers/<int:customer_id>")
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return customer_schema.dump(customer), 200


@app.put("/customers/<int:customer_id>")
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    customer_data = customer_schema.load(request.get_json(), partial=True)

    for field, value in customer_data.items():
        setattr(customer, field, value)

    db.session.commit()
    return customer_schema.dump(customer), 200


@app.delete("/customers/<int:customer_id>")
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": f"Customer {customer_id} deleted successfully."}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
