<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Django ORM Relationships

### Setup Instruction

The structure of the whole Django project is built for you. Run the following commands in order to have your local environment up and running.  

```bash
$ mkvirtualenv -p $(which python3) django_orm_relationships
$ pip install -r requirements.txt
$ make migrate
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```

A command to load some initial data into your database is also provided.

```bash
$ make load_initial_data
```

You should see an `Imported!` message when the command execution finishes. That mean all initial data was imported successfully.

This will also create a superuser (user: `admin`, password: `admin`) that you can use when you point to `http://localhost:8080/admin` in your browser with the server running. You will find the Django admin site where you can create, delete and modify objects from your database.


### Your Tasks

For this practice you will work inside the `artists/orm_exercises.py` file. You'll find there a couple of functions that are the tasks you have to implement, using the different ORM methods that are provided by the Django `objects` manager.
Each of the task has its instructions as a docstring, so use them as a guide to know what you have to do.

In order to check if you implemented them correctly, there are tests associated to each task inside the `artists/tests.py`. You can run the tests like this:

```bash
$ make test
```
