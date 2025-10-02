import json
from db_query import fetch_users
from db_simulation import simulated_users

def returnData(users: list) -> str:
    json_data = json.dumps(users, indent=4, ensure_ascii=False)
    return json_data

if __name__ == "__main__":
    print(returnData(fetch_users()))