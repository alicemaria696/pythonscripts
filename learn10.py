"""def numbers(a,b):
    sum = a + b
    print("Sum :", sum)
    sub = a - b
    print("Sub :", sub)
    return a * b

result = numbers(6, 5)
print("Multiply :", result)"""


"""def numbers():
    a = int(input("enter the number"))
    b = int(input("enter another number"))
    sum  = a + b
    yield sum
    mul = a * b
    yield mul 
    
result = numbers()
print(next(result))
print(next(result))"""



"""access = [
    ("alice", "reader"),
    ("bob", "admin"),
    ("alice", "admin"),
    ("charlie", "reader"),
    ("bob", "reader"),
    ("david", "reader"),
    ("charlie", "developer"),
    ("alice", "reader"),
    ("bob", "admin"),
]

user = set()
dup = {}

for u,r in access:
    if u in user:
        dup[u].add(r)
        
    else:
        user.add(u)
        dup[u] = {r}
print("user :", user)
print("duplicate :", dup)

for u , r in dup.items():
    if "admin" in r and "reader" in r:
        print("User with admin and reader roles :", u)
    else:
        print("user without reader and admin roles: ", u)"""
        
"""login_logs = [
    ("alice", "10.0.0.1"),
    ("bob", "10.0.0.2"),
    ("alice", "10.0.0.2"),
    ("charlie", "10.0.0.3"),
    ("bob", "10.0.0.2"),
    ("alice", "10.0.0.3"),
    ("charlie", "10.0.0.4"),
    ("david", "10.0.0.5"),
    ("alice", "10.0.0.1"),
]

user = {}

for u, ip in login_logs:
    if u in user:
        user[u].add(ip)
    else:
        user[u] = {ip}
    
print(user)

for u,ip in user.items():
    if len(ip) >= 3:
        print("User with 3 or more logins with different ip addresses is :", u,ip, len(ip))
    else:
        print("none")"""
        
role_changes = [
    ("alice", "reader", "developer"),
    ("bob", "reader", "admin"),
    ("alice", "developer", "admin"),
    ("charlie", "reader", "developer"),
    ("bob", "admin", "admin"),
    ("david", "reader", "reader"),
    ("charlie", "developer", "admin"),
    ("alice", "admin", "reader"),
]

user_role = {}

"""for u, old_role, new_role in role_changes:
    if u in user_role:
        user_role[u][0].add(old_role)
        user_role[u][1].add(new_role)
    else:
        user_role[u] = ({old_role}, {new_role})
print("User and Role list :", user_role)

for u,(o,n) in user_role.items():
    if "admin" in n and o:
        print("User with admin access :", u)
    else:
        print("User with no admin access :", u)"""
        
        
"""you meant like this:
for u, o, r in role_changes:
if u in user_role:
user_role[u][0].add(r)
else:
user_role[u] = ({o}, {r})
print("User and Role list :", user_role)
for u, (o,r) in user_role.items():
if "admin" in o and r:
print("user with role as admin :", u)"""
        
for u, o, r in role_changes:
    if u in user_role:
        user_role[u].add(r)
    else:
        user_role[u] = ({r})
print("User and Role list :", user_role)

for u, r in user_role.items():
    if "admin" in r:
        print("user with admin role :", u)
    else:
        print("user with no admin role :", u)



        
        


     