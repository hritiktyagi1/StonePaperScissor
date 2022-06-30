import random
option=['stone','paper','scissor']
game=True
while game:
    cpu=random.choice(option)
    user=input("enter your choice:")
    print("cpu:",cpu)
    if cpu==user:
        print("match tie")
    elif cpu=="stone"and user=="scissor":
        print("cpu win")
    elif cpu=="paper"and user=="stone":
        print("cpu win")
    elif cpu=="scissor"and user=="paper":
        print("cpu win")

    elif cpu=="stone"and user=="paper":
        print("you win")
    elif cpu=="paper"and user=="scissor":
        print("you win")
    elif cpu=="scissor"and user=="stone":
        print("you win")









