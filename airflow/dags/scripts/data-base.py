from sqlalchemy import create_engine
from sqlalchemy import text
import psycopg2

class Connection:
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres/airflow", echo=True)
        self.schema_schema = "/opt/airflow/dags/scripts/schema/schema.sql"
        

    def create_table(self):
        """
        Create tables of schema
        """
        try:
            with self.engine.connect() as conn:
                with open(f'{self.schema_schema}') as file:
                    query = text(file.read())
                    conn.execute(query)
        except Exception as e:
            print(e)


    def df_to_sql(self, tablename, raw_df):
        """convert dataframe to sql data
        Args:
            raw_df: The dataframe
            tablename: The database table name
        """
        try:
            with self.engine.connect() as conn:
                raw_df.to_sql(name=tablename, con=conn, if_exists='replace', index=False)
        except Exception as e:
            print(f"Failed  ---- {e}")


