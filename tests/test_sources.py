import unittest
from app.models_sources import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test behaviour of the source class
    '''
    def setUp(self):
        '''
        Method to run before every Test
        '''
        self.new_source= Source( "aljazeera","Aljazeera","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at aljazeera.com.","https://aljazeera.com","general","en","USA")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()