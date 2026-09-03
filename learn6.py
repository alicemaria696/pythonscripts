"""login_logs = [
    ("alice", "10.0.0.1"),
    ("bob", "10.0.0.2"),
    ("alice", "10.0.0.3"),
    ("charlie", "10.0.0.1"),
    ("alice", "10.0.0.4"),
    ("bob", "10.0.0.2"),
    ("david", "10.0.0.5"),
    ("alice", "10.0.0.1"),
]

users = {}
for u , ip in login_logs:
    if u in users:
        users[u].add(ip)
    else:
        users[u] = {ip}
for u,ip in users.items():
    #print(u,ip)
    if len(ip)>=2:
        print("the user with more ip blocks are: ", u)
    else:
        print("the other users are: ", u, ip)"""
        

user_roles = [
    ("alice", "reader"),
    ("alice", "admin"),
    ("bob", "reader"),
    ("charlie", "reader"),
    ("charlie", "developer"),
    ("charlie", "admin"),
    ("david", "reader"),
    ("david", "developer"),
    ("eve", "admin"),
]

user = set()
dup = set()
dict = {}
for u,r in user_roles:
    if u in user:
        dup.add(u)
        dict[u].add(r)
    else:
        user.add(u)
        dict[u] = {r}
print("noneduplicate :",user)
print("duplicate :",dup)
print(dict)

for u,r in dict.items():
    if len(r) >2:
        print("The user with different role is :", u,r)
    else:
        print("single users and role are: ", u)
        
        
    
  
    
