# instasele

**instasele** Simple Library To Control Instagram Accounts.

# Library Information
*Author :* [**Al-Saeed Hassan**](https://t.me/DEV_BEN)\
*Library :* [**instasele**](https://github.com/sa3ed7asan/instasele)\
*License:* [**MIT License**](https://github.com/sa3ed7asan/instasele/blob/main/LICENSE)\
*Release:* **28**/08/20**24**\
*Version :* **1.0.0**

If You Have Any Problem [Issues](https://github.com/sa3ed7asan/instasele/issues)

# Featurs:
- Available:
    - Login
    - Save Cookies File
    - Follow a user
    - Like a post
    - Add a comment on a post
- Comming:
    - Send DMs to users
    - Upload posts
    - Save posts
    - View user stories


# Usage

### Login into an `Instagram` account

#### Using credintials
```python
from instasele import Client
username = "account_username"
password = "account_password"
client = Client()
client.login(username, password, save_login=True)
```
`Cookies will be saved in cookies/account_username.json`

#### Using Cookies
```python
from instasele import Client
username = "account_username"
client = Client()
client.login(username, use_cookies=True)
```
*(opptional use_cookies)*.
*(opptional cookies_file)*.
*(opptional headless)*.

### Actions
#### Like
```python
from instasele import Client
username = "account_username"
password = "account_password"
client = Client()
login_response = client.login(username, password)
if response["ok"]:
    post_url = "instagram_post_url"
    client.like(post_url)
```

#### Comment
```python
from instasele import Client
username = "account_username"
password = "account_password"
client = Client()
login_response = client.login(username, password)
if response["ok"]:
    post_url = "instagram_post_url"
    client.comment(post_url, "comment")
```

#### Follow
```python
from instasele import Client
username = "account_username"
password = "account_password"
client = Client()
login_response = client.login(username, password)
if response["ok"]:
    account_url = "instagram_account_url"
    client.follow(account_url)
```

# Installation

**instasele** Available Now On PyPi

```console
python -m pip install instasele
```


**Note:** This is an unofficial library, created and maintained by [**Al-Saeed Hassan**](https://github.com/sa3ed7asan/). It is not supported or endorsed by Instagram.
