class ImageParser():
    def __init__(self, pg, url):
        self.parseImage = pg.image.load(url)

    def parsedImageBroadcaster(self):
        return self.parseImage