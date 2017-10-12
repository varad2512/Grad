import mysql.connector
cnx = mysql.connector.connect(user='inf551', password='inf551',
 host='127.0.0.1',
 database='inf551')
cursor = cnx.cursor()
query = "select name from Beers"
cursor.execute(query)
print cursor
for name in cursor:
 print name
cursor.close()
cnx.close()