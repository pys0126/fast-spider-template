from logic.base_logic import BaseLogic
from util.fetch_util import Fetch
from requests import Session


class IndexLogic(BaseLogic):
    def __init__(self, fetch_object: Fetch, base_url: str) -> None:
        super().__init__(fetch_object, base_url)
        self.encodeing: str = "GBK"
        self.method: str = "GET"
        self.url: str = "/2h1.php"

    def parse(self) -> None:
        # 可以使用get_session方法获取Session对象，进行自定义请求
        session: Session = self.fetch_object.get_session()
        session.get(url="https://www.baidu.com")