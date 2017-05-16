#!usr/bin/env python
import os
from app import create_app, user_db
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
manager = Manager(app)
migrate = Migrate(app, user_db)

def make_shell_context():
    return dict(app=app, db=user_db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("user_db", MigrateCommand)
manager.add_command("runserver", Server(
    host='example.local',
    port=5000
))

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()
