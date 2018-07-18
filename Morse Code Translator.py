import re

dict= { 'A' : '.-', 
        'B' : '-...',
        'C' : '-.-.',
        'D' : '-..',
        'E' : '.',
        'F' : '..-.',
        'G' : '--.',
        'H' : '....',
        'I' : '..',
        'J' : '.---',
        'K' : '-.-',
        'L' : '.-..',
        'M' : '--',
        'N' : '-.',
        'O' : '---', 
        'P' : '.--.',
        'Q' : '--.-',
        'R' : '.-.',
        'S' : '...',
        'T' : '-',
        'U' : '..-',
        'V' : '...-',
        'W' : '.--',
        'X' : '-..-',
        'Y' : '-.--',
        'Z' : '--..',

        '1' : '.----',
        '2' : '..---',
        '3' : '...--',
        '4' : '....-',
        '5' : '.....',
        '6' : '-....',
        '7' : '--...',
        '8' : '---..',
        '9' : '----.',
        '0' : '-----',

        " " : '/'}

while True:
    while True:
        ans = input("(1) Translate text to Morse Code \n(2) Translate Morse Code to Text \n->")
        if ans in ('1', '2'):
            break
        print ('Invalid input.')
    if ans == '1':
        msg = input("Enter your Message: ")
        txt = re.sub('[^A-Za-z0-9]+', ' ', msg)
        for char in txt:
            print(dict[char.upper()] + " ", end ='')

        while True:
            answer = input('\n\nRun again? (y/n): ')
            if answer in ('y', 'n'):
                break
            print ('Invalid input.')
        if answer == 'y':
            continue
        else:
            print ('Goodbye')
            break
    else:
        txt = input("Enter your Message: ")
        code = txt.split(' ')
        inv_map = {v: k for k, v in dict.items()}
        for char in code:
            print(inv_map[char.upper()], end ='')