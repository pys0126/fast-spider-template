from util.fetch_util import Fetch
from util.fetch_util import Methods
from requests.adapters import Response

class BaseLogic:
    def __init__(self, fetch_object: Fetch, base_url: str) -> None:
        self.fetch_object: Fetch = fetch_object
        self.base_url: str = base_url
        self.response: Response = Response()
        self.method: str = Methods.GET.value
        self.encodeing: str = "GBK"
        self.url: str = "/"

    def request(self) -> None:
        self.fetch_object.url = self.url if self.url.startswith("http") else self.base_url + self.url        
        self.response = self.fetch_object.request(method=self.method, encodeing=self.encodeing)
        print("已请求：", self.fetch_object.url)

    def parse(self) -> None:
        ...
    
    def start(self) -> None:        
        self.request()
        self.parse()