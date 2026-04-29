CLI Reference
=============

Referencia completa de todos los comandos disponibles en el CLI de API Market.

Uso general::

    apimarket [GRUPO] [OPCIONES]

Para ver todos los comandos disponibles::

    apimarket --help

Para ver la versión instalada::

    apimarket --version

----

RENAPO
------

**-vc / --validate-curp** ``CURP``

Valida un CURP contra el padrón de RENAPO y retorna los datos personales registrados.

.. code-block:: bash

    apimarket -vc LOOA531113HTCPBN07

----

**-cc / --calculate-curp** ``NOMBRES PATERNO MATERNO DIA MES AÑO ENTIDAD SEXO``

Obtiene el CURP a partir de datos personales.

.. code-block:: bash

    apimarket -cc "JUAN CARLOS" GARCIA MARTINEZ 15 03 1990 09 H

Valores válidos para ``SEXO``: ``H`` (hombre), ``M`` (mujer), ``X`` (no binario).

Valores válidos para ``ENTIDAD``: clave de 2 dígitos del estado de nacimiento (ej. ``09`` para CDMX).

----

SAT
---

**-ro / --get-rfc** ``CURP``

Obtiene el RFC a partir de un CURP.

.. code-block:: bash

    apimarket -ro LOOA531113HTCPBN07

----

**-cr / --calculate-rfc** ``NOMBRES PATERNO MATERNO DIA MES AÑO``

Calcula el RFC a partir de datos personales.

.. code-block:: bash

    apimarket -cr "BRYAN ANTONIO" LOPEZ HERNANDEZ 06 06 1997

----

**-vs / --validate-sat** ``NOMBRE RFC REGIMEN CP``

Valida datos fiscales en el SAT.

.. code-block:: bash

    apimarket -vs "NOMBRE COMPLETO" LOHB970606P42 601 06600

----

**-df / --fiscal-data** ``RFC``

Obtiene datos fiscales registrados en el SAT por RFC.

.. code-block:: bash

    apimarket -df LOHB970606P42

----

IMSS
----

**-lu / --locate-umf** ``CP``

Localiza la UMF (Unidad de Medicina Familiar) correspondiente a un código postal.

.. code-block:: bash

    apimarket -lu 06600

----

**-ln / --locate-nss** ``CURP``

Localiza el NSS (Número de Seguridad Social) a partir de un CURP.

.. code-block:: bash

    apimarket -ln LOOA531113HTCPBN07

----

**-vi / --check-validity** ``NSS CURP``

Verifica la vigencia de derechos IMSS con NSS y CURP.

.. code-block:: bash

    apimarket -vi 12345678952 LOOA531113HTCPBN07

----

**-cl / --get-clinic** ``CURP``

Obtiene la clínica IMSS asignada a partir de un CURP.

.. code-block:: bash

    apimarket -cl LOOA531113HTCPBN07

----

**-hl / --labor-history** ``CURP NSS``

Consulta el historial laboral registrado en el IMSS.

.. code-block:: bash

    apimarket -hl LOOA531113HTCPBN07 12345678952

----

SEP
---

**-ce / --validate-cedula** ``CEDULA``

Valida una cédula profesional en la SEP.

.. code-block:: bash

    apimarket -ce 1234567

----

**-vr / --validate-certificate** ``FOLIO``

Valida un certificado de estudios por folio.

.. code-block:: bash

    apimarket -vr FOLIO123

----

**-oc / --get-cedula** ``NOMBRES PATERNO MATERNO``

Busca cédulas profesionales por datos personales.

.. code-block:: bash

    apimarket -oc "JUAN CARLOS" GARCIA MARTINEZ

----

INFONAVIT
---------

**-bc / --search-credit** ``NSS``

Busca crédito INFONAVIT asociado a un NSS.

.. code-block:: bash

    apimarket -bc 12345678952

----

**-si / --infonavit-subaccount** ``NSS``

Obtiene el saldo de la subcuenta de vivienda INFONAVIT.

.. code-block:: bash

    apimarket -si 12345678952

----

IDSE Pro
--------

**-lc / --list-certificates**

Lista los certificados digitales disponibles en IDSE Pro.
Requiere ``IDSEPRO_BEARER_TOKEN`` e ``IDSEPRO_API_KEY`` configurados.

.. code-block:: bash

    apimarket -lc

----

Cuenta
------

**-pm / --permissions**

Muestra los permisos asociados a la cuenta y API key activa.

.. code-block:: bash

    apimarket -pm

----

**-gt / --store-token** ``NOMBRE EMPRESA DESCRIPCION PERMISOS RFC CIEC``

Crea y guarda un nuevo token en la cuenta. ``PERMISOS`` es una lista separada por comas.

.. code-block:: bash

    apimarket -gt "Mi Token" "Mi Empresa" "Descripcion" "permiso1,permiso2" LOHB970606P42 ciec123

----

Manejo de errores
-----------------

Cuando los datos de entrada no pasan la validación, el CLI retorna un mensaje de error
con el código correspondiente y sale con código 1:

.. code-block:: bash

    $ apimarket -vc INVALIDA
    Error [INVALID_CURP_01]: Longitud inválida: se esperaban 18 caracteres, se recibieron 8.

    $ apimarket -vc 123456789012345678
    Error [INVALID_CURP_02]: El formato del CURP es inválido.

    $ apimarket -vc LOOA531113HTCPBN09
    Error [INVALID_CURP_03]: Dígito verificador inválido.

Para el catálogo completo de códigos de error ver :doc:`error_catalog`.
