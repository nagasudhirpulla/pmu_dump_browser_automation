from typing import TypedDict


class IAppConfig(TypedDict):
    webDriverLocation: str
    loginLocation: str
    username: str
    password: str