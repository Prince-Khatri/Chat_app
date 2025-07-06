# Chat App – Django Project

* A Django web application for managing users, groups, and messages using pure SQL queries and MySQL integration.
* A simple chat application built using Django and MySQL, developed as a DBMS assignment using native SQL queries.

## Features

- User authentication and registration
- Group creation and messaging
- Admin functionality
- Uses native SQL queries instead of Django ORM
- Deployed using Render and TiDB Cloud

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
