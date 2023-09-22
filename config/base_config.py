import os
import json
from typing import Any

# 读取Json配置
json_path: str = os.path.join(os.getcwd(), "config.json")
if not os.path.exists(json_path):
    raise FileExistsError("config.json配置文件不存在，请确保在项目根目录下")
with open(file=json_path, mode="r", encoding="u8") as f:
    json_data: str = f.read()
json_config: dict = json.loads(json_data)

# 获取FetchConfig
fetch_config: Any = json_config.get("FetchConfig")

