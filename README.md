<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Django ORM Relationships

### Setup Instruction

The structure of the whole Django project is built for you. Run the following commands in order to have your local environment up and running.

```bash
$ mkvirtualenv -p $(which python3.5) django_orm_relationships
$ pip install -r requirements.txt
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```

You will have a superuser already created (username: `admin`, password: `admin`) that you can use when you point to `http://localhost:8080/admin` in your browser with the server running. There you can find the Django admin site where you will be able to create, delete and modify objects from your database.

The database already contains some objects that we have created for you, but feel free to interact with it the way you want.


### Your Tasks

For this practice you will work inside the `artists/orm_exercises.py` file. You'll find there a couple of functions that are the tasks you have to implement, using the different ORM methods that are provided by the Django `objects` manager.
Each of the task has its instructions as a docstring, so use them as a guide to know what you have to do.

In order to check if you implemented them correctly, there are tests associated to each task inside the `artists/tests.py`. You can run the tests like this:

```bash
$ py.test django_orm_relationships/artists/tests.py -k task_1
$ py.test django_orm_relationships/artists/tests.py -k task_2
$ py.test django_orm_relationships/artists/tests.py -k task_N  # replace with the current function
```
