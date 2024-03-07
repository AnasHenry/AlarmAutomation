import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.google.android.deskclock',
    appActivity='com.android.deskclock.DeskClock',
    language='en',
    locale='US'
)
url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(url, options=UiAutomator2Options().load_capabilities(capabilities))
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_navigate_to_alarm(self):
        # Getting input
        h = int(input("Enter hour (1 - 12): "))
        m = int(input("Enter minutes(00 - 55): "))
        cond = input("AM or PM? ").lower()

        # Click on the Alarm tab
        alarm_tab = self.wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Alarm")))
        alarm_tab.click()

        add_alarm = self.wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Add alarm")))
        add_alarm.click()

        hour_input = self.wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, f"{h} o'clock")))
        hour_input.click()

        minute_input = self.wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, f"{m} minutes")))
        minute_input.click()

        am_pm_selector = self.wait.until(EC.visibility_of_element_located(
            (AppiumBy.ID, f"com.google.android.deskclock:id/material_clock_period_{cond}_button")))
        am_pm_selector.click()

        ok_button = self.wait.until(EC.visibility_of_element_located(
            (AppiumBy.ID, "com.google.android.deskclock:id/material_timepicker_ok_button")))
        ok_button.click()

        # Wait for the alarm page to load
        time.sleep(2)  # Adjust this time according to your device's speed
        print("Alarm is successfully created..(つ▀¯▀ )つ")


if __name__ == '__main__':
    unittest.main()
