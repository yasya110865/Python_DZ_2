
person = ['Пушкин', 'Челентано', 'Чехов', 'Пастер', 'Флеминг']
years = [1799, 1938, 1860, 1822, 1881]
next_game = 'да'
while next_game == 'да':
    right = 0
    wrong = 0
    for i in range(len(person)):
        answer = int(input('В каком году родился ' + person[i] + '? ' ))
        if answer == years[i]:
            right += 1
        else:
            wrong += 1
    print('Правильных ответов - ', right * 100/ (right + wrong), '%')
    next_game = input('Хотите повторить? ')
