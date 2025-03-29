import requests


def test_url_status(url, status_code):
    """
    Проверяет, что URL возвращает ожидаемый статус-код.
    По умолчанию проверяет https://ya.ru на статус 200.
    """
    response = requests.get(url)

    assert response.status_code == status_code, (
        f"Ожидался статус {status_code}, но получен {response.status_code} для URL {url}"
    )
