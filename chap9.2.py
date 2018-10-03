x = input("What is your dog's name?")

with open("dog_name.txt", "w") as f:
    f.write(x)
