# Tech Check #6
# Name..: Cristina Ponay
# ID....: W0424195

__AUTHOR__ = "Cristina Ponay <w0424195@nscc.ca>"

def main():
    try:
        myfile = open("readthis.csv")
    except FileNotFoundError:
        print("File readthis.csv does not exist")
    else:
        damageList = []
        msgList = []
        for line in myfile:
            line = line.replace("\n", "")
            lineList = line.split(",")
            damageList.append(int(lineList[-1]))
            msgList.append(lineList[0:2])
        print("Welcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.")
        quitnow = input("Hit any key to continue ('Q' or 'q' to quit): ").lower()
        
        while quitnow != 'q':
            while True:
                try:
                    hit = int(input("\nPlease enter your initial hit points (1-200): "))
                except ValueError:
                    print("You do not listen very well do you? Think you are going to survive this dungeon?")
                else:
                    if not hit in range(1,201):
                         print("You do not listen very well do you? Think you are going to survive this dungeon?")
                    else:
                        break
            

            while hit != 0:
                for i in range(len(msgList)):
                    hit -= damageList[i]
                    msg = f"You were attacked by a {msgList[i][0]} with a {msgList[i][1]} attack for {damageList[i]} damage. "
                    if hit < 1:
                        hit = 0
                        msg += f"Current hit points: {hit}"
                        print(msg)
                        print("That was sad. And brief. At least the elf feels better about himself!!!\n")
                        break
                    msg += f"Current hit points: {hit}"
                    print(msg)

            print("Welcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.")  
            quitnow = input("Hit any key to continue ('Q' or 'q' to quit): ").lower()
            if quitnow == 'q':
                print("That's it. Reatreat in fear and warn your friends!")
    finally:
        myfile.close()

if __name__ == "__main__":
    main()