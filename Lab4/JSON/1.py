import json

x = open('sample-data.json')
data = json.load(x)

print("Interface Status")
print("="*80)
print("DN" + " "*45 + "Description" + " "*11 + "Speed" + " "*4 + "MTU" )
print("-"*46 + " " + "-"*20 + "  " + "-"*6 + "  " + "-"*6)
cnt = 0
for i in data["imdata"]:
    if cnt == 18:
        break
    s = i["l1PhysIf"]["attributes"]["dn"]
    if len(s) == 41:
        print(i["l1PhysIf"]["attributes"]["dn"] + " "*6 + i["l1PhysIf"]["attributes"]["descr"] + " "*21 + i["l1PhysIf"]["attributes"]["speed"] + " "*3 + i["l1PhysIf"]["attributes"]["mtu"])
    else:
        print(i["l1PhysIf"]["attributes"]["dn"] + " "*5 + i["l1PhysIf"]["attributes"]["descr"] + " "*21 + i["l1PhysIf"]["attributes"]["speed"] + " "*3 + i["l1PhysIf"]["attributes"]["mtu"])
    cnt+=1
    
    