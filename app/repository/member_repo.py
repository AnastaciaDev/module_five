# enforce the rule to abide by
from app.repository.interface import MemberInterfaceRepo


class MemberRepoWithDataStructures(MemberInterfaceRepo):

    def __init__(self, store):
        self._store = store

    # Create
    def post_data(self, member_data):
        # import a python debugger
        import pdb

        pdb.set_trace()
      
        self._store["member"].append(member_data)
        return member_data

    # Read
    def get_by_email(self, member_email):
        return next((member for member in self._store["member"] if member["email"] == member_email), None)

  
    def get_by_id(self, member_id):
        # import pdb; pdb.set_trace()
        return next((member for member in self._store["member"] if member.get("id") == member_id), None)

  
    def get_all(self):
        return list(self._store["member"])

    def delete_member(self, member_id):
        member = self.get_by_id(member_id)

        if not member:
            return False
        
        self._store["member"].remove(member)
        return True


    def update_member(self, member_id, data):
        member = self.get_by_id(member_id)

        if not member:
            return None
            
        member.update(data)
        return member
