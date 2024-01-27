import psycopg2


# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
# this is similar to a set or list, similar to an array in JS
cursor = connection.cursor()

# fetch the results (multiple), creates a variable named 'results' to retrieve data from the array/cursor
# this will handle any result that gets queried
results = cursor.fetchall()

# fetch the result (single). If we are intentionally looking for one single record.
#results = cursor.fetchone()

#close the connection, so it doesnt persist.
connection.close()

# print results. Iterate over the results. 
for result in results:
    print(result)
