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
        self.new_article = Articles('Wycliffe Musalia','Tim Wanyonyi Kickstarts Westlands MP Campaigns Despite ODM Ticket Stalemate with Fred Gumo Son','Westlands MP Tim Wanyonyi dropped his gubernatorial bid after Azimio la Umoja leadership coerced him to back Polycarp Igathe','https://www.tuko.co.ke/politics/453154-tim-wanyonyi-kickstarts-westlands-mp-campaigns-despite-odm-ticket-stalemate-fred-gumos-son/','https://netstorage-tuko.akamaized.net/images/14a314fedd9bd531.jpg?imwidth=720','2022-04-02T05:22:26Z')

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article,Articles))