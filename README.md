## Видео обзор



## Быстрый запуск

Шаблонный код основан на https://github.com/nickjj/docker-django-example,
используется базовый Django / Celery / Docker проект.

### Основные требования

* **Docker должен быть установлен** (Windows, macOS, Linux).
* **Docker Compose v2** нужен для проекта, версия **2.20.2+**.
* На **Windows** рекомендуется использовать **WSL / WSL2**, так как команды выполняются в shell. Можно адаптировать для PowerShell.

### Настройка проекта

1. **Клонирование репозитория и переход в директорию**:

```bash
git clone https://github.com/nickjj/docker-django-example meme_notify
cd meme_notify
```

2. **Создание .env файла** (оригинальный игнорируется):

```bash
cp .env.example .env
```

3. **Сборка проекта** (первый запуск ~5-10 минут, для установки и загрузки
   зависемостей):

```bash
docker compose up --build
# Мониторинг, можно запустить в отдельном терминале или с параметром -d
docker compose up flower 
```

* Загружаются Docker-образы, устанавливаются зависимости Python + Yarn.

### Частые ошибки и решения

* **depends_on "Additional property required is not allowed"** → обновить Docker Compose до **2.20.2+** или Docker Desktop **4.22.0+**.
* **Порт занят** → проверить переменную **DOCKER_WEB_PORT_FORWARD** в `.env`.
* **Permission denied** → проверить uid:gid на Linux (должно быть 1000:1000), при необходимости настроить переменные UID и GID в `.env`.

### Инициализация базы данных

```bash
./run manage migrate
```

### Проверка работы

* **Браузер:** [http://localhost:8000](http://localhost:8000)

### Управление контейнерами

* **Остановка:**

```bash
docker compose down
```

* **Запуск повторно:**

```bash
docker compose up
```

(будет быстрее, чем первый запуск)
