import sys
import sqlite3
import pandas as pd

def update_db(csv_file, db_file, table_name):
    df = pd.read_csv(csv_file)
    conn = sqlite3.connect(db_file)
    df.to_sql(table_name, conn, index=False)
    conn.close()
    print(f"✅ Replaced table '{table_name}' with {len(df)} rows.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 csv_to_sqlite.py <csv_file> <db_file> <table_name>")
        sys.exit(1)

    csv_file = sys.argv[1]
    db_file = sys.argv[2]
    table_name = sys.argv[3]

    update_db(csv_file, db_file, table_name)
