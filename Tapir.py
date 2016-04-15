import json
from v3resources.Resource import *


class Tapir(object):
    """ Tapir """


    def __init__(self, oauth = ''):
        """ Initialize some parameters """
        self.oauth = oauth

    def get_stream(self, channel_name):
        """ Make an API request for a stream object corresponding to channel_name """
        self.stream = json.loads(Stream().channel(channel_name).text)
        

    def channel_is_streaming(self, channel_name = ''):
        """ Check to see if a channel is streaming """ 
        
        self.get_stream(channel_name)
        stream_json = self.stream['stream']
        if stream_json is None:
            return False
        else:
            print(stream_json['channel']['name'])
            print(stream_json['game'])
            print(stream_json['viewers'])
            print(stream_json['created_at'])
            return True
