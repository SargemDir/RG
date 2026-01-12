FROM python:3.11-slim

# Установка Chromium и необходимых инструментов для сборки пакетов
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    ca-certificates \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# По умолчанию запуск pytest
CMD ["pytest"]
