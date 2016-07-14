from bottle import Bottle, run, request, response
from hipchat import HipChat
from slack import Slack


class Handler:
    @property
    def request_json(self):
        return self.request_json

    @request_json.setter
    def request_json(self, value):
        self.request_json = value

    @property
    def chat_client(self):
        return self.chat_client

    @chat_client.setter
    def chat_client(self, value):
        self.chat_client = value

    """Let's set up the necessary variables upon initializing"""
    def __init__(self, req):
        self.request_json = req.json

        if self.request_json[u'item']:
            self.chat_client = HipChat()
        else:
            self.chat_client = Slack()



        self.chat_client.message = self.request_json

        # self.command_message = self.request_json[u'item'][u'message'][u'message']
        # self.room_id = self.request_json[u'item'][u'room'][u'name']

        response.content_type = 'application/json'

        derp = request.json
        msg = derp
        room = derp[u'item'][u'room'][u'name']
        who = derp[u'item'][u'message'][u'from'][u'mention_name']
        m = msg.split()
        command = m[0]
        parsed = m[1:]
        parsed = " ".join(parsed)
