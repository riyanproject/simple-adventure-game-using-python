name=input("enter your name:")
print("welcome",name,"to this adventure")

answer=input("you are on dirt road,it has come to an end and you can go left or right.which way would u like to go? ").lower()

if answer=="left":
    answer=input("you come to a river,u can walk around it swim across it?type walk to walk around it and swim to swim across it:")

    if answer=="swim":
        print("u swim across and eaten by a aligator")
    elif answer=="walk":
        print("u walked for many miles and ran out of water,you lose.")
    else:
        print("not a valid option.u lose")


elif answer=="right":
    answer=input("you have come to a bridge,it looks wobbly,do u want to cross it or head back?(cross/back)")
    if answer=="back":
        print("you go back to the main road")
    elif answer=="cross":
        answer=input("you've crossed the bridge and meet a stranger.do u want to talk to them.(yes,no)")
        if answer=="yes":
            print("you talked to the stranger and they gave you gold,you win!!!")

        elif answer=="no":
            print("you ignored the stranger and they are angry u lose!!")

        else:
            print("not a valid option.u lose")
else:
    print("not a valid option.u lose.")


print("thank u for  trying",name)
