import requests
import dotenv
import os


def get_inp(day=1):
    url = f"https://adventofcode.com/2023/day/{day}/input"
    dotenv.load_dotenv(".session_cookie")
    resp = requests.get(
        url,
        cookies={"session": os.environ["SESSION"]},
    )
    return resp.text
