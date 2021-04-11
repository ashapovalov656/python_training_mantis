from model.project import Project
import re


def clear(s):
    return re.sub("[() -]", "", s).\
        replace(".", "").\
        replace("/", "")


def create_project_if_empty(app):
    if len(app.soap.get_projects(app.config["webadmin"]["username"], app.config["webadmin"]["password"])) == 0:
        app.project.create(Project(name="123", desc="456"))
