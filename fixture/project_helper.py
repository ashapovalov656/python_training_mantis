

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.app.open_homepage()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.desc)

    def delete_project_by_id(self, project_id):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//a[@href='manage_proj_edit_page.php?project_id=%s']" % project_id).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        # confirm delete
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.app.open_homepage()
