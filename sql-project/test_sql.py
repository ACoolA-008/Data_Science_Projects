import sqlite3
import pytest

@pytest.fixture(scope="module")
def db_connection():
    conn = sqlite3.connect(":memory:")
    with open("sql-project/schema.sql", "r") as f:
        conn.executescript(f.read())
    with open("sql-project/data.sql", "r") as f:
        conn.executescript(f.read())
    yield conn
    conn.close()

def test_job_table_exists(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='JOB';")
    assert cursor.fetchone() is not None, "JOB table does not exist"

def test_data_inserted_into_job(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM JOB;")
    count = cursor.fetchone()[0]
    assert count > 0, "No data found in JOB table"
