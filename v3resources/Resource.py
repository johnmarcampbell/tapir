import requests

class Resource(object):
    """ Base class for API resources """


    def __init__(self, oauth = ''):
        """ Initialize some parameters """
        self.base_url =  'https://api.twitch.tv/kraken'
        self.version_header = {'Accept':'application/vnd.twitchtv.v3+json'}
        self.oauth = oauth
        if self.oauth:
            self.oauth_header = {'Authorization':'OAuth ' + oauth}

class Root(Resource):
    """ Class for Root API resource """


    def __init__(self, oath = ''):
        """ Initialize some parameters """
        Resource.__init__(self, oath)

    def get(self):
        """
        GET /
        Basic information about the API and authentication status. If you
        are authenticated, the response includes the status of your token and
        links to other related resources.
        """
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)

        return requests.get(self.base_url, headers = headers)
