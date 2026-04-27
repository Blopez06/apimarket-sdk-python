import pytest

import apimarket

__author__ = "Carlos Eduardo Sanchez Torres (sanchezcarlosjr)"
__copyright__ = "Carlos Eduardo Sanchez Torres (sanchezcarlosjr)"
__license__ = "MIT"


@pytest.mark.anyio
async def test_async_fetch_curp_details():
    apimarket.assemble(async_client=True)
    response = await apimarket.fetch_curp_details("LOOA531113HTCPBN07")
    assert response.data.apellido_paterno == 'LOPEZ'
    assert response.data.apellido_materno == 'OBRADOR'


def test_sync_fetch_curp_details():
    apimarket.assemble(async_client=False)
    response = apimarket.fetch_curp_details("LOOA531113HTCPBN07")
    assert response.data.apellido_paterno == 'LOPEZ'
    assert response.data.apellido_materno == 'OBRADOR'


def test_sync_calculate_rfc():
    apimarket.assemble(async_client=False)
    response = apimarket.calculate_rfc("Bryan Antonio", "Lopez", "Hernadez", "06", "06", 1997)
    rfc = response.additional_data['data']['rfc']
    validationCode = response.additional_data['codigoValidacion']
    assert rfc is not None
    print("RFC:", rfc)
    print("Codigo de Validación:", validationCode)


def test_idse_listar_certificados():
    apimarket.assemble(async_client=False)
    certificados = apimarket.idse_listar_certificados()
    assert certificados is not None
    assert len(certificados) > 0
    print("Total certificados:", len(certificados))
    print("Nombre:", certificados[0].name)
    print("RFC:", certificados[0].rfc)
    print("Vigente hasta:", certificados[0].valid_until)

