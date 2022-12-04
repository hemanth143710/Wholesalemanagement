from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Date,DateTime


students=Table(
    'students',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('age',String(255)),
    Column('country',String(255)),
)

orders=Table(
    'orders',meta,
    Column('Customer_id',Integer,primary_key=True),
    Column('Orderdate',String(255)),
    Column('RequiredDate', String(255)),
    Column('ShippedDate', String(255)),
    Column('ShipName',String(255)),
    Column('ShipAddress',String(255)),
    Column('ShipCity', String(255)),
    Column('ShipCountry', String(255)),
    Column('Shippostalcode', String(255)),
    Column('AmountPaid', String(255)),

)

stock=Table(
    'stock',meta,
    Column('Stock_id',Integer,primary_key=True),
    Column('Stock_name',String(255)),
    Column('Stock_quantity', Integer),

)

buyers=Table(
    'buyers',meta,
    Column('Buyer_id',Integer,primary_key=True),
    Column('Stock_id',Integer),
    Column('City',String(255)),
    Column('Street',String(255)),
    Column('State',String(255)),
    Column('Pincode',String(255)),
)


customer=Table(
    'customer',meta,
    Column('Customer_id',Integer,primary_key=True),
    Column('Customer_name',String(255)),
    Column(' Phone_number',String(45)),
    Column('Address',String(255)),
    Column('Pincode',String(255)),
)





# Stock_id int(09) NOT NULL PRIMARY KEY,
#     Stock_name varchar(50) NOT NULL,
#     Stock_quantity int(20) NOT NULL
#     );

# Order_id int(11) NOT NULL PRIMARY KEY,
#     Customer_id int(11) NOT NULL,
#     Orderdate DATE,
#     RequiredDate DATE,
#     ShippedDate DATE,
#     ShipName varchar(255),
#     ShipAddress varchar(255),
#     ShipCity varchar(255),
#     ShipCountry varchar(255),
#     Shippostalcode varchar(6),
#     AmountPaid varchar(1) DEFAULT 'N'
