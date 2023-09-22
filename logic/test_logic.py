from logic.base_logic import BaseLogic
from util.fetch import Fetch


class TestLogic(BaseLogic):    
    def __init__(self, fetch_object: Fetch, base_url: str) -> None:
        super().__init__(fetch_object, base_url)
        self.url: str = "https://live.500.com/zqdc.php"

    def parse(self) -> None:
        print(self.url, self.response.status_code, end="\n\n")