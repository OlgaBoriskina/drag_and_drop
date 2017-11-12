from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import drag_and_drop

import autorization
import unittest

base_url = "http://way2automation.com/way2auto_jquery"
frame_locator = "//iframe[@src='droppable/default.html']"


class Test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get(base_url)
        self.wait = WebDriverWait(self.driver, 10)
        autorization.autirize(self.wait)
        self.driver.refresh()
        self.driver.get(base_url + "/droppable.php")

    def test_action_submenu(self):
        move = drag_and_drop.move(self.driver, self.wait)
        assert (move == "Dropped!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()