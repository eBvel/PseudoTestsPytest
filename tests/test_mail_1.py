import pytest


@pytest.fixture
def log_in():
    print("Вход в систему выполнен!")


def test_sending_mail_1(log_in):
    print("Письмо отправлено!")


def test_sending_mail_2(log_in):
    print("Письмо отправлено!")