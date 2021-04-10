from fixture.application import Application
from fixture.db import DbFixture
import pytest
import os.path
import jsonpickle
import ftputil

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = jsonpickle.decode(f.read())
    return target


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, config["web"]["baseUrl"])
    fixture.session.ensure_login(username=config["webadmin"]["username"], password=config["webadmin"]["password"])
    return fixture


@pytest.fixture
def db(request):
    db_config = load_config(request.config.getoption("--config"))["db"]
    db_fixture = DbFixture(host=db_config["host"], db_name=db_config["name"], user=db_config["user"],
                           password=db_config["password"])

    def fin():
        db_fixture.destroy()

    request.addfinalizer(fin)
    return db_fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):

    def fin():
        if fixture is not None:
            fixture.session.ensure_logout()
            fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--config"))


"""
@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_config(config["ftp"]["host"], config["ftp"]["username"], config["ftp"]["password"])

    def fin():
        restore_server_config(config["ftp"]["host"], config["ftp"]["username"], config["ftp"]["password"])

    request.addfinalizer(fin)


def install_server_config(host, username, password):
"""



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")
