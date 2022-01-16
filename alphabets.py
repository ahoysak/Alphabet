import json

def eng_alf():
    file = open('englishalphabet.json', 'r')
    alphabett = json.loads(file.read())
    file.close()
    print('Англійський алфавіт: ', alphabett)

def eng_lens():
    file = open('englishalphabet.json', 'r')
    alphabett = json.loads(file.read())
    file.close()
    lensofalphabet = len(alphabett)
    print("Кількість букв в англійському алфавіті: ", lensofalphabet)

def check_letter():
    file = open('englishalphabet.json', 'r')
    alphabett = json.loads(file.read())
    letter = input('You must write letter\n'
                   + 'Write a CAPITAL letter:')
    if letter in alphabett:
        print('the letter belongs to the alphabet!')
    else:
        print('Not the correct letter')#не належить

def english_text():
    print("It's just English text.\n"
          +"Don't take it seriously.")

def ukr_alf():
        file = open('ukralphabet.json', 'r')
        alphabett = json.loads(file.read())
        file.close()
        print('Український алфавіт: ', alphabett)

def ukr_lens():
    file = open('ukralphabet.json', 'r')
    alphabett = json.loads(file.read())
    file.close()
    lenukr = len(alphabett)
    print("Кількість букв в українському алфавіті: ", lenukr)