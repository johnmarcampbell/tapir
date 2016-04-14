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
        self.query_dict = {}
        self.query_string = ''

    def GET(self, url, headers):
        """ Function to make API GET requests """
        return requests.get(url + self.query_string, headers = headers)
        
    def POST(self, url, headers):
        """ Function to make API POST requests """
        return requests.post(url, headers = headers)
        
    def DELETE(self, url, headers):
        """ Function to make API DELETE requests """
        return requests.delete(url, headers = headers)

    def add_query_parameter(self, parameter, value):
        """ Function to add query parameters to API requests """
        if parameter in self.query_dict:
           self.query_dict[parameter] += "," + value 
        else:
           self.query_dict[parameter] = value 

        self.make_query_string()
            

    def reset_query_parameters(self):
        """ Function to reset the query parameters for a resource to zero """
        self.query_dict = {}
        self.make_query_string()

    def make_query_string(self):
        """ Use self.query_dict to create self.query_string """
        self.query_string = '?'
        for k,v in self.query_dict.items():
            self.query_string += k + "=" + v + "&"
        self.query_string = self.query_string[:-1] #Remove last "&"
        
        

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

        return self.GET(self.base_url, headers)

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
        return self.GET(request_url, self.version_header)

    # TODO: Implement query parameters (game, channel, limit, etc.)
    def get(self):
        """
        GET /streams
        Returns a list of stream objects that are queried by a number of
        parameters sorted by number of viewers descending.
        """
        return self.GET(self.base_url, self.version_header)

    def featured(self):
        """
        GET /streams/featured
        Returns a list of featured (promoted) stream objects.
        """
        request_url = self.base_url + "/featured"
        return self.GET(request_url, self.version_header)

    def summary(self):
        """
        GET /streams/summary
        Returns a summary of current streams.
        """
        request_url = self.base_url + "/summary"
        return self.GET(request_url, self.version_header)
    
    def followed(self):
        """
        GET /streams/followed
        Returns a list of stream objects that the authenticated user is following.
        """
        request_url = self.base_url + "/followed"
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)

        return self.GET(request_url, headers)

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
        return self.GET(self.base_url, headers)

    def user(self, user):
        """
        GET /users/:user
        Returns a user object.
        """
        request_url = self.base_url + "s/" + user
        return self.GET(request_url, self.version_header)

class Channel(Resource):
    """ Class for Channel API resource """


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
        return self.GET(self.base_url, headers)
    
    def channel(self, channel):
        """
        GET /channels/:channel/
        Returns a channel object.
        """
        request_url = self.base_url + "s/" + channel
        return self.GET(request_url, self.version_header)
    
    def videos(self, channel):
        """
        GET /channels/:channel/videos
        Returns a list of videos ordered by time of creation, starting
        with the most recent from :channel.
        """
        request_url = self.base_url + "s/" + channel + "/videos"
        return self.GET(request_url, self.version_header)

    def follows(self, channel):
        """
        GET /channels/:channel/follows
        Returns a list of follow objects.
        """
        request_url = self.base_url + "s/" + channel + "/follows"
        return self.GET(request_url, self.version_header)
    
    def editors(self, channel):
        """
        GET /channels/:channel/editors
        Returns a list of user objects who are editors of :channel.
        """
        request_url = self.base_url + "s/" + channel + "/editors"
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)
        return self.GET(request_url, headers)

    def stream_key(self, channel):
        """
        DELETE /channels/:channel/stream_key
        Resets channel's stream key.
        """
        request_url = self.base_url + "s/" + channel + "/stream_key"
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)
        return self.DELETE(request_url, headers)
    
    def post(self, channel):
        """
        POST /channels/:channel/commercial
        Start commercial on channel.
        """
        request_url = self.base_url + "s/" + channel + "/commercial"
        headers = self.version_header.copy()
        if self.oauth:
            headers.update(self.oauth_header)
        return self.POST(request_url, headers)
    
    def teams(self, channel):
        """
        GET /channels/:channel/teams
        Returns a list of team objects :channel belongs to.
        """
        request_url = self.base_url + "s/" + channel + "/teams"
        return self.GET(request_url, self.version_header)
