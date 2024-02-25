import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("oil.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table OIL(NAME VARCHAR(25),TYPE VARCHAR(25),
PRICE VARCHAR(25),STOCK INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into OIL values('Fortune','Sunflower','1010',90)''')
cursor.execute('''Insert Into OIL values('Sunpure','Sunflower','1000',100)''')
cursor.execute('''Insert Into OIL values('Ruchi Gold','Palm','800',86)''')
cursor.execute('''Insert Into OIL values('Freedom','Sunflower','1030',50)''')
cursor.execute('''Insert Into OIL values('Gemini','Sunflower','1050',35)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from OIL''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
