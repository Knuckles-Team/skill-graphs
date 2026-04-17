# SQL (Relational) Databases[¶](https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases)
**FastAPI** doesn't require you to use a SQL (relational) database. But you can use **any database** that you want.
Here we'll see an example using [SQLModel](https://sqlmodel.tiangolo.com/).
**SQLModel** is built on top of **FastAPI** to be the perfect match for FastAPI applications that need to use **SQL databases**.
Tip
You could use any other SQL or NoSQL database library you want (in some cases called "ORMs"), FastAPI doesn't force you to use anything. 😎
As SQLModel is based on SQLAlchemy, you can easily use **any database supported** by SQLAlchemy (which makes them also supported by SQLModel), like:
  * PostgreSQL
  * MySQL
  * SQLite
  * Oracle
  * Microsoft SQL Server, etc.


In this example, we'll use **SQLite** , because it uses a single file and Python has integrated support. So, you can copy this example and run it as is.
Later, for your production application, you might want to use a database server like **PostgreSQL**.
Tip
There is an official project generator with **FastAPI** and **PostgreSQL** including a frontend and more tools:
This is a very simple and short tutorial, if you want to learn about databases in general, about SQL, or more advanced features, go to the [SQLModel docs](https://sqlmodel.tiangolo.com/).
