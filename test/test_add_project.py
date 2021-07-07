

def add_project(app, db):
    old_projects = db.get_project_list()
    name = app.project.generate_random_name
    app.project.create(name)
    new_projects = db.get_project_list()
    old_projects.append(name)
    assert old_projects == new_projects
