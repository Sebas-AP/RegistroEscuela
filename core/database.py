import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

supabase = None

def get_supabase_client():
    global supabase
    if supabase is None:
        if supabase_url and supabase_key:
            try:
                from supabase import create_client, Client
                supabase = create_client(supabase_url, supabase_key)
            except Exception as e:
                print("Error inicializando Supabase:", e)
    return supabase
