import pytest
import apimarket
from apimarket.validations import InvalidCURPError


class TestValidarCurpUnit:
    @pytest.mark.parametrize("curp, expected_code", [
        ("LOOA531113",           InvalidCURPError.Code.INVALID_LENGTH),
        ("LOOA531113HTCPBN07XX", InvalidCURPError.Code.INVALID_LENGTH),
        ("123456789012345678",   InvalidCURPError.Code.INVALID_FORMAT),
        ("LOOA531113HTCPBN09",   InvalidCURPError.Code.INVALID_DIGIT),
    ])
    def test_invalid_curp_raises_before_api_call(self, curp, expected_code):
        with pytest.raises(InvalidCURPError) as exc_info:
            apimarket.fetch_curp_details(curp)
        assert exc_info.value.code == expected_code


@pytest.mark.integracion
class TestValidarCurpIntegration:
    def test_valid_curp_returns_success(self, sdk):
        response = apimarket.fetch_curp_details("LOOA531113HTCPBN07")
        assert response.success is True
        assert response.status == 200
        assert response.codigo_validacion is not None

    def test_response_has_personal_fields(self, sdk):
        response = apimarket.fetch_curp_details("LOOA531113HTCPBN07")
        assert response.data.curp == "LOOA531113HTCPBN07"
        assert response.data.apellido_paterno == "LOPEZ"
        assert response.data.apellido_materno == "OBRADOR"
        assert response.data.nombres is not None
        assert response.data.fecha_nacimiento is not None
        assert response.data.estado_nacimiento is not None
        assert response.data.sexo is not None

    def test_response_has_historial(self, sdk):
        response = apimarket.fetch_curp_details("LOOA531113HTCPBN07")
        assert response.data.historial is not None

    def test_response_has_doc_probatorio(self, sdk):
        response = apimarket.fetch_curp_details("LOOA531113HTCPBN07")
        assert response.data.datos_doc_probatorio is not None


@pytest.mark.integracion
@pytest.mark.anyio
async def test_async_valid_curp_returns_success(sdk_async):
    response = await apimarket.fetch_curp_details("LOOA531113HTCPBN07")
    assert response.data.apellido_paterno == "LOPEZ"
    assert response.data.apellido_materno == "OBRADOR"
