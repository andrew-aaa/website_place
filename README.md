# Москва глазами Артёма 🗺️

Интерактивная карта Москвы с интересными местами, собранными Артёмом.

## О проекте

Веб-приложение на Django с интерактивной картой Leaflet, показывающее различные интересные места в Москве. Каждое место отмечено на карте пульсирующим маркером с подробным описанием в боковой панели.

## 🚀 Возможности

- **Интерактивная карта** на основе Leaflet с пульсирующими маркерами
- **Боковая панель** с детальной информацией о местах
- **Карусель изображений** для каждого места
- **Админ-панель** с Drag&Drop сортировкой изображений
- **GeoJSON API** для интеграции с другими сервисами
- **Адаптивный дизайн** для мобильных устройств

## 🛠 Технологии

- **Backend**: Django 5.2, Python 3.8+
- **Frontend**: Vue.js 2.6, Leaflet, Bootstrap 4.5
- **Карты**: OpenStreetMap, Leaflet providers
- **База данных**: SQLite (разработка) / PostgreSQL (продакшен)
- **Дополнительно**: CKEditor, django-nested-admin

## 📦 Установка и запуск

### 1. Клонирование репозитория
```bash
git clone <repository-url>
cd website_place_artem
```

### 2. Настройка виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения
Создайте файл `.env` в корне проекта:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost
DB_PORT=5432
```

### 5. Миграции базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Создание суперпользователя
```bash
python manage.py createsuperuser
```

### 7. Сбор статических файлов
```bash
python manage.py collectstatic
```

### 8. Запуск сервера
```bash
# Обычный запуск
python manage.py runserver

# С SSL для разработки
python manage.py runserver_plus --cert-file cert.crt
```

## 🗄 Настройка базы данных

### Для разработки (SQLite)
Используется по умолчанию в settings.py

### Для продакшена (PostgreSQL)
Раскомментируйте настройки PostgreSQL в `settings.py` и установите:
```bash
pip install psycopg2-binary
```

## 👨‍💻 Администрирование

Доступ к админ-панели: `/admin/`

**Особенности админки:**
- Drag&Drop сортировка изображений мест
- WYSIWYG редактор для описаний (CKEditor)
- Предпросмотр изображений
- Вложенное редактирование мест и их изображений

## 🌐 API endpoints

- `GET /places.geojson` - все места в формате GeoJSON
- `GET /places/<id>/json/` - детальная информация о месте

## 🎨 Настройка карты

### Добавление новых мест
1. Зайдите в админ-панель `/admin/`
2. Добавьте новое место с координатами (широта/долгота)
3. Загрузите изображения с сортировкой по позициям

### Кастомизация маркеров
В `index.html` можно настроить:
- Цвет пульсации маркеров
- Размер иконок
- Скорость пульсации

## 🔧 Разработка

### Структура проекта
```
myproject/                 # Корневая директория проекта
├── manage.py
│
├── myproject/             # Главная конфигурация проекта
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── app/                  # Основное приложение
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   │
│   ├── templates/         # HTML шаблоны
│   │   └── app/
│   │       └── index.html
│   │
│   ├── static/           # Статические файлы
│   │   └── app/
│   │       ├── css/
│   │       │   ├── components/
│   │       │   └── leaflet-sidebar.css
│   │       ├── js/
│   │       │   └── leaflet-sidebar.js
│   │       ├── images/
│   │       │   ├── favicon.png
│   │       │   └── hand-pointer-regular.svg
│   │
│   └── migrations/
│       └── __init__.py
```

### Логирование
Используется кастомный логгер с уровнями:
- `debug` - отладочная информация
- `error` - ошибки приложения

## 🚀 Деплой

### Подготовка к продакшену
1. Установите `DEBUG=False` в `.env`
2. Настройте `ALLOWED_HOSTS` с доменом сайта
3. Используйте PostgreSQL вместо SQLite
4. Настройте SSL сертификаты
5. Соберите статические файлы

### Рекомендуемая инфраструктура
- **WSGI сервер**: Gunicorn или uWSGI
- **Веб-сервер**: Nginx с проксированием
- **База данных**: PostgreSQL
- **Файловое хранилище**: AWS S3 или подобное

## 🐛 Устранение проблем

### Статические файлы не загружаются
```bash
python manage.py collectstatic --noinput
```

### Ошибки миграций
```bash
python manage.py makemigrations --dry-run --verbosity 3
```

### Проблемы с SSL в разработке
Убедитесь, что установлен `django-extensions`:
```bash
pip install django-extensions
```

## 📄 Лицензия

## MIT License

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте https://dvmn.org/.

Тестовые данные взяты с сайта https://kudago.com/.

## Иконки и ресурсы

- Иконки: [Font Awesome](https://fontawesome.com/) (лицензия зависит от используемых иконок)
- Карты: [OpenStreetMap](https://www.openstreetmap.org/copyright) (ODbL)
- Библиотеки: См. соответствующие лицензии в package.json и requirements.txt

*Примечание: Убедитесь, что все сторонние библиотеки и ресурсы совместимы с MIT лицензией.*

## 👤 Автор

https://github.com/devmanorg/where-to-go-frontend/
https://github.com/andrew-aaa

---

**Примечание**: Для безопасности никогда не коммитьте приватные ключи и чувствительные данные в репозиторий. Все настройки должны быть через переменные окружения.
