from typing import Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import instasele


class Follow:
    def follow(client: "instasele.Client", account_url: str) -> Dict:
        """Follow an account

        Args:
            account_url (str): Account URL

        Returns:
            Dict: Dictionry of response
        """
        client.get(account_url)
        client.wait.until(
            lambda client: client.execute_script("return document.readyState")
            == "complete"
        )
        follow_button = client.wait.until(
            EC.element_to_be_clickable((By.TAG_NAME, "button"))
        )
        if (
            follow_button
            and follow_button.text
            and follow_button.text.lower() == "follow"
        ):
            follow_button.click()
            return {"status": "ok", "message": "account followed", "error_type": None}
        else:
            return {
                "status": "bad",
                "message": "cannot find follow button",
                "error_type": "page_error",
            }
