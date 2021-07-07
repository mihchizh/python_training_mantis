

def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.logged_in_as("administrator")