Error Catalog
=============

Catálogo de todos los códigos de error que puede lanzar el SDK durante la validación de datos.
Cada excepción lleva un código único, un mensaje descriptivo en español y el valor del campo que causó el error.

El código vive anidado dentro de la excepción correspondiente, por lo que solo necesitas un import para acceder a ambos.

----

Estructura de una excepción
----------------------------

Todas las excepciones de validación comparten la misma estructura:

.. code-block:: python

   exception.code          # miembro del Enum interno (ej. InvalidCURPError.Code.INVALID_LENGTH)
   exception.code.value    # string del código  (ej. "INVALID_CURP_LENGTH")
   exception.message       # mensaje en español (ej. "Longitud inválida...")
   str(exception)          # "[INVALID_CURP_LENGTH] CURP: LOOA53 - Longitud inválida..."

----

CURP — ``InvalidCURPError``
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 28 50

   * - Código
     - ``InvalidCURPError.Code``
     - Descripción
   * - ``INVALID_CURP_LENGTH``
     - ``INVALID_LENGTH``
     - El CURP no tiene exactamente 18 caracteres.
   * - ``INVALID_CURP_FORMAT``
     - ``INVALID_FORMAT``
     - El CURP no cumple el patrón oficial: letra vocal, consonantes, fecha (AAMMDD), sexo (H/M/X), clave de entidad y consonantes internas.
   * - ``INVALID_CURP_DIGIT``
     - ``INVALID_DIGIT``
     - El dígito verificador (posición 18) no corresponde al cálculo oficial del SAT. Por seguridad no se indica el valor correcto.

----

RFC — ``InvalidRFCError``
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 28 50

   * - Código
     - ``InvalidRFCError.Code``
     - Descripción
   * - ``INVALID_RFC_FORMAT``
     - ``INVALID_FORMAT``
     - El RFC no cumple el patrón de persona física (4 letras + 6 dígitos + 3 alfanuméricos) ni el de persona moral (3 letras + 6 dígitos + 3 alfanuméricos). Solo se aceptan mayúsculas.

----

NSS — ``InvalidNSSError``
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 28 50

   * - Código
     - ``InvalidNSSError.Code``
     - Descripción
   * - ``INVALID_NSS_LENGTH``
     - ``INVALID_LENGTH``
     - El NSS no tiene exactamente 11 dígitos.
   * - ``INVALID_NSS_FORMAT``
     - ``INVALID_FORMAT``
     - El NSS contiene caracteres no numéricos.
   * - ``INVALID_NSS_DIGIT``
     - ``INVALID_DIGIT``
     - El dígito verificador (posición 11) no corresponde al cálculo del algoritmo IMSS (Luhn modificado).

----

Fecha de nacimiento — ``InvalidBirthDateError``
------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 28 50

   * - Código
     - ``InvalidBirthDateError.Code``
     - Descripción
   * - ``INVALID_BIRTH_DAY_FORMAT``
     - ``INVALID_BIRTH_DAY_FORMAT``
     - El día de nacimiento no tiene al menos 2 dígitos numéricos (ej. ``'06'``).
   * - ``INVALID_BIRTH_MONTH_FORMAT``
     - ``INVALID_BIRTH_MONTH_FORMAT``
     - El mes de nacimiento no tiene al menos 2 dígitos numéricos (ej. ``'06'``).
   * - ``INVALID_BIRTH_YEAR_FORMAT``
     - ``INVALID_BIRTH_YEAR_FORMAT``
     - El año de nacimiento no tiene al menos 4 dígitos numéricos (ej. ``'1990'``).

----

Folio UUID — ``InvalidFolioError``
------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 28 50

   * - Código
     - ``InvalidFolioError.Code``
     - Descripción
   * - ``INVALID_FOLIO_FORMAT``
     - ``INVALID_FORMAT``
     - El folio no tiene formato UUID válido (``xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx``). Solo se aceptan dígitos hexadecimales separados por guiones en las posiciones requeridas.

----

Ejemplos de uso
---------------

Capturar y leer el código de error:

.. code-block:: python

   from apimarket.validations import validate_curp, InvalidCURPError

   try:
       validate_curp("INVALIDO")
   except InvalidCURPError as e:
       print(e.code.value)   # "INVALID_CURP_LENGTH"
       print(e.message)      # "Longitud inválida: se esperaban 18 caracteres, se recibieron 8."
       print(str(e))         # "[INVALID_CURP_LENGTH] CURP: INVALIDO - Longitud inválida..."

Comparar el código para manejar cada caso:

.. code-block:: python

   from apimarket.validations import validate_curp, InvalidCURPError

   try:
       validate_curp(curp)
   except InvalidCURPError as e:
       if e.code == InvalidCURPError.Code.INVALID_LENGTH:
           print("El CURP debe tener 18 caracteres.")
       elif e.code == InvalidCURPError.Code.INVALID_FORMAT:
           print("El formato del CURP no es válido.")
       elif e.code == InvalidCURPError.Code.INVALID_DIGIT:
           print(f"Dígito verificador incorrecto: {e.message}")

El mismo patrón aplica para ``InvalidRFCError`` e ``InvalidNSSError``:

.. code-block:: python

   from apimarket.validations import validate_rfc, InvalidRFCError
   from apimarket.validations import validate_nss, InvalidNSSError

   try:
       validate_rfc(rfc)
   except InvalidRFCError as e:
       if e.code == InvalidRFCError.Code.INVALID_FORMAT:
           print("El RFC no tiene el formato correcto.")

   try:
       validate_nss(nss)
   except InvalidNSSError as e:
       if e.code == InvalidNSSError.Code.INVALID_DIGIT:
           print("El dígito verificador del NSS es incorrecto.")

----

Resumen de códigos
------------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Código
     - Excepción
     - Causa
   * - ``INVALID_CURP_LENGTH``
     - ``InvalidCURPError``
     - Longitud distinta a 18 caracteres
   * - ``INVALID_CURP_FORMAT``
     - ``InvalidCURPError``
     - Formato no válido
   * - ``INVALID_CURP_DIGIT``
     - ``InvalidCURPError``
     - Dígito verificador incorrecto
   * - ``INVALID_RFC_FORMAT``
     - ``InvalidRFCError``
     - Formato no válido
   * - ``INVALID_NSS_LENGTH``
     - ``InvalidNSSError``
     - Longitud distinta a 11 dígitos
   * - ``INVALID_NSS_FORMAT``
     - ``InvalidNSSError``
     - Contiene caracteres no numéricos
   * - ``INVALID_NSS_DIGIT``
     - ``InvalidNSSError``
     - Dígito verificador incorrecto
   * - ``INVALID_FOLIO_FORMAT``
     - ``InvalidFolioError``
     - Formato UUID inválido
   * - ``INVALID_BIRTH_DAY_FORMAT``
     - ``InvalidBirthDateError``
     - Día de nacimiento sin formato de 2 dígitos
   * - ``INVALID_BIRTH_MONTH_FORMAT``
     - ``InvalidBirthDateError``
     - Mes de nacimiento sin formato de 2 dígitos
   * - ``INVALID_BIRTH_YEAR_FORMAT``
     - ``InvalidBirthDateError``
     - Año de nacimiento sin formato de 4 dígitos
