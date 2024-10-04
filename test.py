import mysql.connector
from mysql.connector import Error
from datetime import datetime

def manage_numberplate_db(numberplate):
    """Connect to the MySQL database, create table, insert number plate, and fetch data."""
    
    # Fixed connection parameters
    host = "mysql-19dff4d2-freedomtech85-86f4.j.aivencloud.com"
    user = "avnadmin"
    password = "AVNS_p8_dV9ddaew1CwyFWzu"
    database = "defaultdb"
    port = 18038
    
    # Step 1: Connect to MySQL Server and existing database
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        print("Connection to MySQL DB successful")

        # Step 2: Create the new table 'numberplate'
        create_table_query = """
        CREATE TABLE IF NOT EXISTS numberplate (
            id INT AUTO_INCREMENT PRIMARY KEY,
            numberplate TEXT NOT NULL,
            entry_date DATE,
            entry_time TIME
        )
        """
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        print("Table created successfully")

        # Step 3: Insert data into the new table 'numberplate'
        insert_data_query = """
        INSERT INTO numberplate (numberplate, entry_date, entry_time)
        VALUES (%s, %s, %s)
        """
        current_date = datetime.now().date()  # Get current date
        current_time = datetime.now().time()  # Get current time
        data = (numberplate, current_date, current_time)  # Numberplate data
        cursor.execute(insert_data_query, data)
        connection.commit()
        print("Data inserted successfully")

        # Step 4: Retrieve and display data from the table
        fetch_data_query = "SELECT * FROM numberplate"
        cursor.execute(fetch_data_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

    except Error as e:
        print(f"Error: '{e}'")
    
    finally:
        # Close the connection
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

