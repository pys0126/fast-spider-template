from util.fetch import Fetch
from threading import Thread
from logic.test_logic import TestLogic
from logic.index_logic import IndexLogic
from config.fetch_config import FetchConfig

class BaseService:
    def __init__(self) -> None:
        self.base_url = FetchConfig.BASE_URL[:-1] if FetchConfig.BASE_URL.endswith("/") else FetchConfig.BASE_URL
        self.fetch: Fetch = Fetch(url=self.base_url, cookie=FetchConfig.COOKIE)
        self.logic_tasks: list = [
            IndexLogic(fetch_object=self.fetch, base_url=self.base_url),
            TestLogic(fetch_object=self.fetch, base_url=self.base_url)
        ]
    
    def start(self) -> None:
        tasks: list = []
        for logic_task in self.logic_tasks:
            tasks.append(Thread(target=logic_task.start, args=()))
        for task in tasks:
            task.start()
        for task in tasks:
            task.join()            