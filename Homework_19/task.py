import sqlite3

file = input("Введите название файла: ")
connection = sqlite3.connect(file)
cursor = connection.cursor()

result = cursor.execute("""
SELECT title FROM films
WHERE genre = (SELECT id FROM genres WHERE title = "детектив") AND year BETWEEN 1995 AND 2000
""").fetchall()
result = list(map(lambda x: str(x)[1:(len(str(x)) - 2):], result))

print("\n".join(result))