

def test_add_project(app, db):
    old_projects = db.get_project_list()
    name = app.project.generate_random_name()
    while name in old_projects:
        name = app.project.generate_random_name()
    app.session.Login("administrator", "root")
    app.project.create(name)
    new_projects = db.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(name)
    assert sorted(old_projects) == sorted(new_projects)



