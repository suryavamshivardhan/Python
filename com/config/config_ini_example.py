from com.config import config_ini_reader

conf = config_ini_reader.setup()

print(conf['DEFAULT']['Compression'])

for key in conf:
    print(key,conf[key])