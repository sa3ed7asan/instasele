from selenium.webdriver.remote.webelement import WebElement
import instasele
import time


def get_element_by_child(
    client: "instasele.Client",
    tag: str = "div",
    attr: str | None = None,
    attr_value: str | None = None,
    child_tag_name: str | None = None,
    child_attr: str = "aria-label",
    child_attr_value: str | None = None,
) -> WebElement | None:
    """Get HTML Element By Its Child

    Args:
        client (instasele.Client): Custom Chrome Driver From InstaSele
        tag (str, optional): Element to be gotten. Defaults to "div".
        attr (str | None, optional): Element Attribute. Defaults to None.
        attr_value (str | None, optional): Element Attribute Value. Defaults to None.
        child_tag_name (str | None, optional): Element Child Tag Name. Defaults to None.
        child_attr (str, optional): Element Child Attribute. Defaults to "aria-label".
        child_attr_value (str | None, optional): Element Child Attribute Value. Defaults to None.

    Returns:
        WebElement: Selenium Web Element
    """
    client.wait.until(
        lambda client: client.execute_script("return document.readyState") == "complete"
    )
    time.sleep(2)
    elements = client.execute_script(
        f"return document.querySelectorAll(\"{tag}[{attr}='{attr_value}']\");"
    )
    for element in elements:
        has_child = client.execute_script(
            f"""
            var element = arguments[0];
            return element.querySelector("{child_tag_name}[{child_attr}=\'{child_attr_value}\']") !== null;
        """,
            element,
        )
        if has_child:
            return element
    return None
