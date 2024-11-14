from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://postgres:1234@localhost:5432/email_monitoring')
SessionLocal = sessionmaker(bind=engine)


def create_tables():
    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()


        for table in tables:
            with engine.connect() as conn:
                conn.execute(f"TRUNCATE TABLE {table} CASCADE")


        Base.metadata.create_all(bind=engine)
        return True

    except Exception as e:
        print(f"Error creating tables: {str(e)}")
        return False