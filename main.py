from alphabets import *

print('Select language')
while True:
    print('1. English alphabet\n'
           + '2. Ukrainian alphabet')

    select_choose = int(input('Select a language: ')) #вибір команди
    if select_choose == 1:
        print('Choose an action with the English alphabet: \n'
               + '1. Number of letters\n' #кількість букв
               + '2. Check letter\n'      #перевірити чи до англ алфавіту належить
               + '3. Example text in English ')  #приклад англ мовою
        next_select_choose = int(input('Your choose: '))
        if next_select_choose == 1:
            eng_lens()
        elif next_select_choose == 2:
            check_letter()
        elif next_select_choose == 3:
            english_text()

    elif select_choose == 2:
        print('Ви вибрали Українську мову!\n'
              + '1.Подивитись алфавіт.\n'
              + '2.Подивитись кількість букв алфавіту.')
        next_urk_choose = int(input("Виберіть дію,яку хочете зробити: "))
        if next_urk_choose == 1:
            ukr_alf()
        elif next_urk_choose == 2:
            ukr_lens()


