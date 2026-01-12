FROM python:3.11-slim

# Установка Chromium и зависимостей
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копируем и устанавливаем зависимости для Docker
COPY requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt

# Копируем проект
COPY . .

# По умолчанию запускаем pytest
CMD ["pytest", "--junitxml=/app/test-results/results.xml", "--html=/app/test-results/report.html"]
