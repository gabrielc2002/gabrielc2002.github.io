import time
def chucke():
    print("Humphrey(you), is being taken to chuckecheese by your mom ashley, you arrive")
    time.sleep(3)
    print("Ashley wants to buy some food, she buys pizza wings, mojos, and drinks")
    time.sleep(2)
    print("Ashley says Which do you want to eat humphrey? Pizza or wings.")
    time.sleep(4)
    choice=raw_input('Humphrey thinks carefully knowing he is at Chuckecheese, (pizza/wings)')
    while choice !='pizza' and choice !='wings':
        choice=raw_input('Invalid Answer. Try again(pizza/wings)')
    if choice == 'pizza':
        print('he obtains food poisoning and his tastebuds are ravaged, he dies a very painful death from Chuckecheese pizza')
        return
    if choice == 'wings':
        time.sleep(2)
        print('Your mom is letting you go play games!!')
    choice=raw_input('You can play basketball, or go to the play area, (ball/area)')
    while choice !='ball' and choice !='area':
        choice=raw_input('Invalid Answer. Try again(ball/area)')
    if choice == 'ball':
        print('You are shooting hoops and going ham, you get 1000 tickets, you are attracting attention.')
        time.sleep(5)
        print('Keesha the  worker comes, and says stop playing basketball you are winning to many tickets')
        choice=raw_input('He thinks, (stop/ignore)')
        while choice !='stop' and choice !='ignore':
            choice=raw_input('Invalid Answer. Try again(stop/ignore)')
        if choice == 'ignore':
            print ('Keesha kicks you and you die because you are fragile')
            return
        if choice == 'stop':
            print('you want to play terminator, but chucke and his band is playing so you go see him')
            time.sleep(3)
        choice=raw_input('They are animatronics, but still entertaining, but is it worth it to pay attention? (ignore/giveattention)')
        while choice !='ignore' and choice !='giveattention':
            choice=raw_input('Invalid Answer. Try again(ignore/giveattention)')
        if choice == 'giveattention':
            time.sleep(8)
            print('Humphrey dies of a heart attack because the animatronics are scary')
            return
        if choice == 'area':
            print('you live another day, now go pick out a prize from the prize section')
            time.sleep(5)
            print('Daquan says The prize section has lots of things. You have 1000 tickets from the basketball.')
            time.sleep(4)
        choice=raw_input('You can choose between 1000 army men, and 1 premium nerf gun, (men/gun)')
        while choice !='men' and choice !='gun':
            choice=raw_input('Invalid Answer. Try again(man/gun)')
        if choice == 'men':
            time.sleep(3)
            print('Not enough space, your mom beats you and you die')
            return
        else: #you chose gun
            print('You get to shoot your sibling at home, you survived congrats.')
            return
    else: #you chose area
        print('you go to the play area and meet 2 kids named jonnhy and jill')
        time.sleep(6)
        print('they begin to bully humphrey and demand his tokens, humphrey becomes enraged')
    choice=raw_input('give them tokens or defend yourself?(Give/Defend)')
    while choice !='Give' and choice !='Defend':
        choice=raw_input('Invalid Answer. Try again(Give/Defend)')
    if choice == 'Give':
        time.sleep(3)
        print('Your mom disgraces you and you commit suicide, you dishonor family.')
        return
    else : #you chose Defend
        time.sleep(5)
        print('Their Dad (John) comes with all his friends and yells at you and is tempted to beat you up')
    choice=raw_input('Do you try to beat him and his friends up? Or run. (beat/run)')
    while choice !='beat' and choice !='run':
        choice=raw_input('Invalid Answer. Try again(beat/run)') 
    if choice == 'beat':
        time.sleep(3)
        print('You yell BONZAI He grabs you, his fat friend, buff friend and creepy friend all jump you, youre 4 you cant beat up 4 guys')
        time.sleep(3)
        for friend in ['fat', 'buff', 'creepy']: 
            print('The '+friend+' shoots you')
            time.sleep(3)
        return
    if choice == 'run':
        time.sleep(4)
        print('You hide back in the play area, and he follows you, and since adults are not allowed in the play area, he is forced to eat the pizza.')
        time.sleep(6)
        print('The Worker comes and sees you are causing chaos, she tells you to get out.')
    choice=raw_input('Do you get out or ignore her? (out/stay)')
    while choice !='out' and choice !='stay':
        choice=raw_input('Invalid Answer. Try again(out/stay)')
    if choice == 'stay':
        time.sleep(3)
        print('she sends chucke and he eats you alive')
        return
    else : #you chose out
        time.sleep(4)
        print('she tells you to go get a prize then leave')
        time.sleep(4)
        print('Daquan says The prize section has lots of things. You have 1000 tickets from john and jill.')
        time.sleep(4)
        choice=raw_input('You can choose between 1000 army men, and 1 premium nerf gun, (men/gun)')
        while choice !='men' and choice !='gun':
            choice=raw_input('Invalid Answer. Try again(man/gun)')
        if choice == 'men':
            time.sleep(3)
            print('Not enough space, your mom beats you and you die')
            return
        else: #you chose gun
            time.sleep(3)
            print('You also get to shoot your sibling at home, you survived congrats.')
        return