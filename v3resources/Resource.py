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


    def __init__(self, oauth = ''):
        """ Initialize some parameters """
        Resource.__init__(self, oauth)

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

class Stream(Resource):
    """ Class for Stream API resource """



    def __init__(self, oauth = ''):
        """ Initialize some parameters """
        Resource.__init__(self, oauth)
        self.base_url += "/streams"

    def channel(self, channel):
        """ 
        GET /streams/:channel/    
        Returns a stream object if live.
        """
        request_url = self.base_url + "/" + channel
        return requests.get(request_url, headers = self.version_header)

    # TODO: Implement query parameters (game, channel, limit, etc.)
    def get(self):
        """
        GET /streams
        Returns a list of stream objects that are queried by a number of
        parameters sorted by number of viewers descending.
        """
        return requests.get(self.base_url, headers = self.version_header)

    def featured(self):
        """
        GET /streams/featured
        Returns a list of featured (promoted) stream objects.
        """
        request_url = self.base_url + "/featured"
        return requests.get(request_url, headers = self.version_header)

    def summary(self):
        """
        GET /streams/summary
        Returns a summary of current streams.
        """
        request_url = self.base_url + "/summary"
        return requests.get(request_url, headers = self.version_header)
    
    def followed(self):
        """
        GET /streams/followed
        Returns a list of stream objects that the authenticated user is following.
        """
        request_url = self.base_url + "/followed"
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)

        return requests.get(request_url, headers = headers)

class User(Resource):
    """ Class for User API resource """



    def __init__(self, oauth = ''):
        """ Initialize some parameters """

        Resource.__init__(self, oauth)
        self.base_url += "/user"

    def get(self):
        """
        GET /user
        Returns a user object.
        """
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)
        return requests.get(self.base_url, headers = headers)

    def user(self, user):
        """
        GET /users/:user
        Returns a user object.
        """
        request_url = self.base_url + "s/" + user
        return requests.get(request_url, headers = self.version_header)

class Channel(Resource):
    """
    DOCSTRING
    """


    def __init__(self, oauth = ''):
        """ Initialize some parameters """
        Resource.__init__(self, oauth)
        self.base_url += "/channel"

    def get(self):
        """
        GET /channel
        Returns a channel object.
        """
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)
        return requests.get(self.base_url, headers = headers)
    
    def channel(self, channel):
        """
        GET /channels/:channel/
        Returns a channel object.
        """
        request_url = self.base_url + "s/" + channel
        return requests.get(request_url, headers = self.version_header)
    
    def videos(self, channel):
        """
        GET /channels/:channel/videos
        Returns a list of videos ordered by time of creation, starting
        with the most recent from :channel.
        """
        request_url = self.base_url + "s/" + channel + "/videos"
        return requests.get(request_url, headers = self.version_header)

    def follows(self, channel):
        """
        GET /channels/:channel/follows
        Returns a list of follow objects.
        """
        request_url = self.base_url + "s/" + channel + "/follows"
        return requests.get(request_url, headers = self.version_header)
    
    def editors(self, channel):
        """
        GET /channels/:channel/editors
        Returns a list of user objects who are editors of :channel.
        """
        request_url = self.base_url + "s/" + channel + "/editors"
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)
        return requests.get(request_url, headers = headers)

    def stream_key(self, channel):
        """
        DELETE /channels/:channel/stream_key
        Resets channel's stream key.
        """
        request_url = self.base_url + "s/" + channel + "/stream_key"
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)
        return requests.delete(request_url, headers = headers)
    
    def post(self, channel):
        """
        POST /channels/:channel/commercial
        Start commercial on channel.
        """
        request_url = self.base_url + "s/" + channel + "/commercial"
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)
        return requests.post(request_url, headers = headers)
    
    def teams(self, channel):
        """
        GET /channels/:channel/teams
        Returns a list of team objects :channel belongs to.
        """
        request_url = self.base_url + "s/" + channel + "/teams"
        return requests.get(request_url, headers = self.version_header)
