# John Campbell
# CSC 341
# Project

import JC_Project_DB as my_db

from sqlalchemy.orm import sessionmaker

from JC_Project_FORM import Insert_Menu_Form, Insert_Item_Form, View_Sides_Form
from flask import Flask, render_template, url_for, request, redirect

Session = sessionmaker(bind=my_db.engine)
session = Session()


app = Flask(__name__)

app.config["SECRET_KEY"] = "Its a secret?"

menuList = session.query(my_db.Menus).all()
menuOpts = []

for menu in menuList:
    mylist = []
    mylist.append(str(menu.menu_id))
    mylist.append("{}: {}".format(menu.menu_id, menu.menu_name))
    my_tuple = tuple(mylist)
    menuOpts.append(my_tuple)

itemList = session.query(my_db.Items).all()
itemOpts = []

for item in itemList:
    mylist = []
    mylist.append(str(item.item_id))
    mylist.append("{}: {}".format(item.item_id, item.item_name))
    my_tuple = tuple(mylist)
    itemOpts.append(my_tuple)


@app.route("/")
def myredirect():
    return redirect(url_for("JC_ProjectTable"))


@app.route("/JC_ProjectTable")
def JC_ProjectTable():
    query = session.query(my_db.Menus)
    results = query.all()

    menu_dict = [u.__dict__ for u in results]

    query = session.query(my_db.Items)
    results = query.all()

    item_dict = [u.__dict__ for u in results]

    query = session.query(my_db.Sides)
    results = query.all()

    side_dict = [u.__dict__ for u in results]

    menu_columns = list(menu_dict[0].keys())
    menu_columns.remove("_sa_instance_state")
    menu_data = []
    for record in menu_dict:
        rowList = list(record.values())
        rowList.pop(0)
        menu_data.append(rowList)

    item_columns = list(item_dict[0].keys())
    item_columns.remove("_sa_instance_state")
    item_data = []
    for record in item_dict:
        rowList = list(record.values())
        rowList.pop(0)
        item_data.append(rowList)

    side_columns = list(side_dict[0].keys())
    side_columns.remove("_sa_instance_state")
    side_data = []
    for record in side_dict:
        rowList = list(record.values())
        rowList.pop(0)
        side_data.append(rowList)

    return render_template(
        "JC_ProjectTable.html",
        title="John Campbell Project",
        header="John Campbell Project",
        menu_data=menu_data,
        menu_columns=menu_columns,
        item_data=item_data,
        item_columns=item_columns,
        side_data=side_data,
        side_columns=side_columns,
    )


@app.route("/JC_ProjectTable2")
def JC_ProjectTable2():
    query = session.query(my_db.Items)
    results = query.all()
    result_dict = [u.__dict__ for u in results]
    return render_template(
        "JC_ProjectTable2.html",
        title="John Campbell Project",
        header="John Campbell Project",
        items=result_dict,
    )


@app.route("/JC_ProjectInsertMenu", methods=["GET", "POST"])
def JC_ProjectInsertMenu():
    form = Insert_Menu_Form()

    if form.validate_on_submit():
        result = request.form
        new_menu = my_db.Menus(
            menu_name=result["menu_name"],
            menu_start=result["menu_start"],
            menu_end=result["menu_end"],
            menu_days=result["menu_days"],
        )
        session.add(new_menu)
        session.commit()

        query = session.query(my_db.Menus)
        results = query.all()

        menu_dict = [u.__dict__ for u in results]

        query = session.query(my_db.Items)
        results = query.all()

        item_dict = [u.__dict__ for u in results]

        query = session.query(my_db.Sides)
        results = query.all()

        side_dict = [u.__dict__ for u in results]

        menu_columns = list(menu_dict[0].keys())
        menu_columns.remove("_sa_instance_state")
        menu_data = []
        for record in menu_dict:
            rowList = list(record.values())
            rowList.pop(0)
            menu_data.append(rowList)

        item_columns = list(item_dict[0].keys())
        item_columns.remove("_sa_instance_state")
        item_data = []
        for record in item_dict:
            rowList = list(record.values())
            rowList.pop(0)
            item_data.append(rowList)

        side_columns = list(side_dict[0].keys())
        side_columns.remove("_sa_instance_state")
        side_data = []
        for record in side_dict:
            rowList = list(record.values())
            rowList.pop(0)
            side_data.append(rowList)

        return render_template(
            "JC_ProjectTable.html",
            title="John Campbell Project",
            header="John Campbell Project",
            menu_data=menu_data,
            menu_columns=menu_columns,
            item_data=item_data,
            item_columns=item_columns,
            side_data=side_data,
            side_columns=side_columns,
        )

    return render_template(
        "JC_ProjectInsertMenu.html",
        title="John Campbell Project",
        header="John Campbell Project",
        form=form,
    )


