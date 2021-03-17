import pytest
from nornir import InitNornir
# Creater pytest fixture
# Scopes (fuction, class, module, package, session)
@pytest.fixture(scope="session", autouse=True) # Decorator
def nr():
    nr = InitNornir(config_file="config.yaml")
    yield nr
    nr.close_connections()