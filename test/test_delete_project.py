from helpers import create_project_if_empty
import random


def test_delete_project_by_id(app, db):
    create_project_if_empty(app, db)
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    assert len(old_projects) - 1 == len(db.get_project_list())
    new_projects = db.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects
