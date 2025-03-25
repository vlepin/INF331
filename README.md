# INF331 Tarea 1

1) Requerimiento

Un emprendedor nos ha solicitado una aplicación sencilla para gestionar su inventario de productos en la bodega de su negocio. Nos ha dicho que, con tanta tecnología, necesita algo práctico y funcional.

**Requerimientos:**

- CRUD de Productos: Permitir a los usuarios agregar, consultar, actualizar y eliminar productos del inventario. Cada producto debe tener un nombre, descripción, cantidad disponible, precio unitario y categoría (por ejemplo, "Electrónica", "Ropa", "Alimentos", etc.).
- Gestión de Stock: Permitir actualizar la cantidad de productos cuando se vendan o se reciban nuevas unidades.
- Filtrado y Búsqueda
- Generación de Reportes: Mostrar un resumen con el total de productos en inventario, el valor total del inventario y los productos agotados.
- Autenticación: Proteger el acceso con un sistema de autenticación por nombre de usuario y contraseña.

2) Tarea

Evidentemente el requisito está incompleto, por lo que será su labor completarlo, para poder construir una solución sin ambigüedades, puede hacer preguntas en el foro de la semana y también hacer supuestos.

Preparar entregable (en Github) que especifique requerimiento, y que considere de manera explícita los siguientes puntos: / 25pts

- ¿Cómo especificarías mejor el requerimiento? (Validación)
- ¿Cómo asegurarías que el programa cumpla el requerimiento? (Verificación)
- Organización, explicar cómo se organizó el proyecto y el flujo de trabajo de éste.
- Incluir evidencia de flujo de trabajo y configuraciones realizadas (Imágenes de pantalla).
- Problemas encontrados y como se solucionaron.

Importante:
- Utiliza los conceptos de Validación y Verificación
- Incluir portada de documento y en esta agregar enlace a repositorio
- Escribir programa / 25pts
- Pruebas / 25pts
- Aspectos formales / 25pts

Preguntas de la tarea En foro de la semana
- Hasta miércoles 26 de marzo a las 23:59hrs
  
Fecha de entrega
- miércoles 2 de abril de 2025, 23:59
  
3) Detalle tarea

3.1) Aspectos formales

- Analizar y diseñar requerimiento en conjunto
- Cada equipo organizará y diseñará su proyecto, de acuerdo sus propios criterios
  
Ejemplo: 

Cada estudiante podría construir un módulo de la aplicación, etc...

- La organización y diseño que escojan tendrá impacto sobre su proceso de desarrollo de software, la administración del código, entre otros. Poner atención en este punto, ¿por qué? porque esto tiene impacto por ejemplo en las revisiones de código

- Deberá crear un espacio de trabajo propio en Slack.
- Se deberá integrar GitHub con Slack y configurar visualización en Slack de al menos:
New commits,
New pull requests,
Merges

Flujo de administración del código fuente (enlaces GIT)
- Seleccionar un paradigma para administrar los fuentes, explicar y justificar el ¿por qué de su elección?
- Definir aspectos mínimos de administración:
- Protección de ramas
- Revisores/aprobadores 
- Etc
  
3.2) Codificación

- Programación en Java o Python
- Controlar excepciones (documento de ayuda en aula)
- Logs

**Alternativa 1: Configurar logs propios: La aplicación debe generar "Logs" de las operaciones, en el caso de Java usar Log4J. Ver referencia de manejo de logs**

Ejemplo “muy referencial” (01/04/2025):

23:52:27 Info: envío mensaje

23:52:30 Info: envío mensaje

23.52.31 Warning: No se logro realizar envío

Dejar excepciones en log

**Alternativa 2: Usar Sentry.io**

Crear "Readme", que incluya:

Nombre

Descripción

Instalación

Cómo usar

Cómo contribuir

Licencia

(Se pueden seguir las sugerencias de GitHub)

Usar formato markdown. Ver referencia.

3.3) Pruebas

- Definir estrategia de pruebas: ¿Cómo vamos a probar? ¿Quién prueba qué? ¿haremos pruebas cruzadas?
- Definición de pruebas, según definición preparada en conjunto (puntos 1 y 2 de documento), cada prueba debe considerar, por ejemplo:
- Id_Test: Identificador de prueba
- Entrada al sistema: Entrada a la que se someterá el sistema o descripción de la prueba
- Resultado Esperado: Resultado que se espera, al ingresar al sistema a una determinada entrada
- Resultado Obtenido: Resultado obtenido al ingresar al sistema una determinada prueba
- Fallo o éxito: Éxito en caso de que resultado esperado sea igual a resultado obtenido, fallo en otro caso
- Cometario adicional: Comentario adicional asociado a la prueba, en caso de ser necesario
- Preparación y ejecución de Pruebas:
- Ciclo de pruebas 1 (Primera ejecución de conjunto de pruebas):
- Preparar conjunto de pruebas de manera individual
- Ejecutar de manera individual sobre programa(s)
- Ciclo de pruebas 2 (Segunda ejecución de conjunto de pruebas):
- Consolidar con compañero un único conjunto de pruebas y ejecutar en conjunto de pruebas consolidadas a programa(s)
- Ciclo de pruebas 3 (Solo en caso de ser necesario):
- Registrar pruebas en archivo adjunto.
  
4) Entregables

- Enlace a repositorio, en el repositorio debe estar todo lo anterior solicitado.
- Registro de pruebas:
- Alternativa 1: Crear cuenta en app.greentest.ai y dejar registro de las pruebas
- Alternativa 2: Excel: Suite de casos (adjunto): 
- Entregar un único archivo Excel, consolidar todo en un ÚNICO archivo (ciclos 1, 2, ... en un único archivo)
- Los dos integrantes del grupo puedes subir el mismo archivo
- 10 puntos adicionales por reportar, experiencia de uso, fallos o problemas operativos en Greentest.ai
