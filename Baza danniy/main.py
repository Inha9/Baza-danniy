import sqlite3 as sql

con = sql.connect("first.db")
cur = con.cursor()


# cur.execute(
#     """CREATE TABLE users(
#        name TEXT,
#        age INTEGER,
#        coin INTEGER
#     )"""
# )

# /cur.execute(
#     """
#     INSERT INTO users (name, age, coin) VALUES ('James', 19, 250)
#     """
# )
# con.commit()
#
# con.close()

while True:
   name = input("name:")
   age = input("age:")
   coin = input("coin:")
   if "stop" in name or "stop" in age or "stop" in coin:
      break
cur.execute(
        f"""
        INSERT INTO users(name, age, coin) VALUES("{name}", {age}, {coin})
        """
   )
con.commit()
con.close()