import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news = News(12345,"BBC NEWS","If you drive past potholes and faded lane dividers on your morning commute to work, chances are you’ll continue to see such road blemishes until someone alerts the local department of transportation to the problem by filing a complaint. Utah-based startup Bly…","http://127.0.0.1:5000/technology","Technology")

    def test_instance(self):
        self.assertTrue(isinstance(self.news,News))