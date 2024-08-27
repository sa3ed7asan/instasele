from typing import Dict
from instasele.utils import get_element_by_child
import instasele


class Like:
    def like(client: "instasele.Client", post_url: str) -> Dict:
        """Like a post

        Args:
            post_url (str): Post URL

        Returns:
            Dict: Dictionry of response
        """
        client.set_window_size(412, 800)
        client.get(post_url)
        like_button = get_element_by_child(
            client,
            attr="role",
            attr_value="button",
            child_tag_name="svg",
            child_attr="aria-label",
            child_attr_value="Like",
        )
        if like_button:
            print(type(like_button))
            client.execute_script("arguments[0].click()", like_button)
            return {"status": "ok", "message": "post liked", "error_type": None}
        else:
            return {
                "status": "bad",
                "message": "cannot find like button",
                "error_type": "page_error",
            }
