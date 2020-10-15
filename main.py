import json

link = input("input link: ")
date_class_name = input("data class name: ")
#to_json = json.dump({"link": link,"date_class_name": date_class_name})


with open(r"simple_fles/json_transfer.json", "r+") as js:
    json.dump({"link": link,"date_class_name": date_class_name}, js)
    

with open(r"simple_fles/json_transfer.json", "r+") as js:
    data = json.load(js)
    print(data)

