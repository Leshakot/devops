# JupyterHub в Docker

Этот проект запускает JupyterHub с аутентификацией и пользовательскими контейнерами через DockerSpawner.

---

## Структура

- `docker-compose.yml` — описывает сервисы JupyterHub и пользовательских ноутбуков  
- `jupyterhub_config.py` — конфигурация JupyterHub и DockerSpawner  
- `.env` — файл с переменными окружения (например, данные для подключения к базе)  
- `pattern_notebook/` — Dockerfile и образ для пользовательских ноутбуков  

---

## Быстрый старт

1. Клонируйте репозиторий:

   ```bash
   git clone <URL_репозитория>
   cd <имя_папки_репозитория>
   ```

2. Убедитесь, что у вас установлен [Docker](https://www.docker.com/get-started) и [Docker Compose](https://docs.docker.com/compose/install/).  
 
3. Соберите и запустите контейнеры в фоне:

   ```bash
   docker-compose up -d --build
   ```

4. Откройте JupyterHub в браузере:

   ```bash
   http://<IP>:8000
   ```

---

## Остановка и удаление контейнеров

1. Остановить и удалить контейнеры (тома сохраняются):

   ```bash
   docker-compose down
   ```

2. Полная остановка с удалением всех томов и данных:

   ```bash
   docker-compose down -v
   ```

> ⚠️ **Внимание**: эта команда удалит все связанные с проектом тома, включая базы данных и пользовательские данные.
