"""login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("david", "failed"),
    ("david", "failed"),
    ("eve", "success"),
]
fcount = {}

for u,r in login_attempts:
    if r == "failed":
        if u in fcount:
            fcount[u] = fcount[u] + 1
        else:
            fcount[u] = 1
for u, c in fcount.items():
    if c >= 3:
        print(u, c)"""
        
        
"""login_attempts = [
    ("alice", "failed"),
    ("bob", "success"),
    ("alice", "failed"),
    ("charlie", "failed"),
    ("alice", "failed"),
    ("bob", "failed"),
    ("charlie", "failed"),
    ("david", "success"),
    ("bob", "failed"),
]

fcount = []
        
for u,r in login_attempts:
    if r == "failed":
        #print(u)
        fcount.append(u)
print(fcount)"""


access_logs = [
    ("alice", "reader"),
    ("bob", "reader"),
    ("alice", "admin"),
    ("charlie", "reader"),
    ("bob", "developer"),
    ("alice", "admin"),
    ("david", "reader"),
    ("bob", "admin"),
]

users = []
count = set()
dup = set()
for u,r in access_logs:
    if r in users:
        print("none")
    else:
        users.append(u)
print(users)

for c in users:
    if c in count:
        dup.add(c)
    else:
        count.add(c)
print("Nonduplicate role users are", count)
print("duplicate role users are", dup)

        
        





        




        

        
    

            


        
    