erin = dict({"name": "Erin Allen",
             "height": "5'11",
             "eye color": "blue/green",
             "fave author": "Colleen Hoover",
             "fave color": "purple"})
             

n = input("Choose a key:")
if n in erin:
    erin_key = erin[n]
    print(erin_key)
else:
    print("Not Found.")

