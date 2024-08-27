from instasele import Client

client = Client()
username = "_tezy_13_6"
post_url = "instagram_post_url"

login_response = client.login(username, use_cookies=True)
if login_response["ok"]:
    client.like(post_url)
    client.comment(post_url, "Very Well !")
    client.follow("instagram_account_url")

client.close()

# sarahalhosiny
