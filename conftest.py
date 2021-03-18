import pytest
from nornir import InitNornir
# Creater pytest fixture
# Scopes (fuction, class, module, package, session)
@pytest.fixture(scope="session", autouse=True) # Decorator
def pytestnr():
    pytestnr = InitNornir(config_file="config.yaml")
    yield pytestnr
    pytestnr.close_connections()