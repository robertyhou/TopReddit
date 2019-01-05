import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.config['SECRET_KEY'] = 'I <3 sfu2000'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.shell_context_processor
def make_shell_context():
    return dict()


"""@app.cli.command()
def test():
    Run the unit tests.
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)"""
