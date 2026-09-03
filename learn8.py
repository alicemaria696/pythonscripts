"""login_logs = [
    ("alice", "10.0.0.1", "success"),
    ("bob", "10.0.0.2", "failed"),
    ("alice", "10.0.0.1", "failed"),
    ("alice", "10.0.0.5", "success"),
    ("bob", "10.0.0.2", "failed"),
    ("charlie", "10.0.0.3", "failed"),
    ("bob", "10.0.0.8", "failed"),
    ("alice", "10.0.0.5", "failed"),
]


dup = {}

for u,ip,s in login_logs:
    if u in dup:
        dup[u][0].add(ip)
        dup[u][1].add(s)
    else:
        dup[u] = ({ip},{s})
    
print("duplicate users with more than 1 ip address with status failed:",dup)

for u, (ips ,ss) in dup.items():
    if len(ips) > 1 and "failed" in ss:
        print(u)
    else:
        print("none")"""
        
role_changes = [
    ("alice", "reader", "admin"),
    ("bob", "reader", "developer"),
    ("alice", "admin", "admin"),
    ("charlie", "reader", "admin"),
    ("bob", "developer", "admin"),
    ("david", "reader", "reader"),
    ("alice", "admin", "developer"),
]

role = {}

for u,o,n in role_changes:
    if u in role:
        role[u][0].add(o)
        role[u][1].add(n)
    else:
        role[u] = ({o},{n})
print("The users with admin as role are :", role)

for r, (old,new) in role.items():
    if "admin" in new and old != new:
        print("upgrade admin role :",r)
    else:
        print("none")

        
        