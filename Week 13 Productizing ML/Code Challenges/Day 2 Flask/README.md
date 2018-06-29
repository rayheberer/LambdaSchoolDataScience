# ML-Hello-Flask
Repo for playing with basic Flask usage
--------------------------------------------------

This repository is for validating and demonstrating a basic Flask installation.
Flask is a simple "minimalist" web-application framework for the Python
programming language. Your goal is to create a basic initial Flask project -
first, ensure you have Python 3 installed:

```
$ python --version  # Should be >3
```

Next, you want to install Pipenv, a tool for managing packages and environments.
If you're using a Mac, run `brew install pipenv`, and if you're running Linux
check the package repository for your distribution to see if it has it.
Otherwise (including Windows), run `pip install pipenv` (this assumes you have
pip, but that should come with your Python installation).

Once you have Pipenv you can use it to start a new Python project. You should do
so in a new directory made inside your local clone of your fork of this
repository, so you can commit your work and submit via a pull request.

It's a good practice to specify the version of Python for your new project, e.g.
`pipenv --python 3` will start a new project with Python version 3.

Starting your project creates a `Pipfile` which will specify the metadata and
packages for your project. It will also create a virtual environment, which
keeps all your Python packages tidy and separate for each project.

The next command you should run is `pipenv install flask`, to specify Flask as
your first dependency. This will pull in both Flask and the packages it depends
on, and install them to your virtual environment. Pipenv also locks the versions
of all dependencies (with Pipfile.lock) - this is a good thing, as deterministic
builds are easier to debug. You don't have to worry about it, and shouldn't edit
the lock file by hand.

Lastly you need to activate the virtual environment, to actually load Flask and
its related libraries. This is done via `pipenv shell`.

Now you should be able to check the version of Flask and see something like:

```
$ flask --version
Flask 1.0.2
Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170118]
```

You can then create your first Flask app by making a file named `hello.py` with
the following code:

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

And then run the app by setting an environment variable pointing to the file and
executing `flask`:

```
$ export FLASK_APP=hello.py  # Set the Flask app to be the given file, MacOS/Linux
$ flask run
```

Other ways to set the `FLASK_APP` variable:

```
C:\path\to\app>set FLASK_APP=hello.py  # Windows command prompt
PS C:\path\to\app> $env:FLASK_APP = "hello.py"  # Windows PowerShell
```

You'll see something like:

```
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Try loading the given URL in your browser, and you should see "Hello, World!"

If you need help, check out the
[quickstart guide](http://flask.pocoo.org/docs/1.0/quickstart/), which gives
tips for debugging.

Gotten this far? Spend the rest of your time working through the
[official Flask tutorial](http://flask.pocoo.org/docs/1.0/tutorial/). It steps
through building a basic blog application, showing how to lay out a project,
set up and connect to a database, and generally build a simple but full-stack
application.

Want to see another, "heavier-duty" Python web application framework? Check out
[Django](https://github.com/LambdaSchool/Hello-Django)!
