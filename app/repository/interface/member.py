# enforce the rule to abide by

from abc import ABC, abstractmethod

class MemberInterfaceRepo(ABC):

    # Create
    @abstractmethod
    def post_data(self, data):
        pass

    # Read
    @abstractmethod
    def get_by_email(self, email):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update_member(self, member_id, data):
        pass

    @abstractmethod
    def delete_member(self, member_id):
        pass

