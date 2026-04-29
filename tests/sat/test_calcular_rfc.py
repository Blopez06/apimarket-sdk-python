import pytest
import apimarket
from apimarket.validations import validate_birth_date, InvalidBirthDateError


class TestValidateFechaNacimiento:
    @pytest.mark.parametrize("dia, mes, ano", [
        ("06", "06", "1997"),
        ("01", "12", "1990"),
        ("31", "01", "2000"),
    ])
    def test_valid_fecha_passes(self, dia, mes, ano):
        validate_birth_date(dia, mes, ano)

    @pytest.mark.parametrize("dia, mes, ano, expected_code", [
        ("6",  "06", "1997", InvalidBirthDateError.Code.INVALID_DIA_FORMAT),
        ("ab", "06", "1997", InvalidBirthDateError.Code.INVALID_DIA_FORMAT),
        ("06", "6",  "1997", InvalidBirthDateError.Code.INVALID_MES_FORMAT),
        ("06", "ab", "1997", InvalidBirthDateError.Code.INVALID_MES_FORMAT),
        ("06", "06", "90",   InvalidBirthDateError.Code.INVALID_ANO_FORMAT),
        ("06", "06", "abc",  InvalidBirthDateError.Code.INVALID_ANO_FORMAT),
    ])
    def test_invalid_fecha_raises(self, dia, mes, ano, expected_code):
        with pytest.raises(InvalidBirthDateError) as exc_info:
            validate_birth_date(dia, mes, ano)
        assert exc_info.value.code == expected_code
        assert exc_info.value.message is not None

    def test_dia_error_message_describes_format(self):
        with pytest.raises(InvalidBirthDateError) as exc_info:
            validate_birth_date("6", "06", "1997")
        assert "2 dígitos" in exc_info.value.message

    def test_ano_error_message_describes_format(self):
        with pytest.raises(InvalidBirthDateError) as exc_info:
            validate_birth_date("06", "06", "97")
        assert "4 dígitos" in exc_info.value.message


@pytest.mark.integracion
class TestCalcularRfcIntegration:
    def test_calculates_rfc_from_personal_data(self, sdk):
        response = apimarket.calculate_rfc("Bryan Antonio", "Lopez", "Hernandez", "06", "06", "1997")
        assert response.success is True
        assert response.status == 200
        assert response.codigo_validacion is not None

    def test_response_data_has_rfc(self, sdk):
        response = apimarket.calculate_rfc("Bryan Antonio", "Lopez", "Hernandez", "06", "06", "1997")
        assert response.data is not None
        assert response.data.rfc is not None

    def test_response_data_has_personal_fields(self, sdk):
        response = apimarket.calculate_rfc("Bryan Antonio", "Lopez", "Hernandez", "06", "06", "1997")
        assert response.data.nombres is not None
        assert response.data.apellido_paterno is not None
        assert response.data.apellido_materno is not None
        assert response.data.fecha_nacimiento is not None

    def test_response_data_has_mensaje(self, sdk):
        response = apimarket.calculate_rfc("Bryan Antonio", "Lopez", "Hernandez", "06", "06", "1997")
        assert response.data.mensaje is not None
