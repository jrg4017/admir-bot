import abc
from abc_base import Integration


class Slack(Integration):
    @property
    def room_id(self):
        return self.room_id

    @room_id.setter
    def room_id(self, value):
        self.room_id = value[u'channel_id']

    @property
    def user(self):
        return self.user

    @user.setter
    def user(self, value):
        self.user = value[u'user_id']

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
        msg = value[u'text']
        m = msg.split()
        # let's set the first word as the command
        self.command = m[0]
        temp = m[1:]
        self.command_message = " ".join(temp)
