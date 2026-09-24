from abc import ABC, abstractmethod

class DepartmentInterfaceService(ABC):

    # Create
    @abstractmethod
    def post_data():
        pass

    # Read
    @abstractmethod
    def get_by_name():
        pass

    @abstractmethod
    def get_by_id():
        pass

    @abstractmethod
    def get_all():
        pass
