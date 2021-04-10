from model.project import Project
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return (prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])).strip()


testdata = [Project(name=random_string("Project", 10), desc=random_string("Desc", 20)) for i in range(3)]


@pytest.mark.parametrize("test_project", testdata)
def test_create_project(app, orm, test_project):
    old_projects = orm.get_project_list()
    project_names = [p.name for p in old_projects]

    while test_project.name in project_names:
        test_project.name = random_string("Project", 10)

    app.project.create(test_project)
    old_projects.append(test_project)
    new_projects = orm.get_project_list()

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
