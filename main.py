from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, Namespace
from prettytable import PrettyTable

from conf.db import session
from conf.models import Teacher, Student, Subject, Grade, Group


def get_table(sel):
    table = PrettyTable()
    result = [dict(list(vars(record).items())[-1:0:-1]) for record in sel]
    table.field_names = result[0].keys()
    table.add_rows([value.values() for value in result])
    return table


def create_record(args: Namespace) -> str:
    record = eval(args.model)(name=args.name)
    session.add(record)
    session.commit()
    return f'Record {args.name} created'


def list_record(args: Namespace) -> str:
    sel = session.query(eval(args.model)).all()
    table = get_table(sel)
    return f'All records in {args.model}:\n{table}'


def update_record(args: Namespace) -> str:
    sel = session.get(eval(args.model), args.id)
    sel.name = args.name
    session.add(sel)
    session.commit()
    return f'Record {args.id} updated to {args.name}'


def remove_record(args: Namespace) -> str:
    sel = session.get(eval(args.model), args.id)
    session.delete(sel)
    session.commit()
    return f'Record {args.name} deleted'


def main():
    parser = ArgumentParser('DB Reader', description='Simple access to database with CLI-interface',
                            epilog='Let\'s try it', formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-a', '--action', choices=['create', 'list', 'update', 'remove'], default='list',
                        help='Choose an action for the database', type=str)
    parser.add_argument('-m', '--model', choices=['Grades', 'Group', 'Student', 'Subject', 'Teacher'],
                        help='Choose a model from the database', type=str, required=True)
    parser.add_argument('-i', '--id', help='Choose id', type=int)
    parser.add_argument('-n', '--name', help='Choose a name', type=str)

    args = parser.parse_args()

    call_dict = {
        'create': create_record,
        'list': list_record,
        'update': update_record,
        'remove': remove_record,
    }

    print(call_dict.get(args.action)(args))
    session.close()


if __name__ == '__main__':
    main()
