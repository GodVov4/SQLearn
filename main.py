import sqlite3

from faker import Faker
from random import randint


fake = Faker('uk_UA')


NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_TEACHERS = randint(3, 5)
NUMBER_GRADES = randint(1, 20)


with sqlite3.connect('university.db') as conn:
    cur = conn.cursor()

    # groups
    for _ in range(NUMBER_GROUPS):
        cur.execute('INSERT INTO groups (name) VALUES (?)', (fake.word(),))

    # teachers
    for _ in range(NUMBER_TEACHERS):
        cur.execute('INSERT INTO teachers (fullname) VALUES (?)', (fake.name(),))

    # subjects
    for teacher_id in range(1, NUMBER_TEACHERS+1):
        for _ in range(NUMBER_SUBJECTS//NUMBER_TEACHERS):
            cur.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (fake.word(), teacher_id))

    # students and grades
    for group_id in range(1, NUMBER_GROUPS+1):
        for _ in range(NUMBER_STUDENTS//NUMBER_GROUPS):
            cur.execute(
                'INSERT INTO students (fullname, group_id) VALUES (?, ?) RETURNING id', (fake.name(), group_id)
            )

            student_id = cur.fetchone()[0]
            for subject_id in range(1, (NUMBER_SUBJECTS//NUMBER_TEACHERS*NUMBER_TEACHERS)+1):
                for _ in range(3):
                    cur.execute(
                        "INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)",
                        (student_id, subject_id, randint(0, 100), fake.date_this_decade())
                    )

    conn.commit()
