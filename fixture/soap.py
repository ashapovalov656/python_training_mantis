from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def convert_projects_to_model(self, projects):
        def convert(project):
            return Project(id=str(project.id), name=project.name, desc=project.description)
        return list(map(convert, projects))

    def get_projects(self, username, pasword):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        #pp = client.service.mc_projects_get_user_accessible(username, pasword)
        #n = pp[0].id
        #qwe = 2
        return self.convert_projects_to_model(client.service.mc_projects_get_user_accessible(username, pasword))
