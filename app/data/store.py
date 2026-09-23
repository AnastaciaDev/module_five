from typing import Dict, List, Any

store = {
    "member": [],
    "dept" : []
}


def restore_data():
    for key in store:
        store[key].clear()

def seed_data():
    from app.models.user import Member

    restore_data()

    # store["member"].append(Member(
    #     Membername="admin", 
    #     email="admin@hrms.io",
    #     role="admin"
    # ).to_dict())

    # store["member"].append(Member(
    #     Membername="manager", 
    #     email="manager@hrms.io",
    #     employee_id="002", 
    #     role="manager"
    # ).to_dict())

    # store["member"].append(Member(
    #     Membername="alice", 
    #     email="alice@hrms.io",
    #     employee_id="003", 
    #     role="employee"
    # ).to_dict())

