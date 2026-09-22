from typing import Dict, List, Any

store = {
    "users": []
}


def restore_data():
    for key in store:
        store[key].clear()

def seed_data():
    from app.models.user import User

    restore_data()

    store["users"].append(User(
        username="admin", 
        email="admin@hrms.io",
        role="admin"
    ).to_dict())

    store["users"].append(User(
        username="manager", 
        email="manager@hrms.io",
        employee_id="002", 
        role="manager"
    ).to_dict())

    store["users"].append(User(
        username="alice", 
        email="alice@hrms.io",
        employee_id="003", 
        role="employee"
    ).to_dict())

