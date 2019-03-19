from com.config import config_json_reader

conf = config_json_reader.setup()

for key in conf:
    print(key,conf[key])