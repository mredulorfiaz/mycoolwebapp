import os

DB_PASS = open('/run/secrets/db_password').read().strip()

DB_HOST = os.getenv("DB_HOST", "db")

CONFIGURATION = {
    "track": "SQLALCHEMY_TRACK_MODIFICATIONS",
    "uri": "SQLALCHEMY_DATABASE_URI",
    "sqlite": "sqlite:///usersdb.sqlite",
    "host": "0.0.0.0",
    "mysql": f"mysql+pymysql://root:{DB_PASS}@{DB_HOST}/flask-application",
}
