import pytest
import apimarket
from apimarket.validations import InvalidCURPError


class TestObtenerRfcUnit:
    @pytest.mark.parametrize("curp, expected_code", [
        ("LOOA531113",           InvalidCURPError.Code.INVALID_LENGTH),
        ("LOOA531113HTCPBN07XX", InvalidCURPError.Code.INVALID_LENGTH),
        ("123456789012345678",   InvalidCURPError.Code.INVALID_FORMAT),
        ("LOOA531113HTCPBN09",   InvalidCURPError.Code.INVALID_DIGIT),
    ])
    def test_invalid_curp_raises_before_api_call(self, curp, expected_code):
        with pytest.raises(InvalidCURPError) as exc_info:
            apimarket.get_rfc_from_curp(curp)
        assert exc_info.value.code == expected_code


@pytest.mark.integracion
class TestObtenerRfcIntegration:
    CURP = "LOOA531113HTCPBN07"

    def test_valid_curp_returns_success(self, sdk):
        response = apimarket.get_rfc_from_curp(self.CURP)
        assert response is not None
        assert response.success is True
        assert response.status is not None
        assert response.codigo_validacion is not None

    def test_response_with_rfc_has_typed_data(self, sdk):
        response = apimarket.get_rfc_from_curp(self.CURP)
        assert response.success is True
        if response.data is not None:
            assert isinstance(response.data.rfc, str)
            assert len(response.data.rfc) >= 12

    def test_response_without_rfc_has_message(self, sdk):
        response = apimarket.get_rfc_from_curp(self.CURP)
        assert response.success is True
        if response.data is None:
            assert response.message is not None
            assert response.status == 204
