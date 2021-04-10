import pymysql.cursors
from model.project import Project


class DbFixture:

    def __init__(self, host, db_name, user, password):
        self.host = host
        self.name = db_name
        self.uer = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=db_name, user=user, password=password, autocommit=True)

    def get_project_list(self):
        project_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, description from mantis_project_table")
            for row in cursor:
                (id, name, description) = row
                project_list.append(Project(id=str(id), name=name, desc=description))
        finally:
            cursor.close()
        return project_list

    def destroy(self):
        self.connection.close()