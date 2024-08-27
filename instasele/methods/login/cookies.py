from instasele.utils.helpers import write
from selenium import webdriver
from typing import Dict
from json import dump


class Cookies:
    """
    A utility class for managing cookies with Selenium WebDriver.

    This class provides methods to load cookies into a WebDriver instance and save cookies
    to a JSON file. It simplifies the process of maintaining session data for web automation.
    """

    def load_cookies(
        driver: webdriver.Chrome, cookies: Dict, url="https://instagram.com"
    ):
        """
        Load cookies into a Selenium WebDriver instance.

        :param cookies: List of cookies (as dictionaries) to be loaded into the WebDriver.
        :param url: The URL of the domain where cookies should be loaded.
                    Defaults to "https://instagram.com". If None, the domain will be inferred from the cookies.
        """
        if url:
            driver.get(url)
        else:
            domain = cookies[0]["domain"]
            driver.get(f"http://{domain}")
        for cookie in cookies:
            if "sameSite" in cookie:
                del cookie["sameSite"]
            driver.add_cookie(cookie)

    def save_cookies(driver: webdriver.Chrome, cookies, file_path="cookies.json"):
        """
        Save cookies to a JSON file.

        :param cookies: A list of cookies (as dictionaries) to be saved.
        :param file_path: The file path where the cookies will be saved as a JSON file.
                          Defaults to "cookies.json".
        """
        write(cookies, file_path)
