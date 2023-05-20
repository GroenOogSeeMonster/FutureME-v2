from sqlalchemy import create_engine
import sys
import time

def check_db(uri):
    engine = create_engine(uri)

    try:
        connection = engine.connect()
    except Exception as e:
        print(e)
        return False

    connection.close()
    return True

if __name__ == "__main__":
    uri = sys.argv[1]

    while not check_db(uri):
        print("DB is not ready yet. Retrying in 5 seconds...")
        time.sleep(5)

    print("DB is ready.")