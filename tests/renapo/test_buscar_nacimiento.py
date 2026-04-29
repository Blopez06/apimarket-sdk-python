import pytest
import apimarket
from apimarket.validations import InvalidCURPError


class TestBuscarNacimientoUnit:
    @pytest.mark.parametrize("curp, expected_code", [
        ("LOOA531113",           InvalidCURPError.Code.INVALID_LENGTH),
        ("LOOA531113HTCPBN07XX", InvalidCURPError.Code.INVALID_LENGTH),
        ("123456789012345678",   InvalidCURPError.Code.INVALID_FORMAT),
        ("LOOA531113HTCPBN09",   InvalidCURPError.Code.INVALID_DIGIT),
    ])
    def test_invalid_curp_raises_before_api_call(self, curp, expected_code):
        with pytest.raises(InvalidCURPError) as exc_info:
            apimarket.get_birth_record(curp)
        assert exc_info.value.code == expected_code


@pytest.mark.integracion
class TestBuscarNacimientoIntegration:
    def test_valid_curp_returns_success(self, sdk):
        response = apimarket.get_birth_record("LOOA531113HTCPBN07")
        assert response.success is True
        assert response.status == 200
        assert response.codigo_validacion is not None

    def test_response_has_personal_fields(self, sdk):
        response = apimarket.get_birth_record("LOOA531113HTCPBN07")
        assert response.data.curp == "LOOA531113HTCPBN07"
        assert response.data.nombre is not None
        assert response.data.primer_apellido is not None
        assert response.data.segundo_apellido is not None
        assert response.data.fecha_nacimiento is not None
        assert response.data.sexo is not None
        assert response.data.nacionalidad is not None
        assert response.data.vivo_muerto is not None

    def test_response_has_datos_padres(self, sdk):
        response = apimarket.get_birth_record("LOOA531113HTCPBN07")
        assert response.data.datos_padres is not None
        assert response.data.datos_padres.nombre_padre is not None
        assert response.data.datos_padres.nombre_madre is not None

    def test_response_has_datos_doc_probatorio(self, sdk):
        response = apimarket.get_birth_record("LOOA531113HTCPBN07")
        assert response.data.additional_data.get('datosDocProbatorio') is not None
