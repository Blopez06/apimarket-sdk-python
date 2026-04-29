Testing
=======

El proyecto usa **pytest** con dos tipos de tests: unitarios y de integración.
Todos los tests corren dentro de Docker para garantizar un entorno consistente.

----

Tipos de tests
--------------

**Unitarios**
  No requieren conexión a ningún servicio externo. Verifican que las validaciones
  de datos se disparen correctamente antes de cualquier llamada a la API.
  Se pueden correr en cualquier momento sin configuración adicional.

**Integración** (marcados con ``@pytest.mark.integracion``)
  Llaman a las APIs reales. Requieren una API key válida configurada en el entorno.

----

Configuración
-------------

Crea un archivo ``.env`` en la raíz del proyecto con las variables necesarias:

.. code-block:: bash

    APIMARKET_API_KEY=tu_api_key_aqui

    # Solo requeridas para tests de IDSE Pro
    IDSEPRO_BEARER_TOKEN=tu_bearer_token
    IDSEPRO_API_KEY=tu_api_key_idse

Para correr en modo sandbox (sin consumir créditos reales):

.. code-block:: bash

    APIMARKET_SANDBOX=true

----

Ejecutar tests
--------------

**Solo unitarios** (sin API key, sin conexión):

.. code-block:: bash

    docker-compose run --rm sdk-app pytest -m "not integracion"

**Solo integración** (requiere API key):

.. code-block:: bash

    docker-compose run --rm sdk-app pytest -m integracion

**Todos los tests**:

.. code-block:: bash

    docker-compose run --rm sdk-app pytest

**Un archivo específico**:

.. code-block:: bash

    docker-compose run --rm sdk-app pytest tests/validations/test_curp.py

**Un test específico**:

.. code-block:: bash

    docker-compose run --rm sdk-app pytest tests/validations/test_curp.py::TestValidateCurp::test_valid_curp

----

Estructura de tests
-------------------

.. code-block:: text

    tests/
    ├── conftest.py              # fixtures compartidos (sdk, sdk_async)
    ├── validations/
    │   ├── test_curp.py         # validaciones de CURP
    │   ├── test_rfc.py          # validaciones de RFC
    │   └── test_nss.py          # validaciones de NSS
    ├── renapo/
    │   ├── test_validar_curp.py # unitarios + integración
    │   └── test_obtener_curp.py # integración
    ├── sat/
    │   └── test_calcular_rfc.py # integración
    ├── imss/
    │   └── test_idse_pro.py     # integración
    ├── sep/                     # pendiente
    ├── infonavit/               # pendiente
    ├── administracion/          # pendiente
    └── repuve/                  # pendiente

----

Fixtures disponibles
--------------------

Definidos en ``tests/conftest.py`` y disponibles en todos los tests:

``sdk``
  Configura el SDK para llamadas síncronas. Usar en tests de integración normales.

  .. code-block:: python

      def test_algo(self, sdk):
          response = apimarket.fetch_curp_details("LOOA531113HTCPBN07")

``sdk_async``
  Configura el SDK para llamadas asíncronas. Usar junto con ``@pytest.mark.anyio``.

  .. code-block:: python

      @pytest.mark.anyio
      async def test_algo_async(sdk_async):
          response = await apimarket.fetch_curp_details("LOOA531113HTCPBN07")

----

Convenciones
------------

- Los tests unitarios no usan fixtures ni markers especiales.
- Los tests de integración siempre llevan ``@pytest.mark.integracion`` y el fixture ``sdk``.
- Usar ``@pytest.mark.parametrize`` para colecciones de datos de prueba.
- Los datos de prueba (CURPs, NSS, RFC) son fijos y conocidos — nunca dinámicos.
