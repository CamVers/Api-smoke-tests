import requests
import pytest

#Базовый URL тестового API
BASE_URL = "https://jsonplaceholder.typicode.com"

#Smoke-тест: проверка доступности API
def test_api_get_posts():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, "API не отвечает"
    assert "userId" in response.json(), "Неправильная структура JSON"

#Тест на создание поста (POST-запрос)
def test_api_create_post():
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201, "Пост не создан"
    assert response.json()["id"] == 101, "ID нового поста неверный"

#Запуск: pytest test_api.py -v