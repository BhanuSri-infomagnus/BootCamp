
from json_py import DatabaseConnector  
import json


def main():
    db = DatabaseConnector(
        server='DESKTOP-OK8NL61\\SQLEXPRESS',
        database='AdventureWorksDW2022',
        username='Bhanu',
        password='admin'
        )
    
    try:
        country_data = {
            "country": "Afghanistan",
            "capital": "Kabul",
            "currency":"AFA",
            "languages": ["Pashto", "Dari"]

            }
        
       
        print("Updating JSON data...")
        update_success = db.execute_query(
            "UPDATE DimCurrency SET Country = ? WHERE CurrencyAlternateKey = ?",
            (json.dumps(country_data), "AFA")
        )
        
        if update_success:
            print("Successfully updated JSON data")
        
        # 2. QUERY JSON COLUMN using execute_query
        print("\nFetching updated data:")
        db.cursor.execute(
            "SELECT * FROM DimCurrency where Country IS NOT NULL"
        )
        result = db.cursor.fetchall()
        
        if result:
            for row in result:
                print(row)
        
        # Update record
        
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure connection is closed
        if(db):
            db.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()