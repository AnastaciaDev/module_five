# enforce the rule to abide by
from app.services.interface import MemberInterfaceService
from app.models import Member


class MemberService(MemberInterfaceService):

    def __init__(self, repository):
        self._repo = repository

    # Create
    def post_data(self, data):
        # handle validation

        member_data = Member(**data)
        return self._repo.post_data(member_data.to_dict())

    # Read  
    def list_all(self):
        return self._repo.get_all()

    def get_member(self, member_id):
        return self._repo.get_by_id(member_id)

    def get_by_email(self, member_email):
        pass

    def delete(self, member_id):
        return self._repo.delete_member(member_id)

    def update(self, member_id, data):

        existing_user = self._repo.get_by_id(member_id)
        if not existing_user:
            return None

        update_member = Member(**data)

        return self._repo.update_member(member_id, update_member.to_dict())
    