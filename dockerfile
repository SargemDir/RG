FROM python:3.11-slim

# Установка Chromium и зависимостей
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Установка Python-зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]
