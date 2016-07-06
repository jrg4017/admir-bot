from bottle import Bottle, run, request, response

class Handler:
    @property
    def request_json(self):
        return self.request_json

    @request_json.setter
    def request_json(self, value):
        self.request_json = value

    """Let's set up the necessary variables upon initializing"""
    def __init__(self):
        self.request_json = request.json

        # if

        self.command_message = self.request_json[u'item'][u'message'][u'message']
        self.room_id = self.request_json[u'item'][u'room'][u'name']

        response.content_type = 'application/json'

        derp = request.json
        msg = derp
        room = derp[u'item'][u'room'][u'name']
        who = derp[u'item'][u'message'][u'from'][u'mention_name']
        m = msg.split()
        command = m[0]
        parsed = m[1:]
        parsed = " ".join(parsed)


# @app.route('/', method='POST')
# def handle():
