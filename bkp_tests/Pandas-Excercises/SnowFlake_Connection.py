import snowflake.connector
import pandas as pd

# 1. Establish the connection
conn = snowflake.connector.connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT_IDENTIFIER',  # Format: 'orgname-accountname'
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA'
)

try:
    # 2. Open a cursor and execute the query
    cursor = conn.cursor()
    query = "SELECT * FROM my_table;"
    cursor.execute(query)
    
    # 3. Fetch results directly as a Pandas DataFrame
    df = cursor.fetch_pandas_all()
    print(df.head())

finally:
    # 4. Clean up resources
    cursor.close()
    conn.close()