# Django Query Inspector

A lightweight Django middleware to log and analyze database queries per request.
This tool helps developers identify inefficient ORM usage such as duplicate queries and performance bottlenecks.

---

## Features

* Logs total database queries per request
* Displays total request execution time
* Detects duplicate SQL queries
* Helps debug ORM inefficiencies during development

---

## How It Works

The middleware intercepts each request and:

1. Captures all executed database queries
2. Calculates total query count and execution time
3. Identifies duplicate queries
4. Prints a structured report in the terminal

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/itsrajat07/django-query-inspector.git
cd django-query-inspector
```

2. Create virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install django
```

3. Add middleware to your Django project:

```python
MIDDLEWARE = [
    ...
    'db_inspector.middleware.QueryLoggerMiddleware',
]
```

4. Run the server:

```bash
python manage.py runserver
```

---

## Example Output

```
====== DB QUERY REPORT ======
Total Queries: 2
Duplicate Queries: 0
Total Request Time: 0.0123s
1. SELECT ... (0.001s)
2. SELECT ... (0.002s)
====== END REPORT ======
```

---

## Use Case

This tool is intended for development environments to:

* Debug database performance issues
* Understand ORM behavior
* Optimize query usage in Django applications

---

## Note

* Works only when `DEBUG = True`
* Not intended for production use

---

## Author

Rajat Kumar
