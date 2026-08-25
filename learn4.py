import pandas as pd
import csv

user_roles = {
    "alice": ["reader", "developer"],
    "bob": ["reader"],
    "charlie": ["admin", "reader"],
    "david": ["developer"],
    "eve": ["admin", "developer"]
}

dict = []

with open("extra_roles.csv", "w") as file:
    writer = csv.writer(file)
    for k,v in user_roles.items():
        if "admin" in v and len(v) > 1:
            dict = [k,v]
            print("Extra Access are", dict)
            writer.writerow(dict)



        
  