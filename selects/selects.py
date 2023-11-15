from prettytable import PrettyTable
from sqlalchemy import func, desc, and_

from conf.db import session
from conf.models import Teacher, Student, Subject, Grade, Group


def select_1():
    sel = (session.query(Student.id, Student.fullname.label('Student'),
                         func.round(func.avg(Grade.grade), 2).label('Average_grade')).select_from(Student).join(Grade)
           .group_by(Student.id).order_by(desc('Average_grade')).limit(5).all())
    return sel


def select_2():
    sel = (session.query(Student.id, Student.fullname.label('Student'), func.round(func.avg(Grade.grade), 2)
                         .label('Average_grade')).select_from(Grade).join(Student).join(Subject)
           .where(Grade.subject_id == 1).group_by(Student.id).order_by(desc('Average_grade')).limit(1).all())
    return sel


def select_3():
    sel = (session.query(Group.id, Group.name.label('Group'),
                         func.round(func.avg(Grade.grade), 2).label('Average_grade'))
           .select_from(Student).join(Group).join(Grade).where(Grade.subject_id == 1).group_by(Group.id)
           .order_by(desc('Average_grade')).limit(1).all())
    return sel


def select_4():
    sel = session.query(func.round(func.avg(Grade.grade), 2).label('Average_grade')).select_from(Grade).all()
    return sel


def select_5():
    sel = (session.query(Teacher.fullname.label('Teacher'), Subject.name.label('Subject'))
           .select_from(Teacher).join(Subject).all())
    return sel


def select_6():
    sel = session.query(Student.fullname.label('Student')).select_from(Student).where(Student.group_id == 1).all()
    return sel


def select_7():
    sel = (session.query(Student.fullname.label('Student'), Grade.grade.label('Grade')).select_from(Student).join(Grade)
           .where(and_(Student.group_id == 1, Grade.subject_id == 1)).all())
    return sel


def select_8():
    sel = (session.query(Teacher.fullname.label('Teacher'), Subject.name.label('Subject'),
                         func.round(func.avg(Grade.grade), 2).label('Average_grade'))
           .select_from(Teacher).join(Subject).join(Grade).group_by(Teacher.fullname, Subject.name).all())
    return sel


def select_9():
    sel = (session.query(Subject.name.label('Subject')).select_from(Student).join(Grade).join(Subject)
           .where(Grade.student_id == 1).group_by(Subject.id).all())
    return sel


def select_10():
    sel = (session.query(Subject.name.label('Subject')).select_from(Subject).join(Grade)
           .where(and_(Subject.teacher_id == 1, Grade.student_id == 1)).group_by(Subject.name).all())
    return sel


def select_11():
    sel = (session.query(Teacher.fullname.label('Teacher'), Student.fullname.label('Student'),
                         func.round(func.avg(Grade.grade), 2).label('Average_grade')).select_from(Teacher).join(Subject)
           .join(Grade).join(Student).where(and_(Grade.student_id == 1, Teacher.id == 1))
           .group_by(Teacher.id, Student.id).all())
    return sel


def select_12():
    sel = (session.query(Grade.grade_date.label('Date'), Group.name.label('Group'), Student.fullname.label('Student'),
                         Grade.grade.label('Grade')).select_from(Grade).join(Student).join(Group)
           .where(and_(Group.id == 1, Grade.subject_id == 1)).order_by(desc(Grade.grade_date)).all())
    return sel



if __name__ == '__main__':
    for i in range(1, 13):
        table = PrettyTable(title=f'Вибірка №{i}', align='l')
        # exec(f'result = select_{i}()')
        result = eval(f'select_{i}()')
        try:
            table.field_names = result[0]._fields
            table.add_rows(result)
            print(table)
        except TypeError:
            pass
