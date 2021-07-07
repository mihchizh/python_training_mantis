

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.manage-menu-link").click()
        wd.find_element_by_xpath("//*[@id='manage-menu']/ul/li[3]/a").click()

    def generate_random_name(self):
        symbols = string.ascii_letters + string.digits
        return "group" + "".join([random.choice(symbols) for i in range(random.randrange(10))])

