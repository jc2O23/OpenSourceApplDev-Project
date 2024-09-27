# John Campbell
# CSC 341
# Project

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///JC_Project.db?check_same_thread=False')
Base = declarative_base()


item_sides_table = Table('item_sides_table', Base.metadata,
    Column('item_id', Integer, ForeignKey('item.item_id')),
    Column('side_id', Integer, ForeignKey('side.side_id'))
)

class Menus(Base):
   __tablename__ = 'menu'
   
   menu_id = Column(Integer, primary_key=True, autoincrement=True)
   menu_name = Column(String)
   menu_start = Column(String)
   menu_end = Column(String)
   menu_days = Column(String)
   menu_item = relationship("Items")


class Items(Base):
   __tablename__ = 'item'
   
   item_id = Column(Integer, primary_key=True, autoincrement=True)
   item_name = Column(String)
   item_price = Column(Integer)
   item_course = Column(String)   
   item_stock = Column(Integer)
   menu_id = Column(Integer, ForeignKey('menu.menu_id'))
   has_sides = relationship("Sides", secondary=item_sides_table, viewonly=True)



class Sides(Base):
   __tablename__ = 'side'
   
   side_id = Column(Integer, primary_key=True, autoincrement=True)
   side_name = Column(String)
   side_price = Column(Integer)
   side_stock = Column(Integer)
   on_item = relationship("Items", secondary=item_sides_table, viewonly=True)


class Order(Base):
   __tablename__ = 'order'
   order_id = Column(Integer, primary_key=True, autoincrement=True)
   order_tally = Column(Integer)
   item_id = Column(Integer, ForeignKey('item.item_id'))
   order_item = relationship("Items")


Base.metadata.create_all(engine)