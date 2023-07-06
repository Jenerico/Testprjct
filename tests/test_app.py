import requests
import pytest
import time

# Проверка, что основной эндпоинт возвращает ожидаемый результат "Hello, world!"
def test_hello_endpoint():
    response = requests.get("http://localhost:5000")
    assert response.status_code == 200
    assert response.text == "Hello, world!"

# Проверка, что эндпоинт "/health" возвращает статус "OK"
def test_health_endpoint():
    response = requests.get("http://localhost:5000/health")
    assert response.status_code == 200
    assert response.text == "OK"

# Проверка, что эндпоинт "/ready" возвращает статус "OK"
def test_ready_endpoint():
    response = requests.get("http://localhost:5000/ready")
    assert response.status_code == 200
    assert response.text == "OK"

# Проверка, что эндпоинт "/metrics" возвращает статус "200 OK"
def test_metrics_endpoint():
    response = requests.get("http://localhost:5000/metrics")
    assert response.status_code == 200

# Запуск приложения в Docker контейнере перед каждым тестом
@pytest.fixture(scope="module")
def docker_container():
    import docker
    import os

    client = docker.from_env()
    container = client.containers.run("your-docker-image-name", detach=True, ports={'5000': 5000})

    # Пауза для обеспечения запуска контейнера
    time.sleep(2)

    yield

    # Удаление контейнера после окончания тестов
    container.stop()
    container.remove()
