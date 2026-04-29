import pytest
import apimarket


@pytest.mark.integracion
class TestObtenerCurpIntegration:
    def test_valid_data_returns_curp(self, sdk):
        response = apimarket.get_curp_from_details(
            "JUAN CARLOS", "GARCIA", "MARTINEZ", "15", "03", "1990", "09", "H"
        )
        assert response.success is True
        assert response.data.curp is not None
        assert len(response.data.curp) == 18

    def test_response_has_all_fields(self, sdk):
        response = apimarket.get_curp_from_details(
            "JUAN CARLOS", "GARCIA", "MARTINEZ", "15", "03", "1990", "09", "H"
        )
        assert response.data.nombres is not None
        assert response.data.apellido_paterno is not None
        assert response.data.apellido_materno is not None
        assert response.data.sexo is not None
        assert response.data.fecha_nacimiento is not None
        assert response.data.estado_nacimiento is not None
        assert response.data.mensaje is not None

    def test_without_materno_returns_empty_string(self, sdk):
        response = apimarket.get_curp_from_details(
            "JUAN", "GARCIA", "", "15", "03", "1990", "09", "H"
        )
        assert response.success is True
        assert response.data.apellido_materno == ""
