import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_todo_valid_structure():
    """
    Тестирует получение конкретной задачи:
    - Проверяет успешный статус ответа
    - Проверяет наличие всех обязательных полей в ответе
    """
    response = requests.get(f"{BASE_URL}/todos/1")
    rt = response.json()
    assert response.status_code == 200, "Ожидался статус код 200"
    assert "userId" in rt, "Ответ должен содержать поле 'userId'"
    assert "id" in rt, "Ответ должен содержать поле 'id'"
    assert "title" in rt, "Ответ должен содержать поле 'title'"
    assert "completed" in rt, "Ответ должен содержать поле 'completed'"


def test_get_nonexistent_todo_returns_404():
    """
    Тестирует обработку несуществующей задачи.
    - Проверяет возврат статуса 404
    - Проверяет пустой ответ
    """
    response = requests.get(f"{BASE_URL}/todos/9999999")
    assert response.status_code == 404, "Для несуществующей задачи должен возвращаться статус 404"
    assert len(response.json()) == 0, "Ответ для несуществующей задачи должен быть пустым"


def test_create_new_todo_success():
    response = requests.post(f"{BASE_URL}/todos")
    response_json = response.json()
    assert response.status_code == 201, "При создании должен возвращаться статус 201"
    assert response_json["id"] == 201, "Новая задача должна получить ID 201"


@pytest.mark.parametrize("post", [1, 5, 10])
def test_get_single_post_by_id(post):
    """
    Тестирует создание новой задачи:
    - Проверяет успешный статус создания (201)
    - Проверяет, что возвращается корректный ID новой задачи
    """
    response = requests.get(f"{BASE_URL}/posts/{post}")
    assert response.status_code == 200, f"Для поста {post} должен возвращаться статус 200"
    assert len(response.json()) > 0, f"Ответ для поста {post} не должен быть пустым"


@pytest.mark.parametrize("post", [1, 5, 10])
def test_comments_for_post(post):
    """
    Тестирует получение комментариев для поста (параметризованный):
    - Проверяет успешный статус ответа
    - Проверяет, что возвращается непустой список комментариев
    - Проверяет, что все комментарии относятся к запрошенному посту
    """
    response = requests.get(f"{BASE_URL}/posts/{post}/comments")
    comments = response.json()
    assert response.status_code == 200, f"Для поста {post} должен возвращаться статус 200"
    assert len(comments) > 0, f"Для поста {post} получен пустой список комментариев"
    for comment in comments:
        assert comment["postId"] == post, f"Комментарий с ID {comment['id']} принадлежит другому посту"
