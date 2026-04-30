import pytest
import apimarket


@pytest.mark.integracion
class TestCalcularRfcIntegration:
    def test_calculates_rfc_from_personal_data(self, sdk):
        response = apimarket.calculate_rfc("Juan Carlos", "Garcia", "Lopez", "01", "01", "1990")
        assert response.success is True
        assert response.status == 200
        assert response.codigo_validacion is not None

    def test_response_data_has_rfc(self, sdk):
        response = apimarket.calculate_rfc("Juan Carlos", "Garcia", "Lopez", "01", "01", "1990")
        assert response.data is not None
        assert response.data.rfc is not None

    def test_response_data_has_personal_fields(self, sdk):
        response = apimarket.calculate_rfc("Juan Carlos", "Garcia", "Lopez", "01", "01", "1990")
        assert response.data.nombres is not None
        assert response.data.apellido_paterno is not None
        assert response.data.apellido_materno is not None
        assert response.data.fecha_nacimiento is not None

    def test_response_data_has_mensaje(self, sdk):
        response = apimarket.calculate_rfc("Juan Carlos", "Garcia", "Lopez", "01", "01", "1990")
        assert response.data.mensaje is not None
