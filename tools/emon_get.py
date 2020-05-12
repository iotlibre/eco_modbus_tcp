#! /usr/bin/python
import urllib.request
import time

cms_ip = "37.187.121.169"
path = '/emoncms'
key = '248ddc1cd611f143a0a0591112bb62af'
node_name = 'pruebatx'
register = 'fr_map'
value = 33

url = "http://{0}{1}/input/post.json".format(cms_ip,path)
string_node_name = "?node={0}".format(node_name)
string_name_value = "&json={0}:{1}".format(register,value)
key_write = "&apikey={0}".format(key)

full_url = url + string_node_name + string_name_value + key_write
print(full_url)
response = urllib.request.urlopen(full_url)
web_page=response.read()
print(web_page)
