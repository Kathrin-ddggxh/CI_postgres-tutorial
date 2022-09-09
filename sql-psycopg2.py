import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database:
# anything queried from the db will become part of the curser object
# then iterate over object
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# IMPORTANT: Only use single quotes to wrap query, and double quotes to
# specify values from within db
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from "Artist" table
# %s is Python string placeholder,
# desired string is then defined in list as 2nd argument
# cursor.execute(
#     'SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by ArtistId #51 from Artist table
cursor.execute(
    'SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51]
)

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is
# "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
