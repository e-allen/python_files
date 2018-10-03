rock = []
pop = []


def collect_songs():
    song = "Enter a song."
    ask = "Type r or p. q to quit"


    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)


        elif genre == ("p"):
            pp = input(song)
            pop.append(pp)


        else:
            print("Invalid.")
        print(rock)
        print(pop)

        
