import sqlite3 as sql

with sql.connect("students.db") as con:
    cur = con.cursor()

    # cur.execute(
    #     """DROP TABLE IF EXISTS students"""
    # )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        subject TEXT,
        score INTEGER
        )"""
    )
    # cur.execute(
    #     """INSERT INTO students (name, age, subject, score) VALUES ('James', 19, 'English', 19)"""
    # )

    # students = cur.execute("""
    # SELECT name, age, subject, score FROM students
    # """)

    # students = cur.execute("""
    #    SELECT name, age FROM students
    #    """)

    # students = cur.execute("""
    #    SELECT * FROM students
    #    """)
    # print(students.fetchall())
    # print(students.fetchone())
    # print(students.fetchmany(2))

    # date = cur.execute("""
    # SELECT * FROM students WHERE name = 8
    # """)

    # date = cur.execute("""
    #     SELECT * FROM students WHERE rowid = 'James'
    #     """)

    # date = cur.execute("""
    #          SELECT * FROM students WHERE subject ='English'
    #          """)

    # date = cur.execute("""
    #             SELECT * FROM students WHERE score < 19 AND age == 13
    #             """)

    # date = cur.execute("""
    #                 SELECT * FROM students WHERE score < 19 OR age == 13
    #                 """)
    #
    # print(date.fetchall())

    # cur.execute("""
    # UPDATE students SET age = 11, score = 2 WHERE name='James'
    # """)

    # cur.execute("""
    # DELETE FROM students WHERE score=5
    # """)

    data = cur.execute("""
    SELECT * FROM students ORDER BY name JASC 
    """)
    print(data.fetchall())
