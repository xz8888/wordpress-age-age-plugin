import urllib2

class JobViteReciever:
    
    def __init__(self, url):
        self.url = url

    def getData(self):
        content = urllib2.urlopen(self.url).read()
        return content