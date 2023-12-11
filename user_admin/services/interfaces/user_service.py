import abc

class UserService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_by_id(self, id):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def create(self, user):
        pass

    @abc.abstractmethod
    def update(self, id):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

    @abc.abstractmethod
    def get_all_active(self):
        pass