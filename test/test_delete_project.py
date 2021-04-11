from helpers import create_project_if_empty
import random


def test_delete_project_by_id(app):
    create_project_if_empty(app)
    old_projects = app.soap.get_projects(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)

    assert len(old_projects) - 1 == len(app.soap.get_projects(app.config["webadmin"]["username"],
                                                              app.config["webadmin"]["password"]))

    new_projects = app.soap.get_projects(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    old_projects.remove(project)

    assert old_projects == new_projects
