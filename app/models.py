class News:
    '''
    Class to define news objects
    '''
    def __init__(self,id,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
