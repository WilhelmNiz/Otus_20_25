import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"


def test_get_single_brewery_by_id():
    """
    Тестирует получение данных конкретной пивоварни по ID.
    Проверяет:
    - успешность запроса (статус 200)
    - соответствие ID в ответе запрошенному
    - наличие всех обязательных полей в ответе
    """
    required_fields = [
        "id",
        "name",
        "brewery_type",
        "country",
        "city",
        "state",
        "postal_code"
    ]
    id = "5128df48-79fc-4f0f-8b52-d06be54d0cec"
    response = requests.get(f"{BASE_URL}/{id}")
    brewery_data = response.json()
    assert response.status_code == 200, "Запрос должен возвращать статус 200"
    assert brewery_data["id"] == id, "ID в ответе должен соответствовать запрошенному"
    for field in required_fields:
        assert field in brewery_data, f"В ответе отсутствует обязательное поле '{field}'"


@pytest.mark.parametrize("page, per_page", [(1, 10), (2, 5), (3, 20)])
def test_list_breweries_pagination(page, per_page):
    """
    Тестирует работу пагинации при получении списка пивоварен.
    Проверяет для каждой комбинации page/per_page:
    - успешность запроса (статус 200)
    - соответствие количества элементов значению per_page
    - отсутствие дубликатов ID на одной странице
    """
    all_breweries_ids = []
    response = requests.get(f"{BASE_URL}?page={page}&per_page={per_page}")
    breweries = response.json()
    current_page_ids = [b["id"] for b in breweries]
    all_breweries_ids.extend(current_page_ids)
    assert response.status_code == 200, "Запрос должен возвращать статус 200"
    assert len(breweries) == per_page, f"Количество элементов должно быть равно {per_page}"
    assert len(current_page_ids) == len(set(current_page_ids)), "Найдены дубликаты ID на одной странице"


@pytest.mark.parametrize("city, response_city",
                         [("san_diego", "San Diego"), ("denver", "Denver"), ("portland", "Portland")])
def test_filter_breweries_by_city(city, response_city):
    """
    Тестирует фильтрацию пивоварен по городу.
    Проверяет:
    - успешность запроса (статус 200)
    - непустой результат
    - соответствие города в ответе ожидаемому значению
    """
    response = requests.get(f"{BASE_URL}?by_city={city}&per_page=3")
    response_json = response.json()
    assert response.status_code == 200, "Запрос должен возвращать статус 200"
    assert len(response_json) > 0, "Результат не должен быть пустым"
    for brewery in response_json:
        assert brewery["city"] == response_city, f"Город должен быть {response_city}"


def test_filter_breweries_by_name():
    """
    Тестирует поиск пивоварен по названию.
    Проверяет:
    - успешность запроса (статус 200)
    - непустой результат
    - наличие искомой строки в названии
    """
    response = requests.get(f"{BASE_URL}?by_name=san_diego&per_page=3)")
    response_json = response.json()
    assert response.status_code == 200, "Запрос должен возвращать статус 200"
    assert len(response_json) > 0, "Результат не должен быть пустым"
    for brewery in response_json:
        assert "San Diego" in brewery["name"], "Название должно содержать 'San Diego'"


def test_brewery_types_validation():
    """
    Тестирует фильтрацию пивоварен по типу.
    Проверяет:
    - успешность запроса (статус 200)
    - непустой результат
    - соответствие типа пивоварни ожидаемому значению (micro)
    """
    response = requests.get(f"{BASE_URL}?by_type=micro&per_page=3")
    response_json = response.json()
    assert response.status_code == 200, "Запрос должен возвращать статус 200"
    assert len(response_json) > 0, "Результат не должен быть пустым"
    for brewery in response_json:
        assert brewery["brewery_type"] == "micro", "Тип пивоварни должен быть 'micro'"
