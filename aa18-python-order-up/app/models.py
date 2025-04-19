from flask_login import UserMixin  # New import
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

# table = db.Table(
#     "employee",
#     db.metadata,
#     db.Column("id", db.Integer, primary_key=True),
#     db.Column("name", db.String(100), nullable=False),
#     db.Column("employee_number", db.Integer, nullable=False),
#     db.Column("hashed_password", db.String(255), nullable=False),
# )


class Employee(db.Model, UserMixin):  # Your class definition
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, employee_number, password):
        self.name = name
        self.employee_number = employee_number
        self.hashed_password = generate_password_hash(password)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, name):
        self.name = name


class MenuItem(db.Model):
    __tablename__ = "menu_item"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    menu_id = db.mapped_column(db.Integer, db.ForeignKey("menu.id"), nullable=False)
    type_id = db.mapped_column(
        db.Integer, db.ForeignKey("menu_item_type.id"), nullable=False
    )

    menu = db.relationship("Menu")
    type = db.relationship("MenuItemType")

    def __init__(self, name, price, type, menu):
        self.name = name
        self.price = price
        self.menu = menu
        self.type = type  # ????


class MenuItemType(db.Model):
    __tablename__ = "menu_item_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name
