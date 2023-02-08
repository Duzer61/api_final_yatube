# Проект «API для Yatube».
### Описание
Учебный проект создан в рамках курса по API от
[Яндекс.Практикум](https://practicum.yandex.ru/).
API реализован на Django Rest Framework. API предоставляет
пользователям ресурсы для создания постов, комментариев к ним,
подписок на других пользователей. Реализованы авторизация,
разграничение прав пользователей, пагинация, поиск по подписчикам.


### Технологии
- Python 3.9
- Django==3.2.16
- Django Rest Framework


## Установка проекта из репозитория (описание для Windows)
 - Клонировать репозиторий `git clone <адрес вашего репозитория>`
 - перейти в директорию с клонированным репозиторием
 - установить виртуальное окружение `python -m venv venv`
 - активировать виртуальное окружение `source venv/Scripts/activate`
 - Установите зависимости `pip install -r requirements.txt`
 - Выполнить миграции `python manage.py migrate`
 - Запустить проект в dev-режиме `python manage.py runserver`

## Примеры запросов к API:
 - GET запрос к списку постов: `/api/v1/posts/`
 - POST запрос для публикации нового поста: `/api/v1/posts/`

    {
    	"text": "string",
    	"image": "string",
    	"group": 1
    }
 - POST запрос для создания комментария: `/api/v1/posts/{post_id}/comments/`
    {
    	"text": "string"
    }
 - PATCH запрос для редактирования комментария: `/api/v1/posts/{post_id}/comments/{id}/`
	 {
	 	"text": "string"
	 }

### Автор
Данил Кочетов - [GitHub](https://github.com/Duzer61)
