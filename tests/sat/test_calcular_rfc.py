import pytest
import apimarket
from apimarket.validations import InvalidRFCError


@pytest.mark.integracion
class TestCalcularRfcIntegration:
    def test_calculates_rfc_from_personal_data(self, sdk):
        response = apimarket.calculate_rfc("Bryan Antonio", "Lopez", "Hernadez", "06", "06", 1997)
        rfc = response.additional_data['data']['rfc']
        validation_code = response.additional_data['codigoValidacion']
        assert rfc is not None
        assert validation_code is not None
