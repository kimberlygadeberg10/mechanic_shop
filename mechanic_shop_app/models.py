from app import db

class Customer(db.Model):
    __tablename__ = "customers"
    
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    
class Vehicle(db.Model):
    __tablename__ = "vehicles"
    
    vehicle_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"), nullable=False)
    vin = db.Column(db.String(17), unique=True, nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    license_plate = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(30))
    
class ServiceTicket(db.Model):
    __tablename__ ="service_tickets"
    
    ticket_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.vehicle_id"), nullable=False)
    date_opened = db.Column(db.Date, nullable=False)
    date_closed = db.Column(db.Date)
    service_description = db.Column(db.String(255), nullable=False)
    problem_reported = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    total_cost = db.Column(db.Numeric(10, 2), nullable=False)