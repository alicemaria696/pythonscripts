login_logs = [
    ("alice", "success", "10.0.0.1"),
    ("alice", "failed", "10.0.0.2"),
    ("alice", "failed", "10.0.0.2"),
    ("bob", "failed", "10.0.0.3"),
    ("bob", "success", "10.0.0.3"),
    ("charlie", "failed", "10.0.0.4"),
    ("charlie", "failed", "10.0.0.5"),
    ("charlie", "failed", "10.0.0.6"),
    ("david", "success", "10.0.0.7"),
]

user = {}
for u,s, ip in login_logs:
    if u in user:
        user[u][s].add(ip)
        
    else:
        user[u] = {
    "failed": set({ip}),
    "success": set({ip})
}
print("user:", user)

        
for u, s in user.items():
    old_ip = s["failed"]
    new_ip = s["success"]

    #print(u, old_ip, new_ip)
    if len(old_ip) >=3 or old_ip != new_ip:
        print(u)
   
