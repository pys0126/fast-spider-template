from enum import Enum
from requests import Session
from fake_useragent import UserAgent
from requests.adapters import Response
from util.string_util import string_to_cookie_dict

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
            "Referer": referer if referer else self.url,
            "Content-Type": "application/json; charset=UTF-8"
        }
        self.cookie: dict = string_to_cookie_dict(text=cookie)
        self.session: Session = Session()
    
    def request(self, method: str = "GET", encodeing: str = "UTF-8") -> Response:
        method = method.upper()
        if method == Methods.GET.value:
            response: Response = self.session.get(url=self.url, params=self.payload, headers=self.headers, cookies=self.cookie)            
        elif method == Methods.POST.value:            
            response: Response = self.session.post(url=self.url, data=self.payload, headers=self.headers, cookies=self.cookie)
        elif method == Methods.PUT.value:
            response: Response = self.session.put(url=self.url, data=self.payload, headers=self.headers, cookies=self.cookie)
        elif method == Methods.DELETE.value:
            response: Response = self.session.delete(url=self.url, data=self.payload, headers=self.headers, cookies=self.cookie)
        else:
            raise ValueError(f"不支持的请求方式：{method}")
        response.encoding = encodeing
        return response

    def get_session(self) -> Session:
        return self.session