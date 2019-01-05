"""
Sets up the flask application depending on configuration.
Valid configurations and details given in config.py.
"""

import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.config['SECRET_KEY'] = 'I <3 sfu2000'

@app.shell_context_processor
def make_shell_context():
    return dict()

if __name__ == '__main__':
    app.run()


