from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

frame_locator = "//iframe[@src='droppable/default.html']"
menu_with_sub_locator = "//a[@href='#example-1-tab-2']"
drag_locator = 'id("draggable")'
drop_locator = 'id("droppable")'


class DragAndDrop:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def switch_to_frame(self):
        frame = self._wait.until(expected.element_to_be_clickable((By.XPATH, frame_locator)))
        self._driver.switch_to.frame(frame)

    def drag_and_drop(self):
        self.switch_to_frame()
        source_element = self._wait.until(expected.element_to_be_clickable((By.XPATH, drag_locator)))
        dest_element = self._wait.until(expected.element_to_be_clickable((By.XPATH, drop_locator)))
        ActionChains(self._driver).drag_and_drop(source_element, dest_element).perform()
        return dest_element.text