import os

class Config:
    # We build the database URI from environment variables
    # Format: mysql+pymysql://user:password@host/db_name
    MYSQL_USER = os.environ.get('DB_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('DB_PASSWORD', 'rootpassword')
    MYSQL_HOST = os.environ.get('DB_HOST', 'mysql') # Service name in K8s
    MYSQL_DB = os.environ.get('DB_NAME', 'todo_db')
    
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False