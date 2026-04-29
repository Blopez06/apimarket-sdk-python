import pytest
import apimarket


@pytest.mark.integracion
class TestIdseProIntegration:
    def test_list_certificates_returns_results(self, sdk):
        certificates = apimarket.idse_list_certificates()
        assert certificates is not None
        assert len(certificates) > 0

    def test_certificate_has_required_fields(self, sdk):
        certificates = apimarket.idse_list_certificates()
        cert = certificates[0]
        assert cert.name is not None
        assert cert.rfc is not None
        assert cert.valid_until is not None
