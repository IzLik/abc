from pyexpat import ErrorString
from labels_paints import *

logo()

print('Это тест на IQ! Проверь себя!\n')
try:
    age = int(input('\nСколько вам лет?: '))
except ValueError:
    age = int(input('Необходимо ввести число. Пожалуйста повторите ввод!: '))
c = 0

ques1 = int(input('Какое число не вписывается в этот ряд?\n1) 4\n2) 9\n3) 2\n'))
if ques1 == 2:
    c+=3
ques2 = int(input('Какой цвет не вписывается в этот ряд?\n1) Зеленый\n2) Желтый\n3) Синий\n'))
if ques2 == 2:
    c+=3
ques3 = int(input('Какая страна не вписывается в этот ряд?\n1) Бразилия\n2) Канада\n3) Мексика\n'))
if ques3 == 1:
    c+=3
ques4 = int(input('Какой город лишний?\n1) Варшава\n2) Париж\n3) Иерусалим\n'))
if ques4 == 3:
    c+=3
ques5 = int(input('Какое слово лишнее?\n1) Умный\n2) Смешной\n3) Спящий\n'))
if ques5 == 3:
    c+=3
ques6 = int(input('Какой металл не вписывается в этот ряд?\n1) Серебро\n2) Медь\n3) Золото\n'))
if ques6 == 2:
    c+=3
ques7 = int(input('Какая профессия не вписывается в этот ряд?\n1) Медсестра\n2) Костоправ\n3) Хирург\n'))
if ques7 == 1:
    c+=3
ques8 = int(input('Какая геометрическая фигура не вписывается в этот ряд?\n1) Квадрат\n2) Круг\n3) Треугольник\n'))
if ques8 == 2:
    c+=3
ques9 = int(input('Какое животное не вписывается в этот ряд?\n1) Кенгуру\n2) Коала\n3) Лев\n'))
if ques9 == 3:
    c+=3
ques10 = int(input('Выберите актера, который не вписывается в этот ряд?\n1) Крис Хемсворт\n2) Райан Гослинг\n3) Райан Рейнольдс\n'))
if ques10 == 1:
    c+=3
ques11 = int(input('Кто из гениев не вписывается в этот ряд?\n1) Джон Нэш\n2) Альберт Энштейн\n3) Стивен Хокинг\n'))
if ques11 == 1:
    c+=3
ques12 = int(input('Какой писатель не вписывается в эту последовательность?\n1) Ф. Скотт Фицджеральд\n2) Владимир Набоков\n3) Эрнест Хемингуэй\n'))
if ques12 == 2:
    c+=3
ques13 = int(input('Какой продукт здесь лишний?\n1) Помидоры\n2) Черника\n3) Кале\n'))
if ques13 == 2:
    c+=3
ques14 = int(input('Какой фильм не вписывается в эту последовательность\n1) Титаник\n2) 500 дней лета\n3) Леон\n'))
if ques14 == 2:
    c+=3
ques15 = int(input('Выберите книгу, которая не вписывается в эту последовательность?\n1) Джейн Эйр\n2) Эмма\n3) Гордость и пробуждение\n'))
if ques15 == 2:
    c+=3

all = c / int(age) * 100 

loading()

print('Ваш результат IQ:', round(all, 0))
if all <= 60:
    print('У вас низкий уровень IQ. Вам надо больше заниматься!')
elif all > 60 and all <= 100:
    print('Поздравляю! У вас средний показатель IQ.')
else:
    print('У вас высокий уровень IQ! Гордитесь этим!')
sleep(5)
loading_line()