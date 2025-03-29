import pytest


def pytest_addoption(parser):
    """Добавляем параметры командной строки для нашего теста"""
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="URL для проверки статуса"
    )
    parser.addoption(
        "--status-code",
        default=200,
        type=int,
        help="Ожидаемый HTTP статус-код"
    )


@pytest.fixture
def url(request):
    """Фикстура, возвращающая URL из параметров командной строки"""
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    """Фикстура, возвращающая статус-код из параметров командной строки"""
    return request.config.getoption("--status-code")
