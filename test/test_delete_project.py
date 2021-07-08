import random


def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(name)
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.session.Login("administrator", "root")
    app.project.delete(project)
    new_projects = db.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects