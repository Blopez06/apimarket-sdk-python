import pytest
import apimarket


@pytest.mark.integracion
class TestValidarCedulaIntegration:
    def test_valid_cedula_returns_success(self, sdk):
        response = apimarket.validate_sep_cedula("12345678")
        assert response.success is True
        assert response.status == 200
        assert response.codigo_validacion is not None

    def test_found_cedula_returns_data_list(self, sdk):
        response = apimarket.validate_sep_cedula("12345678")
        assert response.data is not None
        assert isinstance(response.data, list)
        assert len(response.data) > 0

    def test_cedula_item_has_personal_fields(self, sdk):
        response = apimarket.validate_sep_cedula("12345678")
        item = response.data[0]
        assert item.id_cedula is not None
        assert item.nombre is not None
        assert item.paterno is not None
        assert item.titulo is not None
        assert item.desins is not None

    def test_cedula_item_has_registro_fields(self, sdk):
        response = apimarket.validate_sep_cedula("12345678")
        item = response.data[0]
        assert item.anioreg is not None
        assert item.fecha_expedicion is not None
        assert item.tipo is not None

    def test_not_found_cedula_returns_empty_data(self, sdk):
        response = apimarket.validate_sep_cedula("00000000")
        assert response.success is True
        assert response.status == 200
        assert response.data is None or response.data == []
