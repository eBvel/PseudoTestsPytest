import pytest


# По умолчанию, scope="function". Его можно указать явно.
@pytest.fixture(scope="function")
def log_in(launch):
    print("Вход в систему выполнен!")
    yield
    print("Произведен выход из системы!")


@pytest.fixture(scope="module")
def launch():
    print("Запуск модуля!")
    yield
    print("Завершение модуля!")