@app.route("/JC_ProjectInsertItem", methods=["GET", "POST"])
def JC_ProjectInsertItem():
    form = Insert_Item_Form()
    form.menu_id.choices = menuOpts
    if form.validate_on_submit():
        result = request.form

        new_item = my_db.Items(
            item_name=result["item_name"],
            item_price=result["item_price"],
            item_course=result["item_course"],
            item_stock=result["item_stock"],
        )
        new_item.menu_id = result["menu_id"]
        session.add(new_item)
        session.commit()

        query = session.query(my_db.Menus)
        results = query.all()

        menu_dict = [u.__dict__ for u in results]

        query = session.query(my_db.Items)
        results = query.all()

        item_dict = [u.__dict__ for u in results]

        query = session.query(my_db.Sides)
        results = query.all()

        side_dict = [u.__dict__ for u in results]

        menu_columns = list(menu_dict[0].keys())
        menu_columns.remove("_sa_instance_state")
        menu_data = []
        for record in menu_dict:
            rowList = list(record.values())
            rowList.pop(0)
            menu_data.append(rowList)

        item_columns = list(item_dict[0].keys())
        item_columns.remove("_sa_instance_state")
        item_data = []
        for record in item_dict:
            rowList = list(record.values())
            rowList.pop(0)
            item_data.append(rowList)

        side_columns = list(side_dict[0].keys())
        side_columns.remove("_sa_instance_state")
        side_data = []
        for record in side_dict:
            rowList = list(record.values())
            rowList.pop(0)
            side_data.append(rowList)

        return render_template(
            "JC_ProjectTable.html",
            title="John Campbell Project",
            header="John Campbell Project",
            menu_data=menu_data,
            menu_columns=menu_columns,
            item_data=item_data,
            item_columns=item_columns,
            side_data=side_data,
            side_columns=side_columns,
        )

    return render_template(
        "JC_ProjectInsertItem.html",
        title="John Campbell Project",
        header="John Campbell Project",
        form=form,
    )


@app.route("/JC_ProjectItemSides", methods=["GET", "POST"])
def JC_ProjectItemSides():
    item = ""
    form = View_Sides_Form()
    form.item_opts.choices = itemOpts
    if form.validate_on_submit():
        item_list = []
        result = request.form
        item_sides = (
            session.query(my_db.Items)
            .filter(my_db.Items.item_id == result["item_opts"])
            .first()
        )
        print("{} has the sides: ".format(item_sides.item_name))
        for item in item_sides.has_sides:
            item_list.append(item.side_name)

        return render_template(
            "JC_ProjectItemSides.html",
            title="John Campbell Project",
            header="John Campbell Project",
            item_list=item_list,
            item=item_sides.item_name,
            form=form,
        )

    return render_template(
        "JC_ProjectItemSides.html",
        title="John Campbell Project",
        header="John Campbell Project",
        form=form,
        item=item,
    )


if __name__ == "__main__":
    app.run(debug=True)
