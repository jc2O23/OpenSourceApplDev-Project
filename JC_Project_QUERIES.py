# John Campbell
# CSC 341
# Project


import JC_Project_DB as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()

query = session.query(my_db.Menus)
results = query.all()

for item in results:
   print ("ID/Menu = {}: {} | Days = {} START: {} END: {}".format(item.menu_id, item.menu_name, item.menu_days, item.menu_start, item.menu_end)) 

print("*"*60)

results = session.query(my_db.Items, my_db.Menus.menu_name).join(my_db.Menus).all()

for item, menu_name in results:
    print("ID/Item = {}: {} | Price = ${} Stock = {} Menu = {}".format(
        item.item_id, item.item_name, item.item_price, item.item_stock, menu_name))

print("*"*60)

results = session.query(my_db.Sides).all()

for item in results:
   print ("ID/Side = {}: {} | Price = ${} Stock: {}".format(item.side_id, item.side_name, item.side_price, item.side_stock)) 

print("*"*60)
item_sides = session.query(my_db.Items).filter(my_db.Items.item_id == 3).first()
print("{} has the sides: ".format(item_sides.item_name))
for item in item_sides.has_sides:
   print("- " + item.side_name)

print("*"*60)
item_sides = session.query(my_db.Items).filter(my_db.Items.item_id == 11).first()
print("{} has the sides: ".format(item_sides.item_name))
for item in item_sides.has_sides:
   print("- " + item.side_name)

print("*"*60)
item_sides = session.query(my_db.Sides).filter(my_db.Sides.side_id == 11).first()
print("{} goes with: ".format(item_sides.side_name))
for item in item_sides.on_item:
   print("- " + item.item_name)

print("*"*60)
item_sides = session.query(my_db.Sides).filter(my_db.Sides.side_id == 1).first()
print("{} goes with: ".format(item_sides.side_name))
for item in item_sides.on_item:
   print("- " + item.item_name)