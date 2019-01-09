"""
Sets up the flask application depending on configuration.
Valid configurations and details given in config.py.

app.config is dictionary for storing stuff about the
application itself. 'SECRET_KEY' used to configure
CSRF protection. 'SEND_FILE_MAX_AGE_DEFAULT' sets max file
age to 0 so they aren't cached, which allows new graph
to load on each request.
"""

import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.config['SECRET_KEY'] = 'I <3 sfu2000'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.shell_context_processor
def make_shell_context():
    return dict()

if __name__ == '__main__':
    app.run()


