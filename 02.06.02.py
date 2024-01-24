import collections

pets = {}# пустая база данных

def create():
    last = collections.deque (pets, maxlen=1) [0]
    global namePet, typePet, agePet, ownerName
    print('Пожалуйста, введите имя питомца')
    namePet = input()
    print('Пожалуйста, введите вид питомца')
    typePet = input()
    print('Пожалуйста, введите возраст питомца')
    agePet = int(input())
    print('Пожалуйста, введите имя хозяина')
    ownerName = input()
    zz = {namePet: {'вид питомца': typePet, 'возраст питомца': agePet, 'имя владельца':  ownerName}} 
    pets[1] = zz
    print(f'Информация про вашего питомца внесена в нашу базу данных. Она имеет свой идентификационный номер: {last}')


def read():
    print('Укажите идентификационный номер вашего питомца')
    k1 = int(input())
    pets[k1]
    print('Это', pets[k1][namePet]['вид питомца'], 'по кличке "', *pets[k1], '". Возраст питомца:', pets[k1][namePet]['возраст питомца'], 'лет. Имя владельца:', pets[k1][namePet]['имя владельца'] )
   
def update():
    print('Укажите идентификационный номер вашего питомца, информацию которого вы хотите обновить')
    k1 = int(input())
    global namePet, typePet, agePet, ownerName
    print('Пожалуйста, введите имя питомца')
    namePet = input()
    print('Пожалуйста, введите вид питомца')
    typePet = input()
    print('Пожалуйста, введите возраст питомца')
    agePet = int(input())
    print('Пожалуйста, введите имя хозяина')
    ownerName = input()
    pets[k1] = {namePet: {'вид питомца': typePet, 'возраст питомца': agePet, 'имя владельца':  ownerName}} 
    
def delete():
    print('Укажите идентификационный номер вашего питомца, информацию которого вы хотите обновить')
    k1 = int(input())
    pets.pop(k1)
    
create()
create()
read()
read()
update()
delete()
reade()
    