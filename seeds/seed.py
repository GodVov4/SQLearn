from faker import Faker
from random import randint, choice
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher, Student, Subject, Grade, Group


fake = Faker('uk_UA')


NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_TEACHERS = randint(3, 5)


def insert_groups():
    for _ in range(NUMBER_GROUPS):
        group = Group(name=fake.word())
        session.add(group)


def insert_teachers():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(fullname=fake.name())
        session.add(teacher)


def insert_subjects():
    for teacher_id in range(1, NUMBER_TEACHERS+1):
        for _ in range(NUMBER_SUBJECTS//NUMBER_TEACHERS):
            subject = Subject(name=fake.word(), teacher_id=teacher_id)
            session.add(subject)


def insert_students():
    for group_id in range(1, NUMBER_GROUPS+1):
        for _ in range(NUMBER_STUDENTS//NUMBER_GROUPS):
            student = Student(fullname=fake.name(), group_id=group_id)
            session.add(student)


def insert_relation():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()

    for student in students:
        NUMBER_GRADES = randint(1, 20)
        for _ in range(NUMBER_GRADES):
            relation = Grade(grade=randint(0, 100), grade_date=fake.date_this_decade(),
                             student_id=student.id, subject_id=choice(subjects).id)
            session.add(relation)


def main():
    try:
        insert_groups()
        insert_teachers()
        insert_subjects()
        insert_students()
        session.commit()
        insert_relation()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()


if __name__ == '__main__':
    main()
