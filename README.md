# Personal-Website
CV-Resume and Personal website

## Getting Started
To get started with this project, you will need to have Python and Django installed on your computer. You can follow the instructions on their respective websites to install them.

Once you have installed Python and Django, you can clone this repository to your local machine by running the following command:

```sh
$ git clone https://github.com/parsa-official/Personal-Website
$ cd backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source env/bin/activate
```

After cloning the repository and install virtualenv , navigate to the project directory and run the following commands to apply any necessary database migrations:

```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
```

These commands will create any necessary migration files based on the changes you have made to your models, and apply those changes to the database.

You can now run the development server by running the following command:

```sh
(venv)$ python manage.py runserver
```
You should now be able to access the website by opening your web browser and navigating to http://localhost:8000/.

## Creating a Superuser
To create a superuser account, which will allow you to access the Django admin interface and make changes to the website content, run the following command:

```sh
(venv)$ python manage.py createsuperuser
```

Follow the prompts to enter a username, email address, and password for the superuser account.

## Contributing
If you would like to contribute to this project, feel free to submit a pull request.
