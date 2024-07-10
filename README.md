# Todo-List App Project

## Project Setup Instructions

### Cloning the Repository
Clone the repository to your local machine using Git or download the ZIP directly from GitHub.

```bash
git clone https://github.com/ali9463/Todo-List
```

### Database Configuration
Before running the application, configure the database settings. You have two options: Microsoft SQL Server Studio or SQLite.

#### For Microsoft SQL Server
1. Open `database_manager.py` and `db_credentials.py`.
2. Replace the content with your SQL Server credentials:
   ```python
   sql_server_URI = f'mssql+pyodbc:///?odbc_connect={connection_URI}Encrypt=no'
   ```

#### For SQLite
1. Open `app.py`.
2. Go to line number 15 and replace the database URI configuration:
   ```python
   # app.py
   app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite'
   ```

### Running the Application
Start the Flask application using Python.

```bash
python app.py
```
# Sign Up Page

![WhatsApp Image 2024-07-10 at 12 23 07_b9b0aa26](https://github.com/ali9463/Todo-List-Website/assets/125659351/1aedd3fa-ad99-41c5-8247-8bbce212d3fb)

# Login Page

![WhatsApp Image 2024-07-10 at 12 20 46_b42dda4d](https://github.com/ali9463/Todo-List-Website/assets/125659351/08ae6095-d0f0-40ac-98b3-6d6b072c5677)

# Home Page

![WhatsApp Image 2024-07-10 at 12 24 15_228852e9](https://github.com/ali9463/Todo-List-Website/assets/125659351/60c02e23-6f5f-486b-b2c3-bbf2b6622701)


