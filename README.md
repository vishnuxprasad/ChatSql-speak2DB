# ChatSQL

ChatSQL is a Django-based project that enables users to communicate with databases (SQL and PostgreSQL) using natural language queries and receive natural language responses. This project leverages the LangChain module and the OpenAI API to facilitate this conversational interaction.

## Prerequisites

Before you can run the ChatSQL project, make sure you have the following dependencies installed:

- [Django](https://www.djangoproject.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [pymysql](https://pypi.org/project/pymysql/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [langchain](https://pypi.org/project/langchain/) (version 0.0.209)
- [openai](https://pypi.org/project/openai/)

You can install these dependencies using `pip` with the following commands:

```
pip install Django
pip install python-dotenv
pip install pymysql
pip install psycopg2
pip install langchain==0.0.209
pip install openai
```
## Getting Started

Follow these steps to run the ChatSQL project:

1. Clone the repository:

   ```
   git clone https://github.com/vishnuxprasad/ChatSql-speak2DB.git
   ```

2. Create a virtual environment (optional but recommended):

   ```python
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
      ```python
      venv\Scripts\activate
      ```
   - On macOS and Linux:
      ```python
      source venv/bin/activate
      ```

4. Install project dependencies:

    ```
    pip install -r requirements.txt
   ```

5. Set up environment variables by creating a .env file in the project directory and adding your database credentials and OpenAI API key:

   ```
   # .env

   DATABASE_URL=your_database_url
   OPENAI_API_KEY=your_openai_api_key
   ```

6. Run database migrations:

   ```python
   python manage.py migrate
   ```

7. Start the Django development server:

   ```python
   python manage.py runserver
   ```

8. Access the ChatSQL web interface by opening your browser and navigating to http://localhost:8000.

## Usage
To connect with a database and interact with ChatSQL, follow these steps:

1. Open the ChatSQL web interface.

2. Provide the necessary database credentials and connect to the database.

3. Enter natural language queries related to the database connected.

4. ChatSQL will process your queries using LangChain and OpenAI, and provide natural language responses.