import random
import string

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("управление").click()
        wd.find_element_by_link_text("Управление проектами").click()

    def generate_random_name(self):
        symbols = string.ascii_letters + string.digits
        return "group" + "".join([random.choice(symbols) for i in range(random.randrange(10))])

    def create(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='создать новый проект']").click()
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(name)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()

