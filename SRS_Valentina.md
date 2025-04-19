# Tarea 2: SRS, Especificación de Requerimientos de Software

## Conectados: Servicios a un clic

## Requerimiento de negocio

Conectados es una plataforma web que tiene como objetivo facilitar la conexión entre personas que requieren servicios a domicilio (peluquería, electricidad, gasfitería, etc.) y profesionales que los ofrecen. Se busca mejorar la experiencia de búsqueda, contratación y evaluación de servicios, reduciendo la informalidad, aumentando la confianza y democratizando el acceso al mercado.

## Casos de Uso (UC)
Esta sección detalla los  10 casos de uso más importantes del sistema.

| ID   | Nombre del Caso de Uso         | Descripción                                                                                                              |
|------|:-------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| UC01 | Registro de usuario            | El usuario debe poder registrarse en la plataforma para acceder a los servicios en menos de 2 minutos.                   |
| UC02 | Registro de profesional        | El usuario prestador de servicios debe poder crear un perfil para ofrecer sus servicios con información verificada.             |
| UC03 | Publicación de servicios       | El usuario prestador de servicios debe poder publicar los servicios en su perfil incluyendo fotos, precios y descripciones.     |
| UC04 | Búsqueda de servicios          | El usuario consumidor debe poder buscar servicios usando filtros como categoría, ubicación y disponibilidad.                       |
| UC05 | Visualización de perfil        | El usuario consumidor debe poder visualizar el perfil del usuario prestador de servicios incluyendo reseñas y su portafolio de trabajos.   |
| UC06 | Agenda de citas                | El usuario consumidor debe poder agendar una cita según la disponibilidad del prestador mediante un calendario interactivo.        |
| UC07 | Chat interno                   | El usuario consumidor debe poder enviar mensajes directos al prestador de servicios para coordinar antes de agendar.               |
| UC08 | Valoración del servicio        | El usuario consumidor debe poder dejar una reseña y calificación tras recibir un servicio, reflejando su calidad.                  |
| UC09 | Notificaciones                 | El usuario consumidor debe poder recibir notificaciones en tiempo real sobre reservas, mensajes y cambios en la agenda.            |
| UC10 | Panel de gestión de servicios  | El usuario prestador de servicios debe poder gestionar sus reservas, disponibilidad y reseñas desde un panel personal.          |


## Requerimientos funcionales

- El sistema debe permitir el registro de usuarios consumidores y profesionales.

- El sistema debe permitir a los profesionales publicar y editar servicios.

- El sistema debe permitir a los usuarios buscar servicios por múltiples filtros.

- El sistema debe permitir agendar servicios según disponibilidad.

- El sistema debe permitir enviar y recibir mensajes entre usuarios consumidores y profesionales.

- El sistema debe permitir valorar y reseñar servicios.

- El sistema debe mostrar notificaciones importantes como confirmación de visita, mensajes, entre otros.

- El sistema debe contar con un panel de administración.

- El sistema debe mostrar la agenda y reservas a los profesionales.

- El sistema debe ofrecer un panel personal a cada tipo de usuario.

## Requerimientos no funcionales
Incluir aspectos como rendimiento, usabilidad, seguridad, escalabilidad, disponibilidad, etc.


|Tipo	|Requerimiento|
|:------:|:-------------------------------|
|Usabilidad|	Interfaz intuitiva y adaptada a móviles (diseño *responsive*).|
|Rendimiento	|Las búsquedas deben ejecutarse en menos de 3 segundos.|
|Seguridad	|Cifrado de contraseñas y validación de identidad.|
|Escalabilidad	|Soportar crecimiento de usuarios sin afectar rendimiento.|
|Disponibilidad	|El sistema debe estar disponible 99% del tiempo mensual.|
|Mantenibilidad	|El código debe ser modular y documentado.|

## Priorización de requerimientos

Usando el enfoque MoSCoW se detallan los requerimientos:

|Requerimiento|	Prioridad|
|:------|:-------------------------------|
|Registro de usuarios consumidores y profesionales|	Must have|
|Publicación de servicios|	Must have|
|Búsqueda con filtros|	Must have|
|Agendamiento|	Must have|
|Chat interno|	Should have|
|Valoraciones|	Must have|
|Notificaciones|	Should have|
|Panel de administración	|Should have|
|Diseño responsive|	Must have|

