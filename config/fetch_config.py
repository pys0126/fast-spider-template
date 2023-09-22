from config.base_config import fetch_config

class FetchConfig:
    BASE_URL: str = fetch_config.get("BASE_URL")
    COOKIE: str = fetch_config.get("COOKIE")