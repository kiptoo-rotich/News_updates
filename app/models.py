class News:
    '''
    Class to define news objects
    '''
    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

class News_details:
    '''
    Class to define news_details objects
    '''
    def __init__(self, title, author, id, description, urlToImage, publishedAt, content):
        self.id = id
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.author = author