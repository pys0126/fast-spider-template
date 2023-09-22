from enum import Enum
from typing import Union
from requests import Session
from requests.adapters import Response
from fake_useragent import UserAgent

# 创建UserAgent对象
user_agent: UserAgent = UserAgent()

class Methods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

class Fetch:
    def __init__(self, url: str, cookie: str = "", payload: dict = {}, referer: str = "") -> None:
        self.url: str = url
        self.payload: dict = payload
        self.headers: dict = {
            "User-Agent": user_agent.chrome,
            "cookie": cookie,
            "Referer": referer if referer else self.url,
            "Content-Type": "application/json; charset=UTF-8"
        }
        self.session: Session = Session()
    
    def request(self, method: str = "GET", encodeing: str = "UTF-8") -> Response:
        method = method.upper()
        if method == Methods.GET.value:
            response: Response = self.session.get(url=self.url, params=self.payload, headers=self.headers)            
        elif method == Methods.POST.value:            
            response: Response = self.session.post(url=self.url, data=self.payload, headers=self.headers)
        elif method == Methods.PUT.value:
            response: Response = self.session.put(url=self.url, data=self.payload, headers=self.headers)
        elif method == Methods.DELETE.value:
            response: Response = self.session.delete(url=self.url, data=self.payload, headers=self.headers)
        else:
            raise ValueError(f"占时不支持的请求方式：{method}")
        response.encoding = encodeing
        return response