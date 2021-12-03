import sqlite3

genre_name = input("Введите название жанра: ")
connection = sqlite3.connect("music_db.sqlite")
cursor = connection.cursor()

result = cursor.execute(f"""
SELECT Title FROM Album
WHERE AlbumId IN (SELECT DISTINCT AlbumId FROM Track
WHERE GenreId = (SELECT GenreId FROM Genre
WHERE name = "{genre_name}"))
""").fetchall()
result = list(map(lambda x: str(x)[1:(len(str(x)) - 2):], result))
artists = cursor.execute(f"""
SELECT ArtistId FROM Album
WHERE AlbumId IN (SELECT DISTINCT AlbumId FROM Track
WHERE GenreId = (SELECT GenreId FROM Genre
WHERE name = "{genre_name}"))
""").fetchall()
artists = list(map(lambda x: int(str(x)[1:(len(str(x)) - 2):]), artists))
merged_list = sorted([(artists[i], result[i]) for i in range(0, len(artists))], key=lambda x: (x[0], x[1].lower()))
for i in merged_list:
    print(i[1])