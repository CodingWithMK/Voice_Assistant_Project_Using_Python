from selenium import webdriver

class Info():
    def __init__(self):
        self.driver = webdriver.Chrome('')

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        # search = self.driver.find_element_by_xpath('')
        

assist = Info()
assist.get_info("Hello")