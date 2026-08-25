import csv 
active_users = ["alice", "bob", "charlie", "david", "eve"]

users_with_access = ["alice", "charlie", "eve", "frank"]

inactive = []

for u in users_with_access:
    if u in active_users:
        print("Active List: ", u)
    else:
        print("Inactive users list: ", u)
        inactive.append(u)
print('List is: ', inactive)
with open("inactive_users.csv", "w") as file:
    writer = csv.writer(file)
    for inu in inactive:
        writer.writerow([inu])

        
    
        