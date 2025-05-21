import json
data = [{
            "name": "john",   
            "age": 32,
            "city": "Newyorkcity"
        }]
with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    present_data = json.load(file)
    print(present_data)
