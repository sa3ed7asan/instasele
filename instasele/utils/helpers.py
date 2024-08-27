from json import load, dump
from typing import Dict, List
import os


def read(fp: os.PathLike | str) -> Dict | List:
    """Read json file content

    Args:
        fp (os.PathLike | str): file path to be read

    Returns:
        Dict | List: Content File
    """    
    with open(fp, encoding="utf-8") as f:
        data = load(f)
    return data


def write(data: Dict | List, fp: os.PathLike | str) -> None:
    """Write json data in a file

    Args:
        data (Dict | List): json data to be written
        fp (os.PathLike | str): file path to write data in it
    """    
    with open(fp, "w", encoding="utf-8") as f:
        dump(data, f, indent=4, ensure_ascii=False)
