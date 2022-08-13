# 取得した動画情報軍をnotion APIを利用してnotion dbへ格納する
#

import requests


def insert_into_db(token, id, notion_properties):

    url = "https://api.notion.com/v1/pages"
    payload = {"parent": {"database_id": id}, "properties": notion_properties}
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
