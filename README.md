# TopReddit

![alt text](https://github.com/robertyhou/TopReddit/blob/master/app/static/graph.png)

## Features
- Flask Web Server
- Query custom number of reddit posts using Reddit API
- Utilizes OAuth2 to authenticate user
- Select from /r/all or /r/popular
- Choose time range (Day, Week, Month, Year, All Time)
- Updates dynamically over time
- Protects against CSRF attacks

## Contributors:
- Robert Hou (@robertyhou)
- Samuel Fu (@samuelfu)

## Dependencies:
(also given in requirements.txt)
- astroid==2.0.4
- Click==7.0
- colorama==0.3.9
- dominate==2.3.5
- Flask==1.0.2
- Flask-Bootstrap==3.3.7.1
- Flask-Moment==0.6.0
- Flask-WTF==0.14.2
- isort==4.3.4
- itsdangerous==1.1.0
- Jinja2==2.10
- lazy-object-proxy==1.3.1
- MarkupSafe==1.1.0
- mccabe==0.6.1
- pylint==2.1.1
- six==1.11.0
- visitor==0.1.3
- Werkzeug==0.14.1
- wrapt==1.10.11
- WTForms==2.2.1

## How to run
1. `cd` to wanted directory
2. `git clone https://github.com/robertyhou/TopReddit` to clone
3. Make sure the dependencies are installed. Can be installed with 'pip install -r requirements.txt'
4. `cd` into the repository.
5. `export FLASK_APP=TopReddit.py` on OSX/Linux or `set FLASK_APP=TopReddit.py` on Windows
6. `flask run`
7. Open 'http://localhost:5000' in browser
