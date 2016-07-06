import os

# let's import all the environment vars for the handler
imgur_id = os.environ.get('imgur_id', None)
imgur_secret = os.environ.get('imgur_secret', None)
google_api_key = os.environ.get('google_api_key', None)
google_cseid = os.environ.get('google_cseid', None)
DEBUG = os.environ.get('DEBUG', False)