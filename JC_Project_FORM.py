# John Campbell
# CSC 341
# Project

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, DecimalField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange

class Insert_Menu_Form(FlaskForm):
 
   menu_name = StringField(u"Menu Name", 
                  validators=[InputRequired(message="You must enter a Menu Name"), 
                              Length(min=4, message="You must enter a menu name at least 5 characters long!")])

   menu_start = StringField(u"Menu Start Time (EX: 10AM)", 
                  validators=[InputRequired(message="You must enter a Start Time"), 
                              Length(min=3, max=4, message="You must enter a start time in the format 3PM, 12AM, etc!!")])

   menu_end = StringField(u"Menu End Time (EX: 11PM)", 
                  validators=[InputRequired(message="You must enter a End Time"), 
                              Length(min=3, max=4, message="You must enter a end time in the format 3PM, 12AM, etc!")])
   
   menu_days = StringField(u"Menu Days (EX: Weekdays)", 
                  validators=[InputRequired(message="You must enter days for the menu"), 
                              Length(min=5, message="You must enter greater than 5 characters for menu days!")])
     
   submit = SubmitField("Insert Menu")

class Insert_Item_Form(FlaskForm):
 
   item_name = StringField(u"Item Name", 
                  validators=[InputRequired(message="You must enter an item name"), 
                              Length(min=5, message="You must enter greater than 5 characters long for item name!")])

   item_price = IntegerField(u"Item Price", 
                  validators=[InputRequired(message="You must enter price for the item"), 
                              NumberRange(min=0, max=99, message="You must enter price from 0 to 99!")])
   
   item_course = StringField(u"Item Course (EX: Entree, Appitizer)", 
               validators=[InputRequired(message="You must enter days for the menu"), 
                              Length(min=5, message="You must enter greater than 5 characters for item course!")])
   
   item_stock = IntegerField(u"Item Stock", 
            validators=[InputRequired(message="You must enter days for the menu"), 
                              NumberRange(min=0, max=100, message="You must enter price from 0 to 100!")])
   
   menu_id = SelectField(u"Menu ID", 
            validators=[InputRequired(message="You must select a menu")])

   submit = SubmitField("Insert Item")


class View_Sides_Form(FlaskForm):
   
   item_opts = SelectField(u"Item Select", 
            validators=[InputRequired(message="You must select an item")])

   submit = SubmitField("See Sides")