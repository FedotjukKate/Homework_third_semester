import sqlite3

file = input("Введите название файла: ")
connection = sqlite3.connect(file)
cursor = connection.cursor()

result = cursor.execute("""
SELECT title FROM genres
WHERE id in (SELECT DISTINCT genre FROM films
WHERE year BETWEEN 2010 AND 2011)
""").fetchall()
result = list(map(lambda x: str(x)[1:(len(str(x)) - 2):], result))

print("\n".join(result))