import mysql.connector
import sys
cnx = mysql.connector.connect(user='inf551', password='inf551',
                              host='127.0.0.1',
                              database='sakila')
cursor = cnx.cursor()
sys.argv[1] = sys.argv[1].strip().lower()
query = "select count(film_id) from film_category f INNER JOIN category c on c.category_id = f.category_id where c.name ='"+sys.argv[1]+"'"
cursor.execute(query)
for name in cursor:
    print name[0]
cursor.close()
cnx.close()
