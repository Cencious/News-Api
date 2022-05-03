import unittest
from app.model_articles import Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Polycarp Igathe Pays Tim Wanyonyi Courtesy Call Days after He Stepped Down for His Bid Read more: https://www.tuko.co.ke/politics/452803-polycarp-igathe-pays-tim-wanyonyi-courtesy-call-days-after-he-stepped-down-his-bid/')

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article,Articles))