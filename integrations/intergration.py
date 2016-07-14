from abc import ABCMeta, abstractmethod


class Integration:
    __metaclass__ = ABCMeta

    @abstractmethod
    def room_id(self):
        raise NotImplementedError
        return

    @abstractmethod
    def room_id(self, value):
        pass

    @abstractmethod
    def user(self):
        raise NotImplementedError
        return

    @abstractmethod
    def user(self, value):
        pass

    @abstractmethod
    def command(self):
        raise NotImplementedError
        return

    @abstractmethod
    def command(self, value):
        pass

    @abstractmethod
    def command_message(self):
        raise NotImplementedError
        return

    @abstractmethod
    def command_message(self, value):
        pass
