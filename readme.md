# Тестовое 

## Требования
- Python 3.12
- MySQL 8.x (можно через Docker)

## Docker compose файлы
- `docker-compose.dev.yml` — только MySQL (разработка).
- `docker-compose.prod.yml` — MySQL + Django (условный прод-режим).

## 1) Поднять MySQL для разработки
```bash
cp .env.example .env
docker compose -f docker-compose.dev.yml up -d mysql
```

Проверь, что в `.env` есть: `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_ROOT_PASSWORD`, `MYSQL_HOST`, `MYSQL_PORT`.

## 2) Установить зависимости
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r req.pip
```

## 3) Применить миграции и создать админа
```bash
cd app
python manage.py migrate
python manage.py createsuperuser
```

## 4) Запустить проект
```bash
python manage.py runserver
```

Открыть:
- `http://127.0.0.1:8000/` — клиентская страница со слайдером
- `http://127.0.0.1:8000/admin/` — админка

## Как заполнять слайдер
1. В админке зайди в раздел `Слайды`.
2. Создай записи и выбери изображение через `django-filer`.
3. Порядок слайдов меняется drag&drop в списке (django-admin-sortable2).
4. На клиенте отображаются только активные записи.

## Запуск "всего сразу" (prod compose)
```bash
cp .env.example .env
docker compose -f docker-compose.prod.yml up -d --build
```
