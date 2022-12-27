
## Зависимости

Для запуска проекта установить python версии 3.7 и выше и pip

## Локальный запуск проекта

После клонирования проекта выполните команды:

### Работа  с докером

### Установите Docker, Docker-Compose

### Команда для создание образа с нуля (понадобиться немного времени пока скачаются все образы)
```bash 
docker-compose up -d --build
```

### Затем накатите миграцию с помощью команды
```bash
docker-compose exec web python manage.py migrate --noinput
```
### Затем создайте суперюзера с помощью команды
```bash
docker-compose exec web python manage.py createsuperuser
```

### Команда для запуска проекта, вместо(python manage.py runserver)
```bash
docker-compose up
```
После переходите в localhost:8000/admin



