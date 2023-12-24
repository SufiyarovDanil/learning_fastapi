# Learning FastAPI

Ну... типа.. да, решил начать изучать фастапи а о чем еще тут писать?

Предметная область - Музыка.

Приложение позволяет работать с информацией о музыкальных группах
и их творчестве (Альбомы, треки и т.д.)

## Инструкция по запуску

в папке src необходимо создать файл `.env`
```
# src/.env
DB_HOST=your host
DB_PORT=your port
DB_USER=postgres
DB_PASS=postgres
DB_NAME=music
SECRET_KEY=your secret key
```
Для миграции БД использую библиотеку Alembic,
инструкция по миграции находится в `migrations/README`