## Reglas de negocio
Las siguientes reglas definen restricciones y comportamientos específicos del sistema Conectados, alineados con su dominio de operación. Estas reglas garantizan un funcionamiento justo, seguro y transparente para usuarios y prestadores de servicios.

### Solo profesionales verificados pueden ser mostrados en los resultados de búsqueda.

Para asegurar la calidad y confiabilidad de los servicios, el sistema únicamente mostrará en los resultados de búsqueda a aquellos profesionales cuyo perfil haya sido verificado por el equipo de administración. La verificación puede incluir la validación de identidad, antecedentes y/o certificaciones dependiendo del tipo de servicio ofrecido.

### Cada profesional puede ofrecer múltiples servicios, pero deben estar categorizados.

Un profesional puede registrar más de un servicio en su perfil, pero debe asignar cada uno a una categoría específica predefinida (por ejemplo: peluquería, electricidad, jardinería). Esto permite mantener el sistema organizado y facilita la búsqueda por parte de los usuarios.

### Un usuario solo puede valorar un servicio si efectivamente fue realizado.

Para evitar valoraciones falsas o malintencionadas, el sistema permitirá que un usuario deje una reseña solo si el servicio fue efectivamente agendado y marcado como realizado por ambas partes. Esto garantiza reseñas auténticas y útiles para otros usuarios.

### El sistema bloquea horarios ya reservados para evitar sobreagendamiento.

Una vez que un usuario agenda un servicio con un profesional en un horario determinado, ese espacio se bloquea automáticamente en la agenda del profesional. Esto evita conflictos de horario y sobreagendamiento, asegurando una experiencia fluida y realista.

### Las denuncias de usuarios deben ocultar temporalmente el perfil hasta revisión.

Cuando un usuario presenta una denuncia sobre un profesional, el sistema ocultará temporalmente el perfil denunciado de los resultados de búsqueda. El equipo de administración deberá revisar la denuncia y tomar una decisión antes de reactivar o suspender permanentemente al prestador.

## Diagramas de la solución
Incluir al menos dos diagramas que ayuden a comprender mejor el sistema (por ejemplo: de conUC, casos de uso, flujo de datos, arquitectura, etc.)

Basarse en el enfoque propuesto en el Capítulo 12 de Wiegers.

Solo se evaluará diagramas que aporten valor a la solución.


## Supuestos

Esta sección detalla los supuestos realizados para completar esta especificación, debido a la falta de información completa en algunos aspectos del sistema:

- Se asume que todos los usuarios tienen acceso a un dispositivo con conexión a internet.

- Se asume que los profesionales son responsables de cumplir los horarios ofrecidos.

- Se asume que las tarifas están expresadas en la moneda local.

- Se asume que los profesionales son responsables de cumplir los horarios ofrecidos.

## Incluir una primera aproximación al plan de pruebas del sistema, que contemple:

¿Qué se va a probar?¿Qué no se va a probar?

Una clasificación inicial de los tipos de pruebas a realizar (pruebas funcionales, no funcionales, pruebas de integración, pruebas de aceptación, ¿se probará el backend, se probará el frontend?

Casos de prueba (listado): Listar casos de prueba básicos (solo enunciado) y vincularlos explícitamente con los requerimientos que validan.

### Se va a probar:

Registro, login, publicación, búsqueda, agendamiento, valoraciones.

### No se va a probar:

Integración con pasarelas de pago externas (no está contemplado en esta versión).

### Tipos de pruebas:

- Funcionales (alta prioridad).

- No funcionales (rendimiento, usabilidad).

- Pruebas de integración (backend-frontend).

- Pruebas de aceptación (validación por parte del cliente).

|CP | Caso de Prueba | Requerimiento vinculado|
|:------|:-------------------------------|:------:|
|CP1 | Verificar que un usuario pueda registrarse exitosamente | RF1|
|CP2 | Verificar que un profesional pueda publicar un servicio | RF2|
|CP3 | Verificar que la búsqueda por categoría muestre resultados correctos | RF3|
|CP4 | Verificar que se pueda agendar un servicio sin conflictos de horario | RF4|
|CP5 | Verificar que se pueda valorar un servicio completado | RF6|

