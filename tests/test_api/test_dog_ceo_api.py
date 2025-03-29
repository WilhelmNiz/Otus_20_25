import pytest
import requests

BASE_URL = "https://dog.ceo/api"


def test_api_returns_200_status_code():
    """
    Проверяет, что API возвращает статус код 200 (успешный запрос)
    """
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200, "API должен возвращать статус код 200 для успешного запроса"


@pytest.mark.parametrize("field", ["message", "status"])
def test_response_contains_required_fields(field):
    """
    Проверяет, что ответ API содержит обязательные поля
    """
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    response_json = response.json()
    assert field in response_json, f"Поле {field} отсутствует в ответе"


def test_response_has_correct_status_and_url_format():
    """
    Проверяет что:
    1. Поле status имеет значение 'success'
    2. URL изображения начинается с https://
    """
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    response_json = response.json()
    assert response_json["status"] == "success", (f"Ожидался статус 'success', получен '{response_json['status']}'")
    assert response_json["message"].startswith("https://"), ("URL изображения должен начинаться с 'https://'")


def test_random_image_url_valid():
    """
    Проверяет, что URL изображения имеет допустимое расширение (.jpg)
    """
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    response_json = response.json()
    assert ".jpg" in response_json["message"], "URL изображения должен содержать расширение .jpg"


def test_invalid_endpoint_returns_error():
    """
    Проверяет обработку несуществующего эндпоинта
    """
    response = requests.get(f"{BASE_URL}/breeds/image/invalid")
    response_json = response.json()
    assert response.status_code == 404, "Для несуществующего эндпоинта должен возвращаться статус код 404"
    assert response_json["status"] == "error", "Для несуществующего эндпоинта статус должен быть 'error'"


@pytest.mark.parametrize("num_requests", [5, 10])
def test_multiple_random_images_unique(num_requests):
    """
    Проверяет что при нескольких запросах возвращаются разные URL изображений
    """
    collected_urls = []

    for _ in range(num_requests):
        response = requests.get(f"{BASE_URL}/breeds/image/random")
        data = response.json()
        collected_urls.append(data["message"])

    assert len(set(collected_urls)) > 1, f"Все {num_requests} URL одинаковые: {collected_urls}"
