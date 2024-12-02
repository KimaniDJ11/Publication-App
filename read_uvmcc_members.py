import pandas as pd
from sqlalchemy import create_engine

# Database configuration for the reader user
db_config = {
    'user': 'guckele_reader',
    'password': 'Lw:_wxZW}mz(W!t9%+J9',
    'host': 'webdb.uvm.edu',
    'database': 'GUCKELE_VCC'
}

# Create the database connection string
connection_string = f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"

# SQL query to fetch data from the uvmcc_members table
query = """
SELECT 
    slate_id, first_name, last_name, middle_initial, external_member, 
    membership_level_id, research_program_id, valid_from, current
FROM 
    uvmcc_members;
"""

def fetch_data_with_sqlalchemy():
    try:
        # Create the SQLAlchemy engine
        engine = create_engine(connection_string)
        print("Successfully connected to the database using SQLAlchemy.")
        
        # Use pandas to execute the query and fetch the data
        df = pd.read_sql(query, engine)
        print("Data successfully fetched from the uvmcc_members table.")
        return df

    except Exception as e:
        print(f"Error: {e}")
        return None

# Fetch data
data = fetch_data_with_sqlalchemy()

if data is not None:
    # Display the first few rows of the DataFrame
    print(data.head())
    # Save the data to a CSV file (optional)
    #output_file = 'data/UVMCC_Members_Export.csv'
    #data.to_csv(output_file, index=False)
    #print(f"Data saved to {output_file}")
