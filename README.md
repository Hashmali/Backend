
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Hashmali/backend.git
$ cd backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd backend
(env)$ python manage.py runserver
```
Then we can open the frontend clone and launch it.

To navigate to admin panel we go to `http://127.0.0.1:8000/admin/`.
and sign in with admin account.

In api file you can see the several apps in the project 
