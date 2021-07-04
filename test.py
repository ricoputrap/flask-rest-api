from flask.globals import request
import requests

BASE = "http://127.0.0.1:5000/"

# data = [{ "name": "Cute Cat", "views": 90, "likes": 20 },
#         { "name": "Flask RESTFul Tutorial", "views": 1000, "likes": 570 },
#         { "name": "Cooking Fun!", "views": 30, "likes": 10 }]

# for i in range(len(data)):
#   response = requests.put(BASE + "video/" + str(i), data[i])
#   print(response.json())

# input()
# # # response = requests.delete(BASE + "video/0")
# # print(response)

# input()
# response = requests.get(BASE + "video/6")
# print(response.json())

response = requests.patch(BASE + '/video/2', { "likes": 50 })
print(response.json())