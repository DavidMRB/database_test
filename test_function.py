import json
import pytest
from print_users import returnData
from db_query import fetch_users    

def test_returnData_db():
    users_from_db = fetch_users()
    json_result = returnData(users_from_db)
    
    data = json.loads(json_result)
    assert isinstance(data, list)
    assert len(data) == len(users_from_db)