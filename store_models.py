from models import db 

item_order_table = db.Table('item_order_table',
                            db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
                            db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
                            )

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(250))
    price = db.Column(db.Float)
    creator = db.Column(db.String(300))

    def __str__(self):
        return self.name


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    phone = db.Column(db.String(30))
    email = db.Column(db.String(250))
    price = db.Column(db.Float)
    items = db.relationship("Item",
                            secondary=item_order_table)



        


