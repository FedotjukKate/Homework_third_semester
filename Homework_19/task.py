import sqlite3

connection = sqlite3.connect("films_1.sqlite")
cursor = connection.cursor()

result = cursor.execute("""
SELECT title FROM films
WHERE genre = (SELECT id FROM genres WHERE title = "детектив") AND year BETWEEN 1995 AND 2000
""").fetchall()
result = list(map(lambda x: str(x)[1:(len(str(x)) - 2):], result))

print("\n".join(result))