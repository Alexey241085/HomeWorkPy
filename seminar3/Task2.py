eng = 'qwertyuiopasdfghjklzxcvbnm'
rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

word = input('Введите слово на русском или английском языке: ')

if word[0].lower() in eng:
    summa = 0
    for letter in word:
        for key, value in list_English.items():
            if letter.upper() in value:
                summa += key
    print(f'стоимость введенного английского слова = {summa}')
else:
    if word[0].lower() in rus:
        summa = 0
        for letter in word:

            for key, value in list_Russian.items():
                if letter.upper() in value:
                    summa += key
    print(f'стоимость введенного русского слова = {summa}')