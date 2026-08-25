import csv

user_roles = [
    ("alice", "admin"),
    ("bob", "reader"),
    ("alice", "admin"),
    ("charlie", "reader"),
    ("bob", "reader"),
    ("david", "admin")
]



seen = set()
dup = set()
for i in user_roles:
    if i in seen:
        dup.add(i)
        print("duplicate", i)
    else:
       seen.add(i)
       print("no duplication",seen)
with open("duplicate.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(dup)
    writer.writerow(seen)


    
        
        
        