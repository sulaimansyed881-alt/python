farm={
    "Hose":2,
    "Barn":1,
    "Tractor":5,
    "Sheep":20,
}
print(farm)
for i in farm:
    print(i,farm[i])
print(farm.get("Hose"))
print(farm["Tractor"])
farm["Sheep"]=70
print(farm)


