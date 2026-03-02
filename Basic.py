print('Ania')
print('o-----')
print('*' *10)

#variables
price = 10
name = 'Ania'
is_published = True #boolen
print(price*10)


#input
name = input('waht is your name? ')
print('Hi ' + name)

#zadanie
name = input('waht is your name? ')
color = input('what is your favorite color? ')
print(name + ' likes ' + color)

#zadanie
birth_year = input('what is your birth year? ')
print(type(birth_year))
age = 2026 - int(birth_year)
print(type(age))
print(age)

#zadanie z waga
pounds = input('what is your weight in pounds? ')
weight = int(pounds) * 0.4536
print(weight)

#strings

course = 'Python for beginners'
print(course[0:3])

#formatted strings

first_name = 'John'
last_name = 'Doe'
message = first_name + ' is ' + last_name
print(message)

msg = f'{first_name} {last_name}'
print(msg)


course = 'python for beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('n'))
print(course.replace('beginners', 'medium'))
print('python' in course)

#arithmetic operations
x = 10
x = x +3
print(x)

x+=4
print(x)

#operator precedence
import math as m
print(m.ceil(2.333333333333))
x =2.9
print(abs(-3))

#if_statements
is_hot = False
is_cold = False
if is_hot:
    print('hey')
elif is_cold:
    print('how are you?')
else:
    print('no')

#zadanie
x = 1000000
has_good_credit = True
if has_good_credit:
    print(x*0.1)
else:
    print(x*0.2)

#logical operators

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = False
if has_high_income and not has_criminal_record:
    print("Eligible for loan")




