Yatube API

Описание

        Yatube API — это REST API для социальной сети, где пользователи могут публиковать посты,
        комментировать чужие записи, подписываться на других пользователей, объединяться в группы по интересам.

API создан с использованием Django REST Framework. Проект поддерживает авторизацию по JWT-токенам, фильтрацию и пагинацию данных.

Установка и запуск проекта:

    Клонировать репозиторий:

    git clone https://github.com/your-username/blog-api.git
    cd blog-api

Создание и активировация виртуальное окружение:

    python -m venv venv
    source venv/bin/activate      # для Linux/macOS
    venv\Scripts\activate         # для Windows

Установка зависимостей:

    pip install -r requirements.txt

Создание базы данных и выполнение миграций:

    python manage.py migrate

Создание суперпользователя (по желанию):

    python manage.py createsuperuser

Запуск сервера:

    python manage.py runserver

Аутентификация

Для аутентификации используется JWT:

    POST /api/v1/jwt/create/ — получение access и refresh токен.

    POST /api/v1/jwt/refresh/ — обновление access токен.

    POST /api/v1/jwt/verify/ — проверка валидность access токена.

Примеры запросов к API

Получение списка постов:

    GET /api/v1/posts/

Ответ:

    {
        "count": 12,
        "next": null,
        "previous": null,
        "results": [
            {
            "id": 1,
            "text": "Пример поста",
            "pub_date": "2025-05-13T19:04:12.555Z",
            "author": "user1",
            "image": null,
            "group": null
            }
        ]
    }

Создание нового поста:

    POST /api/v1/posts/(Требуется авторизация)

Тело запроса:

    {
        "text": "Новый пост",
        "group": 1
    }

Получение комментариев к посту:

    GET /api/v1/posts/1/comments/

Подписка на пользователя:

    POST /api/v1/follow/(Требуется авторизация)

    Тело запроса:

        {
            "following": "username"
        }

    Ответ:

        {
            "user": "current_user",
            "following": "username"
        }

Технологии

    Python 3.10+

    Django 5+

    Django REST Framework

    Simple JWT

    SQLite (по умолчанию)

Лицензия

    Проект представлен в учебных целях и распространяется без лицензии