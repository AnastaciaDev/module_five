# enforce the rule to abide by

from abc import ABC, abstractmethod

class MemberInterfaceService(ABC):

    # Create
    @abstractmethod
    def post_data():
        ...

    # Read
    @abstractmethod
    def list_all():
        pass

    @abstractmethod
    def get_member():
        ...

    @abstractmethod
    def get_by_email():
        pass

    # update
    @abstractmethod
    def update(self, member_id, data):
        pass

    # delete
    @abstractmethod
    def delete(self, member_id):
        pass

