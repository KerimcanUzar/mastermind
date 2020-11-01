play = True
while play:
    input("I will choose a 4-digit code, with all digits different and you will try to guess.\nFor that you will enter 4-digit code, with all digits different.\nFor every guess I will give you a hint.\nHints will contain two numbers.\nFirst number shows how many correct digits in the correct place.\nE.g.. I choose 1234 and you say 6854, so hint will be 1-0.\nSecond number shows how many correct digit in wrong place.\nE.g.. I choose 1234 and you say 2340, so hint will be 0-3\nWhen you are ready to start, press enter.\n\n")
    import random
    digit1 = random.randint(0,9)
    digit2 = random.randint(0,9)
    while digit2 == digit1:
        digit2 = random.randint(0,9)
    digit3 = random.randint(0,9)
    while digit3 == digit1 or digit3 == digit2:
        digit3 = random.randint(0,9)
    digit4 = random.randint(0,9)
    while digit4 == digit1 or digit4 == digit2 or digit4 == digit3:
        digit4 = random.randint(0,9)
    tries = 0
    correct = 0
    while correct != 4:
        guess = int (input ("Write a 4 digits number.\n\n"))
        if guess < 10000 and guess > 999:
            gdigit1 = guess/1000
            gdigit2 = (guess/100)%10
            gdigit3 = (guess/10)%10
            gdigit4 = guess%10
            gdigit1 = int(gdigit1)
            gdigit2 = int(gdigit2)
            gdigit3 = int(gdigit3)
            gdigit4 = int(gdigit4)

            correct = 0
            wrong = 0

            if digit1 == gdigit1:
                correct = correct+1
            if digit2 == gdigit2:
                correct = correct+1
            if digit3 == gdigit3:
                correct = correct+1
            if digit4 == gdigit4:
                correct = correct+1

            if digit1 == gdigit2 or digit1 == gdigit3 or digit1 == gdigit4:
                wrong = wrong+1
            if digit2 == gdigit1 or digit2 == gdigit3 or digit2 == gdigit4:
                wrong = wrong+1
            if digit3 == gdigit1 or digit3 == gdigit2 or digit3 == gdigit4:
                wrong = wrong+1
            if digit4 == gdigit1 or digit4 == gdigit2 or digit4 == gdigit3:
                wrong = wrong+1

            print (str(correct) + "-" + str(wrong) + "\n")

            tries = tries+1
            print ("Tries: " + str(tries) + "\n")
        else:
            print("\nInput should be a 4 digits number.\n")

    if input ("You won! Do you want to play again? (y/n) \n\n") == "n":
            play = False