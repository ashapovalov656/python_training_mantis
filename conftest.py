from fixture.application import Application
import pytest
import os.path
import jsonpickle

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
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--config"))["web"]
    webadmin = load_config(request.config.getoption("--config"))["webadmin"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, web_config["baseUrl"])
    fixture.session.ensure_login(username=webadmin["username"], password=webadmin["password"])
    return fixture


@pytest.fixture
def orm(request):
    db_config = load_config(request.config.getoption("--config"))["db"]
    db_fixture = DbFixture(host=db_config["host"], db_name=db_config["name"], user=db_config["user"],
                           password=db_config["password"])

    return db_fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):

    def fin():
        if fixture is not None:
            fixture.session.ensure_logout()
            fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")
