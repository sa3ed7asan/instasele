from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from typing import Dict
import instasele


class Comment:
    def comment(client: "instasele.Client", post_url: str, cmnt: str = "❤") -> Dict:
        """Add Comment To a Post

        Args:
            post_url (str): Post URL
            cmnt (str, optional): Comment. Defaults to "❤".

        Returns:
            Dict: Dictionry of response
        """
        client.set_window_size(1920, 1080)
        client.get(post_url)
        client.wait.until(
            lambda client: client.execute_script("return document.readyState")
            == "complete"
        )

        try:
            form = client.wait.until(
                lambda client: client.execute_script(
                    'return document.querySelector("form");'
                )
            )
            textarea = client.execute_script(
                "return arguments[0].querySelector('textarea')", form
            )

            if textarea:
                attempts = 0
                while attempts < 3:
                    try:
                        client.execute_script(
                            "arguments[0].setAttribute('data-focus-visible-added', 'true')",
                            textarea,
                        )
                        textarea.send_keys(cmnt)
                        break
                    except StaleElementReferenceException:
                        form = client.wait.until(
                            lambda client: client.execute_script(
                                'return document.querySelector("form");'
                            )
                        )
                        textarea = client.execute_script(
                            "return arguments[0].querySelector('textarea')", form
                        )
                        attempts += 1
                form_buttons = client.execute_script(
                    "return arguments[0].querySelectorAll('div[role=\\'button\\']');",
                    form,
                )
                post_button = form_buttons[-1]
                client.execute_script("arguments[0].click()", post_button)
                return {"status": "ok", "message": "post commented", "error_type": None}
            else:
                return {
                    "status": "bad",
                    "error": "cannot find comment textarea",
                    "error_type": "page_error",
                }
        except (
            StaleElementReferenceException,
            NoSuchElementException,
            TimeoutException,
        ) as e:
            return {"status": "bad", "error": str(e), "error_type": type(e).__name__}
