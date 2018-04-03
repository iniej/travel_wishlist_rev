import selenium
from selenium import webdriver

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_shown_on_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Wishlist' in self.browser.title

class FunctionalityTests(LiveServerTestCase):
    fixtures = ['test_places']

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_add_new_place(self):
        # load home page of the website'''
        self.browser.get(self.live_server_url)
        # find input text box'''
        input_name = self.browser.find_element_by_id('id_name')
        # Enter place name
        input_name.send_keys('Denver')
        # Find the add button'''
        add_button = self.browser.find_element_by_id('add-new-place')
        # click the button'''
        add_button.click()

        # wait for new element to appear on the page'''
        wait_for_denver = self.browser.find_element_by_id('place-name-5')
        # Assert places from test_places are on web page'''
        assert 'Tokyo' in self.browser.page_source
        assert 'New York' in self.browser.page_source

        # Assert the new place is also in the web page'''
        assert 'Denver' in self.browser.page_source
