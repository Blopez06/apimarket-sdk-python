import pytest
import apimarket
from apimarket.validations import InvalidNSSError

NSS_VALIDO = "12345678952"


class TestInfonavitUnit:
    @pytest.mark.parametrize("nss, expected_code", [
        ("1234567",      InvalidNSSError.Code.INVALID_LENGTH),
        ("1234567890A",  InvalidNSSError.Code.INVALID_FORMAT),
        ("12345678900",  InvalidNSSError.Code.INVALID_DIGIT),
    ])
    def test_search_credit_invalid_nss_raises(self, nss, expected_code):
        with pytest.raises(InvalidNSSError) as exc_info:
            apimarket.search_credit_by_nss(nss)
        assert exc_info.value.code == expected_code

    @pytest.mark.parametrize("nss, expected_code", [
        ("1234567",      InvalidNSSError.Code.INVALID_LENGTH),
        ("1234567890A",  InvalidNSSError.Code.INVALID_FORMAT),
        ("12345678900",  InvalidNSSError.Code.INVALID_DIGIT),
    ])
    def test_get_subaccount_invalid_nss_raises(self, nss, expected_code):
        with pytest.raises(InvalidNSSError) as exc_info:
            apimarket.get_infonavit_subaccount(nss)
        assert exc_info.value.code == expected_code


@pytest.mark.integracion
class TestSearchCreditByNssIntegration:
    def test_valid_nss_returns_response(self, sdk):
        response = apimarket.search_credit_by_nss(NSS_VALIDO)
        assert response is not None
        assert response.success is True
        assert response.codigo_validacion is not None

    def test_response_has_status(self, sdk):
        response = apimarket.search_credit_by_nss(NSS_VALIDO)
        assert response.status is not None


@pytest.mark.integracion
class TestGetInfonavitSubaccountIntegration:
    def test_valid_nss_returns_response(self, sdk):
        response = apimarket.get_infonavit_subaccount(NSS_VALIDO)
        assert response is not None
        assert response.success is True
        assert response.codigo_validacion is not None

    def test_response_has_status(self, sdk):
        response = apimarket.get_infonavit_subaccount(NSS_VALIDO)
        assert response.status is not None
