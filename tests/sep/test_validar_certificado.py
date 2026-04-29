import pytest
import apimarket
from apimarket.validations import validate_folio_uuid, InvalidFolioError


class TestValidarCertificadoUUID:
    @pytest.mark.parametrize("folio", [
        "550e8400-e29b-41d4-a716-446655440000",
        "00000000-0000-0000-0000-000000000000",
        "ffffffff-ffff-ffff-ffff-ffffffffffff",
        "AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE",
    ])
    def test_valid_uuid_passes(self, folio):
        assert validate_folio_uuid(folio) == folio

    @pytest.mark.parametrize("folio, expected_code", [
        ("sin-formato-uuid",          InvalidFolioError.Code.INVALID_FORMAT),
        ("550e8400e29b41d4a716446655440000", InvalidFolioError.Code.INVALID_FORMAT),
        ("550e8400-e29b-41d4-a716",   InvalidFolioError.Code.INVALID_FORMAT),
        ("",                          InvalidFolioError.Code.INVALID_FORMAT),
        ("zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz", InvalidFolioError.Code.INVALID_FORMAT),
    ])
    def test_invalid_uuid_raises(self, folio, expected_code):
        with pytest.raises(InvalidFolioError) as exc_info:
            validate_folio_uuid(folio)
        assert exc_info.value.code == expected_code
        assert exc_info.value.message is not None

    def test_invalid_uuid_error_message_describes_format(self):
        with pytest.raises(InvalidFolioError) as exc_info:
            validate_folio_uuid("no-es-uuid")
        assert "UUID" in exc_info.value.message


@pytest.mark.integracion
class TestValidarCertificadoIntegration:
    FOLIO_VALIDO = "550e8400-e29b-41d4-a716-446655440000"

    def test_valid_folio_returns_response(self, sdk):
        response = apimarket.validate_sep_certificate(self.FOLIO_VALIDO)
        assert response is not None
        assert response.codigo_validacion is not None

    def test_response_has_status(self, sdk):
        response = apimarket.validate_sep_certificate(self.FOLIO_VALIDO)
        assert response.status is not None

    def test_found_certificate_has_data(self, sdk):
        response = apimarket.validate_sep_certificate(self.FOLIO_VALIDO)
        if response.success and response.data:
            assert response.data.folio is not None
            assert response.data.nombres is not None
            assert response.data.institucion is not None
            assert response.data.tipo_certificacion is not None
