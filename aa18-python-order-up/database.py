from dotenv import load_dotenv

load_dotenv()

from app import app, db
from app.models import Employee, MenuItemType, MenuItem, Menu


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()

    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    db.session.add(beverages)
    db.session.commit()
    db.session.add(entrees)
    db.session.commit()
    db.session.add(sides)
    db.session.commit()
    db.session.add(dinner)
    db.session.commit()
    db.session.add(fries)
    db.session.commit()
    db.session.add(drp)
    db.session.commit()
    db.session.add(jambalaya)
    db.session.commit()
