author_data = [
    {'username': 'Преподаватель 1'},
    {'username': 'Преподаватель 2'},
    {'username': 'Преподаватель 3'},
    {'username': 'Преподаватель 4'},
]

student_data = [
    {'username': 'Ученик 1'},
    {'username': 'Ученик 2'},
    {'username': 'Ученик 3'},
    {'username': 'Ученик 4'},
    {'username': 'Ученик 5'},
    {'username': 'Ученик 6'},
    {'username': 'Ученик 7'},
    {'username': 'Ученик 8'},
    {'username': 'Ученик 9'},
    {'username': 'Ученик 10'},
    {'username': 'Ученик 11'},
    {'username': 'Ученик 12'},
    {'username': 'Ученик 13'},
    {'username': 'Ученик 14'},
]

product_data = [
    {'name': 'Английский язык', 'price': 2000, 'author_username': 'Преподаватель 1'},
    {'name': 'Французский язык', 'price': 1800, 'author_username': 'Преподаватель 1'},
    {'name': 'Математика', 'price': 2500, 'author_username': 'Преподаватель 2'},
    {'name': 'Физика', 'price': 1500, 'author_username': 'Преподаватель 2'},
    {'name': 'Химия', 'price': 3000, 'author_username': 'Преподаватель 3'},
    {'name': 'Биология', 'price': 2700, 'author_username': 'Преподаватель 3'},
    {'name': 'История', 'price': 1700, 'author_username': 'Преподаватель 4', 'max_number_users_in_group': 6},
]

lesson_data = [
    {'name': 'Английский 1', 'link': 'https://site.com/english1', 'product_name': 'Английский язык'},
    {'name': 'Английский 2', 'link': 'https://site.com/english2', 'product_name': 'Английский язык'},
    {'name': 'Английский 3', 'link': 'https://site.com/english3', 'product_name': 'Английский язык'},
    {'name': 'Английский 4', 'link': 'https://site.com/english4', 'product_name': 'Английский язык'},

    {'name': 'Французский 1', 'link': 'https://site.com/franch1', 'product_name': 'Французский язык'},
    {'name': 'Французский 2', 'link': 'https://site.com/franch2', 'product_name': 'Французский язык'},
    
    {'name': 'Математика 1', 'link': 'https://site.com/math1', 'product_name': 'Математика'},
    {'name': 'Математика 2', 'link': 'https://site.com/math2', 'product_name': 'Математика'},
    {'name': 'Математика 3', 'link': 'https://site.com/math3', 'product_name': 'Математика'},
    {'name': 'Математика 4', 'link': 'https://site.com/math4', 'product_name': 'Математика'},
    {'name': 'Математика 5', 'link': 'https://site.com/math5', 'product_name': 'Математика'},

    {'name': 'Физика 1', 'link': 'https://site.com/physics1', 'product_name': 'Физика'},

    {'name': 'Химия 1', 'link': 'https://site.com/chemistry1', 'product_name': 'Химия'},
    {'name': 'Химия 2', 'link': 'https://site.com/chemistry2', 'product_name': 'Химия'},
    {'name': 'Химия 3', 'link': 'https://site.com/chemistry3', 'product_name': 'Химия'},
    {'name': 'Химия 4', 'link': 'https://site.com/chemistry4', 'product_name': 'Химия'},
    {'name': 'Химия 5', 'link': 'https://site.com/chemistry5', 'product_name': 'Химия'},
    {'name': 'Химия 6', 'link': 'https://site.com/chemistry6', 'product_name': 'Химия'},
    {'name': 'Химия 7', 'link': 'https://site.com/chemistry7', 'product_name': 'Химия'},

    {'name': 'Биология 1', 'link': 'https://site.com/biology1', 'product_name': 'Биология'},
    {'name': 'Биология 2', 'link': 'https://site.com/biology2', 'product_name': 'Биология'},
    {'name': 'Биология 3', 'link': 'https://site.com/biology3', 'product_name': 'Биология'},

    {'name': 'История 1', 'link': 'https://site.com/history1', 'product_name': 'История'},
    {'name': 'История 2', 'link': 'https://site.com/history2', 'product_name': 'История'},
]


'''
Добавление ученика к курсу
1) Если нет групп - создать группу и добавить туда ученика
2) Если есть группа, проверить, достаточно можно ли туда добавить
3) Если нельзя добавить, создать новую. (простое решение)
'''

'''
Добавление ученика к курсу
1) Если нет групп - создать группу и добавить туда ученика
2) Если есть группа, но при этом минимальное количество людей для группы нет, 
   то добавить пользователя в группу
3) Достигнуто минимальное значение людей - создать новую группу и добавить туда ученика
4) Добавлять, пока не заполнится минимум
5) Добавить в другую группу, а потом в ту же, пока не достигнется число равное
'''