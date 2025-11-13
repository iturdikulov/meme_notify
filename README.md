## Видео обзор

## Описание проекта

Django 5.x проект с Celery+Redis для асинхронных задач, PostgreSQL.

Приложения: `pages` (UI/формы), `up` (уведомления).

На главной странице пользователь генерирует случайные уведомления с начальным
каналом (SMS/Email/Telegram) с симуляцией сбоев.

### Генерация сообщений

На главной (`pages/views.py`) - форма для `NotificationGenerator` (канал:
telegram/sms/email). Генерируем задачи для отправки сообщений. Задачи
выполняются в воркере Celery.

Каждая задача берёт рандомный мем из `PHOTOBOX_MEMES_RU` (заголовок + описание),
и создаёт уведомление `Notification` (статус=pending, retry=0).

### Доставка

В `send_notification` (`up/notifications.py`): отправляем уведомления по
приоритету - initial_channel (задаёт пользователь), затем другие.

Симуляция отправки: sleep 1-5с, успех отправки случайный (SMS: 30%, Email: 40%,
Telegram: 50%).

## Быстрый запуск

Шаблонный код основан на https://github.com/nickjj/docker-django-example,
используется базовый Django / Celery / Docker проект.

### Основные требования

- **Docker должен быть установлен** (Windows, macOS, Linux).
- **Docker Compose v2** нужен для проекта, версия **2.20.2+**.
- На **Windows** рекомендуется использовать **WSL / WSL2**, так как команды
  выполняются в shell. Можно адаптировать для PowerShell.

### Настройка проекта

1. **Клонирование репозитория и переход в директорию**:

```bash
git clone https://github.com/iturdikulov/meme_notify
cd meme_notify
```

2. **Создаём .env файла** (оригинальный игнорируется):

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

- Загружаются Docker-образы, устанавливаются зависимости Python + Yarn.

### Частые ошибки и решения

- **depends_on "Additional property required is not allowed"** → обновить Docker
  Compose до **2.20.2+** или Docker Desktop **4.22.0+**.
- **Порт занят** → проверить переменную **DOCKER_WEB_PORT_FORWARD** в `.env`.
- **Permission denied** → проверить uid:gid на Linux (должно быть 1000:1000),
  при необходимости настроить переменные UID и GID в `.env`.

### Инициализация базы данных

```bash
./run manage migrate
```

### Проверка работы

- **Браузер:** [http://localhost:8000](http://localhost:8000)

### Управление контейнерами

Остановка:

```bash
docker compose down
```

Запуск повторно:

```bash
docker compose up
```

Удаляем все (volumes, images):

```bash
docker compose down -v --rmi all
```
