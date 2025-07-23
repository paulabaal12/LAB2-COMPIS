## Cambios y Análisis LAB 2 | COMPILADORES

### 1. Implementación de Visitor y Listener
Se desarrollaron ambos enfoques de recorrido de árbol sintáctico (Visitor y Listener) para el análisis semántico y la validación de tipos en el lenguaje definido con ANTLR. Se presentan ejemplos de ejecución utilizando los controladores `Driver.py` y `DriverListener.py`, demostrando la correcta integración y funcionamiento de ambas estrategias.

### 2. Ejecución y Análisis de Archivos de Prueba
Se realizaron pruebas con los archivos proporcionados:

- **program_test_pass.txt:**
  - Todas las operaciones aritméticas se efectúan entre tipos compatibles (`int`, `float`).
  - Las comparaciones (`>`, `<`) se realizan entre valores numéricos, retornando resultados booleanos válidos.
  - La operación lógica AND (`&&`) se aplica correctamente entre valores booleanos.
  - No se presentan divisiones por cero ni usos incorrectos de los operadores módulo (`%`) y potencia (`^`).
  - No existen variables no declaradas ni errores de sintaxis.
  - El sistema valida exitosamente el archivo, confirmando la robustez de las reglas implementadas.

- **program_test_no_pass.txt:**
  - Se detectan intentos de operar entre tipos incompatibles (por ejemplo, `int + string`).
  - Se identifica y reporta la división por cero como error específico.
  - El uso del operador módulo (`%`) con valores de tipo `float` es correctamente rechazado.
  - La potencia (`^`) aplicada a valores de tipo `string` o `bool` genera el error correspondiente.
  - Las comparaciones entre tipos no numéricos (por ejemplo, `string > int`) son invalidadas.
  - La operación lógica AND (`&&`) utilizada con tipos distintos a `bool` es reportada como conflicto.
  - Todos los errores son informados de manera clara y específica, facilitando la identificación y corrección de los problemas.

### 3. Extensión de la Gramática ANTLR
Se amplió la gramática del lenguaje para soportar nuevas operaciones:
  - Módulo (`%`) para obtener el residuo de divisiones entre enteros.
  - Potencia (`^`) para realizar exponentiación.
  - Comparaciones (`>`, `<`) para evaluar relaciones numéricas.
  - Operación lógica AND (`&&`) para conjunciones booleanas.
El archivo `SimpleLang.g4` fue modificado y los artefactos de ANTLR fueron regenerados para reflejar estos cambios.

### 4. Extensión del Sistema de Tipos
El sistema de tipos fue fortalecido para validar múltiples conflictos y errores:
  - Las operaciones aritméticas solo se permiten entre valores numéricos (`int`, `float`).
  - La división por cero es detectada y reportada oportunamente.
  - El operador módulo (`%`) se restringe a valores enteros.
  - El operador potencia (`^`) no acepta valores de tipo `string` ni `bool`.
  - Las comparaciones (`>`, `<`) se limitan a valores numéricos.
  - La operación lógica AND (`&&`) se restringe a valores booleanos.
  - Se detecta y reporta el uso de variables no declaradas.
  - Todos los errores se comunican con mensajes claros y precisos, optimizando el proceso de depuración y corrección.
