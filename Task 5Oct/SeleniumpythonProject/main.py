#Launch a url using selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def openAndTestUrl(url):
    driver = webdriver.Firefox()
    driver.get(url)
    assert "Google" in driver.title
    elem = driver.find_element("name", "q")
    #elem.clear()
    elem.send_keys("BYJUS")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()




if __name__ == '__main__':
    openAndTestUrl("https://google.com")

