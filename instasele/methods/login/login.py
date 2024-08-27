from instasele.methods.login.cookies import Cookies
from instasele.utils.helpers import read, write
from selenium.webdriver.common.by import By
from typing import Dict
from time import sleep
import instasele
import os


class Login(Cookies):
    def login(
        client: "instasele.Client",
        username: str,
        password: str = None,
        cookies_file: os.PathLike | str = None,
        use_cookies: bool = False,
        save_login: bool = False,
    ) -> Dict:
        """Login into an account using both username and password or cookies

        Args:
            username (str): Account username
            password (str, optional): Account password. Defaults to None.
            cookies_file (os.PathLike | str, optional): Local Cookies file. Defaults to None.
            use_cookies (bool, optional): True If You Want To Use Cookie File. Defaults to False.
            save_login (bool, optional): True If You Want To Save Cookies File. Defaults to False.

        Returns:
            Dict: Dictionry of response
        """
        on_success_return = {
            "status": "ok",
            "message": "logged in successfully",
            "error_type": None,
        }
        client.get("http://instagram.com")
        client.wait.until(
            lambda client: client.execute_script("return document.readyState")
            == "complete"
        )
        if use_cookies:
            cookies = read(cookies_file or f"./cookies/{username}.json")
            client.delete_all_cookies()
            client.load_cookies(cookies)
            client.refresh()
            return on_success_return
        else:
            username_input = client.find_element(By.NAME, "username")
            username_input.send_keys(username)
            password_input = client.find_element(By.NAME, "password")
            password_input.send_keys(password)
            submit = client.find_element(By.XPATH, "//button[@type='submit']")
            submit.click()
            sleep(10)
            client.wait.until(
                lambda client: client.execute_script("return document.readyState")
                == "complete"
            )
            sleep(5)
            if "Sorry, your password was incorrect." in client.page_source:
                return {
                    "status": "bad",
                    "message": "incorrect password",
                    "error_type": "credintials",
                }
            elif "Save your login info?" not in client.page_source:
                return {
                    "status": "bad",
                    "message": "Please, check your username and password",
                    "error_type": "unknown",
                }
            elif save_login and "Save your login info?" in client.page_source:
                if not os.path.exists("cookies"):
                    os.mkdir("cookies")
                submit_save_info_button = client.find_element(
                    By.XPATH, "//button[@type='button']"
                )
                submit_save_info_button.click()
                cookies = client.get_cookies()
                client.save_cookies(cookies, "cookies/" + username + ".json")
                on_success_return["message"] += " (login saved)"
                return on_success_return
            elif "Save your login info?" in client.page_source:
                return on_success_return
            else:
                return {
                    "status": "unknown",
                    "message": "unknown",
                    "error_type": "unknown",
                }
