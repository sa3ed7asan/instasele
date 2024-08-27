from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from instasele.methods import Methods
from instasele.logger import Logger

class Client(webdriver.Chrome, Methods):

    options: webdriver.ChromeOptions = webdriver.ChromeOptions()

    def __init__(
        self,
        headless: bool = False,
        wait_until_duration: int = 30,
    ):
        """Instagram Client

        Args:
            chrome_driver_path (str): chromedriver path
            headless (bool, optional): True if you don't need to see the browser. Defaults to False.
            wait_until_duration (int, optional): Increase it according to your internet speed. Defaults to 30.
            termux (bool, optional): True If You Use Termux. Defaults to False.

        Returns:
            instasele.Client: Instagram Client
        """              
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        if headless:
            self.options.add_argument("--headless=new")
        service = Service(executable_path=ChromeDriverManager().install())
        super().__init__(options=self.options, service=service)
        self.wait: WebDriverWait = WebDriverWait(self, wait_until_duration)

# selenium-3.141.0
# webdriver-manager-4.0.2