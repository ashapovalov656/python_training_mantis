from pony.orm import *
from model.project import Project


class ORMFixture:

    db = Database()

    class ORMProject(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column="mantis_project_table")
        name = Optional(str, column="name")
        description = Optional(str, column="description")

    def __init__(self, host, db_name, user, password):
        self.db.bind('mysqli', host=host, database=db_name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_projects_to_model(self, projects):
        def convert(project):
            return Project(id=str(project.id), name=project.name, desc=project.desc)
        return list(map(convert, projects))

    @db_session
    def get_group_list(self):
        return self.convert_projects_to_model(select(p for p in ORMFixture.ORMProject))
