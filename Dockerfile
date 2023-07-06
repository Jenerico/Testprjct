# Базовый образ Python
FROM python:3.9

# Установка зависимостей
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копирование кода в контейнер
COPY app /app

# Указываем рабочую директорию
WORKDIR /app

# Запуск приложения
CMD python app.py
