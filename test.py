from pprint import pprint

from requests import get, post, put

'''print(put('http://localhost:5000/api/news/1',
          json=
          {'title': 'new title'}).json())

print(post('http://localhost:5000/api/news').json())
print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())
print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False,
                 'is_published': True}).json())'''
print(put('http://127.0.0.1:5000/api/news/1', data=[{'title': "Новое название",
                                                    'content': "Новый текст новости"}],
          headers={'content-Type': 'application/json'}))
