import requests
import json
import datetime
import pytz
import os
from dotenv import load_dotenv
load_dotenv(override=True)
from github_row import *

BASE_URL = "https://qiita.com/api/v2/items"

def putQiitaArticle(title, markdown, path="article", id=""):
    token = os.environ["ACCESS_TOKEN"]
    headers = {"Authorization": f"Bearer {token}"}
    item = {
        "title": title,
        "id": id,
        "tags": [
            {
            "name": "アクセルキャンプ"
            },
            {
            "name": "roblox"
            },
            {
            "name": "Lua"
            },
            {
            "name": "小学生向け"
            },
            {
            "name": "中学生"
            },

        ],
        "private": False,
        "coediting": False,
        "tweet": False,
        "body": markdown
    }
    # idがなければ、新規で記事を投稿
    if item["id"] == "":
        res = requests.post(BASE_URL, headers=headers, json=item)
        return res
    else:
        now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        item["title"] += now.strftime("【%Y/%m/%d %H時更新】")
        item_id = item["id"]
        res = requests.patch(BASE_URL + f"/{item_id}", headers=headers, json=item)
        return res

if __name__ == "__main__":
    with open("./article/post.md", encoding="utf-8") as f:
        lines = f.readlines()
    markdown = "".join(lines)
    markdown = replace_images_by_filename(markdown)
    res = putQiitaArticle(lines[6][2:-1], markdown,"article", "").json()
    print(res)
