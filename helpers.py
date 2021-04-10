from model.project import Project
import re


def clear(s):
    return re.sub("[() -]", "", s).\
        replace(".", "").\
        replace("/", "")


def create_project_if_empty(app, orm):
    if len(orm.get_project_list()) == 0:
        app.project.create(Project(name="123", desc="456"))