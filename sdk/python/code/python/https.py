import urllib.request

class Connector:

    def connect(self,url):
        with urllib.request.urlopen(url) as response:
            body = response.read()

        return body;