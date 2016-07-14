import abc
from abc_base import Integration

class HipChat(Integration):
    @property
    def room_id(self):
        return self.room_id

    @room_id.setter
    def room_id(self, value):
        self.room_id = value[u'item'][u'room'][u'name']

    @property
    def user(self):
        return self.user

    @user.setter
    def user(self, value):
        self.user = value[u'item'][u'message'][u'from'][u'mention_name']

    @property
    def command(self):
        return self.command

    @command.setter
    def command(self, value):
        self.command = value

    @property
    def command_message(self):
        return self.command_message

    @command_message.setter
    def command_message(self, value):
        msg = value[u'item'][u'message'][u'message']
        m = msg.split()
        # let's set the first word as the command
        self.command = m[0]
        temp = m[1:]
        self.command_message = " ".join(temp)
