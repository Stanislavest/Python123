# 17.03.2022

# from jinja2 import Template
# per = {'name': 'Игорь', 'age': 28}
#
# # tm = Template("Привет {{ p.name.upper() }}. Мне {{ p.age*2 }} лет.")
# tm = Template("Привет {{ p['name'].upper() }}. Мне {{ p['age']*2 }} лет.")
# msg = tm.render(p=per)
#
# print(msg)

# ==================================================================
# from jinja2 import Template
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person('Игорь', 28)
# tm = Template("Привет {{ p.get_name().upper() }}. Мне {{ p.get_age()*2 }} лет.")
# msg = tm.render(p=per)
# print(msg)

# ==================================================================
# from jinja2 import Template
#
# data = """Модуль Jinja вместо
# определения {{ name }}
# подставит соответствующее значение
# """
#
# tm = Template(data)
# msg = tm.render(name="Игорь")
# print(msg)

# ==================================================================
# from jinja2 import Template
#
# link = "<a href='#'>Ссылка</a>"
#
# tm = Template("{{ link | e }}")
# msg = tm.render(link=link)
# print(msg)

# ==================================================================
# from jinja2 import Template
#
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Житомир'},
#     {'id': 5, 'city': 'Ярославль'}
# ]
#
# link = '''<select name="cities">
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value="{{ c['id'] }}">{{ c['city'] }}</option>
# {% elif c.city == "Москва" -%}
#     <option>{{ c['city'] }}</option>
# {% else -%}
#     {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>'''
# # "-" убирает перенос
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# ==================================================== HOME WORK ===
# from jinja2 import Template
#
# menu=[
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'},
# ]
#
# link="""<ul>
# <li><a href="/index" class="active">Глвная</a></li>
# {% for m in menu[1:]-%}
#     <li><a href="{{ m['href'] }}">{{ m['link'] }}</a></li>
# {% endfor -%}
# </ul>
# """
#
# tm=Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)

# ==================================================================
# from jinja2 import Template

# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
#
# tpl="Суммарная цена автомобилей {{ sc | sum(attribute='price')}}"
#
# tm=Template(tpl)
# msg = tm.render(sc=cars)
#
# print(msg)

# ==================================================================
# from jinja2 import Template
#
# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
# lst=[1, 2, 3, 4, 5, 6]
#
# tpl="Суммарная цена автомобилей {{ sc | sum()}}"
#
# tm=Template(tpl)
# msg = tm.render(sc=lst)

# print(msg)

# ==================================================================
# from jinja2 import Template
#
# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
# # lst=[1, 2, 3, 4, 5, 6]
#
# tpl="Суммарная цена автомобилей {{ (sc | min(attribute='price')).model}}"
#
# tm=Template(tpl)
# msg = tm.render(sc=cars)
# print(msg)

# ==================================================================
# from jinja2 import Template
#
# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
# # lst=[1, 2, 3, 4, 5, 6]
#
# tpl="Суммарная цена автомобилей {{ sc | random}}" # случаный выбор
#
# tm=Template(tpl)
# msg = tm.render(sc=cars)
# print(msg)

# from jinja2 import Template
#
# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
# # lst=[1, 2, 3, 4, 5, 6]
#
# tpl="Суммарная цена автомобилей {{ sc | replace('model', 'brand') }}"
#
# tm=Template(tpl)
# msg = tm.render(sc=cars)
# print(msg)

# ============================== 22.03.2022
# from jinja2 import Template
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0},
# ]
# # {% filter upper %}{{ u.name }}{% endfilter %}
# tpl = """
# {%- for u in users -%}
# {# {% filter upper %}{{ u.name }}{% endfilter %} #}
# {% filter string %}{{ u.year }} - {{ u.weight }}{% endfilter %}
# {% endfor %}
# """
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
# print(msg)

# =================================================== macro-определение
# from jinja2 import Template
#
# # persons = [
# #     {"name": "Алексей", "year": 18, "weight": 78.5},
# #     {"name": "Никита", "year": 28, "weight": 82.3},
# #     {"name": "Виталий", "year": 33, "weight": 94.0},
# # ]
#
# html = """
# {%- macro input(name, value='', type='text', size='20') -%}
#     <input type='{{ type }}' name='{{ name }}' value='{{ value }}'>
# {%- endmacro %}
#
# <p> {{ input('username', 'Введите имя') }} </p>
# <p> {{ input('email', 'Введите email') }} </p>
# <p> {{ input('password') }} </p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)


# ===================================================
# from jinja2 import Template
#
# html = """
# {%- macro input(name, placeholder, type='text', size='20') -%}
# <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
# {%- endmacro %}
# <p>{{ input("firstname", "Имя") }}</p>
# <p>{{ input("lastname", "Фамилия") }}</p>
# <p>{{ input("address", "Адрес") }}</p>
# <p>{{ input("phone", "Телефон", "tel") }}</p>
# <p>{{ input("email", "Почта", "email") }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# ===================================================
# from jinja2 import Template
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0},
# ]
#
# html = """
# {% macro list_users(lst) %}
# <ul>
# {% for u in lst -%}
#     <li>{{ u.name }}</li>
# {% endfor -%}
# </ul>
# {%- endmacro %}
#
# {{ list_users(users) }}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

# ===================================================
# from jinja2 import Template
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0},
# ]
#
# html = '''
# {% macro list_users(users) %}
# <ul>
# {% for u in users -%}
#     <li>{{ u.name }} {{ caller(u) }}</li>
# {% endfor -%}
# </ul>
# {%- endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>age: {{ user.year }}</li>
#         <li>weight: {{ user.weight }}</li>
#     </ul>
# {% endcall %}
# '''
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg)

# ===================================================
from jinja2 import Environment, FileSystemLoader

# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0},
# ]

subs = ["Культура", "Наука", "Политика", "Спорт"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(list_table=subs)

print(msg)

