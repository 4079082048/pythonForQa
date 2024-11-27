import json

from setuptools.command.setopt import config_file
import importlib
from fixture.application import Application
import pytest
import os.path

from generator.group import testdata

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
     #путь к текущему файлу
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)

    if fixture is None or not fixture.is_valid():
            fixture = Application(browser=browser, baseUrl=target["baseUrl"])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc): #получить инфо о тест функции
    for fixture in metafunc.fixturenames: #пробегаем по всем параметрам
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%" % module).testdata #после импорта взять из модуля тестдата