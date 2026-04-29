import pytest
import apimarket


@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest.fixture
def sdk():
    apimarket.assemble(async_client=False)


@pytest.fixture
def sdk_async():
    apimarket.assemble(async_client=True)
