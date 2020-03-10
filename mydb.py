import mysql.connector
from datetime import date
from data_classes import Ospite, Prenotazione
from mysql.connector import errorcode


class Connector:
    def __init__(self, host='localhost',
                 user='root',
                 passwd='bavR@0',
                 database=None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.my_connector = None
        self.cursor = None
        self.get_connect()

    def create_db(self, db_name):
        return self.exec_(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    def create_table(self,
                     name: str = None,
                     fields: dict = None, options = ''):
        """
        :param name: str
        :param fields: dict --> field_name: (field_kind, length) es: 'surname': (VARCHAR, 10)
        :return:
        """

        self.exec_(f"USE {self.database}")
        command = f"CREATE TABLE IF NOT EXISTS {name} "
        field_names = '('
        for col, type_num in fields.items():
            if type(type_num[1]) is int:
                field_names += f' {col} {type_num[0]}({type_num[1]}),'
            elif type_num[1] is None:
                field_names += f' {col} {type_num[0]},'
            else:
                field_names += f' {col} {type_num[0]} {type_num[1]},'
            if len(type_num) > 2:
                field_names = field_names[:-1] + ' '
                for option in type_num[2:]:
                    field_names += f'{option}'
                field_names += ','
        field_names = field_names[:-1] + f'{options})'
        command += field_names
        print(command)
        self.exec_(command)
        print(f'Table {name} has been created')
        return command

    def exec_(self,command=None):
        if not self.cursor:
            return False
        try:
            self.cursor.execute(command)
            return True
        except mysql.connector.errors.ProgrammingError as e:
            print('execute Exception\n', e)
            raise

    def fetch(self,_all=True, print_out=True):
        if _all:
            results = self.cursor.fetchall()
        else:
            results = self.cursor.fetchone()
        if print_out:
            for row in results:
                print(row)
        return results

    def get_connect(self):
        try:
            self.my_connector = mysql.connector.connect(host=self.host,
                                                        user=self.user,
                                                        passwd=self.passwd
                                                        )
            self.get_cursor()
            return self.create_db(self.database)
        except mysql.connector.errors.ProgrammingError as e:
            print('Exception:\n', e)
            raise

    def get_cursor(self):
        if self.my_connector:
            self.cursor = self.my_connector.cursor()

    def insert(self, row_list_dict, table):
        """
        :param row_list_dict: list of dataClasses
        :param table:
        :return:
        """
        values = []
        _fields = []
        for field_dict in row_list_dict:
            _fields = [field for field in field_dict]
            values.append(tuple([str(value) for value in field_dict.values()]))
        print(type(values[0]))
        if not _fields or not values:
            return False
        command = f"INSERT INTO {table} "
        command += '(' + ', '.join(_fields) + ') VALUES (%s, %s, %s, %s, %s)'
        try:
            if len(values) > 1:
                # print(command.format(values))
                self.cursor.executemany(command, values)
            else:
                # print(command.format(values[0]))
                self.cursor.execute(command, values[0])
        except mysql.connector.errors.ProgrammingError as e:
            print('Exception:\n', e)
            raise

    def list_databases(self):
        self.exec_("SHOW DATABASES")
        if self.cursor:
            print('databases:')
            for db in self.cursor:
                print(db)
        else:
            print('something went wrong')

    def query(self, fields, table):
        self.exec_(f"SELECT {fields} FROM {table}")

    def select_db(self, db=None):
        if db is None:
            db = self.database
        self.exec_(f"USE {db}")

    def show_tables(self):
        self.exec_("SHOW TABLES")
        for table in self.cursor:
            print(table)


if __name__ == '__main__':
    mydb = Connector(database='test_db')
    mydb.list_databases()
    my_fields = Ospite.ospiti_table_fields
    ins = 'studenti (nome, age) VALUES (%s, %s)',('Lucio', '37')
    command_create_table = mydb.create_table('ospiti', my_fields)

    mydb.insert(my_fields, 'ospiti')
    mydb.my_connector.commit()
    # mydb.cursor.execute(f"USE {mydb.database}")
    # mydb.cursor.execute("DROP TABLE ospiti")