import os
from unittest import result
from urllib import response
from dotenv import load_dotenv
from notion_client import Client
import pandas as pd 
import sqlite3

def fetch_datasource(datasource_id: str):

    try: 
        notion_token= os.getenv("NOTION_TOKEN")
        notion = Client(auth= notion_token)

        response = notion.data_sources.query(data_source_id=datasource_id)

    except Exception as e:
        print(f"Erreur de connexion à notion api : {e}")
        return None

    print("Datasource fetched successfully.")

    return response.get("results")


def extract_entry(entry):
    properties = entry.get('properties', {})
    result = {}

    for prop_name, prop_data in properties.items():
        prop_type = prop_data.get('type')

                                
        if prop_type == 'date':
            date_obj = prop_data.get('date')
            result [prop_name] = date_obj.get('start') if date_obj else None



        elif prop_type == 'select':
            select_obj = prop_data.get('select')
            result [prop_name] = select_obj.get('name') if select_obj else None


        elif prop_type == 'status':
            status_obj = prop_data.get('status')
            result [prop_name] = status_obj.get('name') if status_obj else None


        elif prop_type == 'url':
            result [prop_name] = prop_data.get('url') 


        elif prop_type == 'title':
            title_arr = prop_data.get('title')
            result [prop_name] = title_arr[0].get('plain_text') if title_arr else None



    return result


def sqliteWrite(df_entry):

    conn = sqlite3.connect('notion_pipe.db')
    df_entry.to_sql('learnings', conn, if_exists='replace', index=False)
    conn.close()
   

def main(): 
    load_dotenv()
    datasource_id= os.getenv("DATA_SOURCE_ID")
    learnings = fetch_datasource(datasource_id)
    if learnings:
        print("Learnings Extracted Successfully.")
        print(f"Number of learnings extracted: {len(learnings)}")

    
    entriesExtracted = []
    for entry in learnings:
        entriesExtracted.append(extract_entry(entry))

    df_entry = pd.DataFrame(entriesExtracted)
    print(df_entry.head())

    df_entry.columns = df_entry.columns.str.lower().str.replace(" ", "_")

    df_entry['date_started'] = pd.to_datetime(df_entry['date_started'])
    #print(df_entry.info())
    #df_entry.to_csv("learnings_data.csv", index=False)

    sqliteWrite(df_entry)

    print("Extraction Finished Successfully.")

if __name__ == "__main__":
    main()
       