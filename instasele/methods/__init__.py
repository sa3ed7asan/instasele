from .login import Login
from .actions import Like, Comment, Follow


class Methods(Login, Like, Comment, Follow):
    pass
