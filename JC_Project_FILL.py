# John Campbell
# CSC 341
# Project

import JC_Project_DB as my_db
from sqlalchemy.orm import sessionmaker
import os
import json
import csv

Session = sessionmaker(bind=my_db.engine)
session = Session()

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('static/data/JC_ProjectDATA.json') as r:
   json_data = json.load(r)

for i, menu in enumerate(json_data["menus"]):
   new_menu = my_db.Menus(menu_name=menu["menu_name"], menu_start=menu["menu_start"], 
   menu_end=menu["menu_end"], menu_days=menu["menu_days"]) 
   session.add(new_menu)
   session.flush() 

   for item in json_data["menus"][i]["menu_items"]:
      new_item = my_db.Items(item_name=item["item_name"], item_price=item["item_price"], 
                          item_course=item["item_course"], item_stock = item["item_stock"])
      new_item.menu_id = new_menu.menu_id
      session.add(new_item)

session.commit()

with open("static/data/JC_ProjectDATA.csv", 'r') as csvfile:
   r = csv.DictReader(csvfile)
    
   for row in r:
      new_side = my_db.Sides(
         side_name=row['side_name'],
         side_price=int(row['side_price']),
         side_stock=int(row['side_stock']))
      
      session.add(new_side)

session.commit()

session.execute(my_db.item_sides_table.insert().values([(1, 5), (3, 5), (4, 5),
                                                        (1, 6), (3, 6), (4, 6),
                                                        (1, 16), (3, 16), (4, 16),
                                                        (1, 17), (3, 17), (4, 17),
                                                        (1, 18), (3, 18), (4, 18),
                                                        (1, 24), (3, 24), (4, 24)]))
session.commit()

session.execute(my_db.item_sides_table.insert().values([(11, 1), (10, 1), (12, 1),
                                                        (11, 2), (10, 2), (12, 2),
                                                        (11, 3), (10, 3), (12, 3),
                                                        (11, 10), (10, 10), (12, 10),
                                                        (11, 9), (10, 9), (12, 9),
                                                        (11, 23), (10, 23), (12, 23),
                                                        (11, 5), (10, 8), (12, 11),
                                                        (11, 7), (10, 22), (12, 19)]))

session.commit()
