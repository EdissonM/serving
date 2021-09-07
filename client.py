import requests
import ast

url = "http://0.0.0.0:80/"
myobj = {"x": 2, "y": 2}

respuesta = requests.post(url, json=myobj)

print(ast.literal_eval(respuesta.text))

