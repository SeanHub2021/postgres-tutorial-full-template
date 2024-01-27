#import a few classes from the sqlalchemy module
from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# link Python file to Chinook database 
db = create_engine("postgresql:///chinook") #3 slashes indicates it is hosted locally

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "artist", meta, 
    Column("artist_id", Integer, primary_key=True),
    Column("name", String)
)

# create variable for "Album" table
album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id"))
)

# create a variable for "Track" table
track_table = Table(
    "track", meta,
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("media_type_id", Integer, primary_key=False),
    Column("genre_id", Integer, primary_key=False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float)
)

# making the connect
with db.connect() as connection:

    #Query 1 - select all records from the "artist" table
    #select_query = artist_table.select()

    #Query 2 - select only the "name" column from the "artist" table
    #select_query = artist_table.select().with_only_columns([artist_table.c.name])

    #Query 3 - select only 'Queen' from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.name == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)