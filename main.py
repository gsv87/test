a = input('Введите искомое слово: ')
with open(file='file.txt', mode='r', encoding='UTF-8') as f:
    print(f.read().count(a))

print('hello')
print('added in another')

print('Меня создали на GitHub')
