# Stage 1: Dependências
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Stage 2: Final
FROM python:3.11-slim
WORKDIR /app
COPY --from=build /app/app.py .
EXPOSE 5000
USER nonroot
LABEL maintainer="Seu Nome"
LABEL version="1.0"
CMD ["python", "app.py"]