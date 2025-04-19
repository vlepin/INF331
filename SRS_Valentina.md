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

## Requerimientos Funcionales

| ID   | Requerimiento Funcional                                                                 |
|:-----:|:-----------------------------------------------------------------------------------------|
| RF1  | El sistema debe permitir el registro de usuarios consumidores y profesionales.          |
| RF2  | El sistema debe permitir a los profesionales publicar y editar servicios.               |
| RF3  | El sistema debe permitir a los usuarios clientes buscar servicios por múltiples filtros.|
| RF4  | El sistema debe permitir agendar servicios según disponibilidad.                        |
| RF5  | El sistema debe permitir enviar y recibir mensajes entre usuarios clientes y profesionales.|
| RF6  | El sistema debe permitir valorar y reseñar servicios.                                   |
| RF7  | El sistema debe mostrar notificaciones importantes como confirmación de visita, mensajes, entre otros.|
| RF8  | El sistema debe contar con un panel de administración.                                  |
| RF9  | El sistema debe mostrar la agenda y reservas a los profesionales.                       |
| RF10 | El sistema debe ofrecer un panel personal a cada tipo de usuario.                       |

## Requerimientos No Funcionales

| ID   | Tipo           | Requerimiento                                                                 |
|:-----:|:---------------|:------------------------------------------------------------------------------|
| RNF1 | Usabilidad      | Interfaz intuitiva y adaptada a móviles (diseño *responsive*).               |
| RNF2 | Rendimiento     | Las búsquedas deben ejecutarse en menos de 3 segundos.                       |
| RNF3 | Seguridad       | Cifrado de contraseñas y validación de identidad.                            |
| RNF4 | Escalabilidad   | Soportar crecimiento de usuarios sin afectar rendimiento.                    |
| RNF5 | Disponibilidad  | El sistema debe estar disponible 99% del tiempo mensual.                     |
| RNF6 | Mantenibilidad  | El código debe ser modular y documentado.                                    |
| RNF7 | Accesibilidad   | El sistema debe cumplir con estándares de accesibilidad WCAG 2.1 nivel AA.   |

## Priorización de Requerimientos

Usando el enfoque **MoSCoW**, se detallan los requerimientos a continuación:

| ID   | Requerimiento                                                  | Prioridad     |
|:----:|:----------------------------------------------------------------|:--------------|
| RF1  | Registro de usuarios consumidores y profesionales              | Must have     |
| RF2  | Publicación y edición de servicios por profesionales           | Must have     |
| RF3  | Búsqueda de servicios por múltiples filtros                    | Must have     |
| RF4  | Agendamiento de servicios según disponibilidad                 | Must have     |
| RF5  | Envío y recepción de mensajes entre clientes y profesionales   | Should have   |
| RF6  | Valoración y reseña de servicios                               | Must have     |
| RF7  | Notificaciones importantes (confirmaciones, mensajes, etc.)    | Should have   |
| RF8  | Panel de administración                                        | Should have   |
| RF9  | Visualización de agenda y reservas para profesionales          | Should have   |
| RF10 | Panel personal para cada tipo de usuario                       | Must have     |
| RNF1 | Interfaz intuitiva y adaptada a móviles (*responsive*)         | Must have     |
| RNF2 | Búsquedas ejecutadas en menos de 3 segundos                    | Must have     |
| RNF3 | Cifrado de contraseñas y validación de identidad               | Must have     |
| RNF4 | Escalabilidad sin afectar rendimiento                          | Should have   |
| RNF5 | Disponibilidad del sistema 99% del tiempo mensual              | Should have   |
| RNF6 | Código modular y documentado                                   | Could have    |
| RNF7 | Cumplimiento de estándares de accesibilidad WCAG 2.1 nivel AA | Could have    |


## Reglas de negocio
Las siguientes reglas definen restricciones y comportamientos específicos del sistema Conectados, alineados con su dominio de operación. Estas reglas garantizan un funcionamiento justo, seguro y transparente para usuarios tanto clientes como prestadores de servicios.

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

## Plan de pruebas del sistema

A continuación, se presenta una primera aproximación al plan de pruebas del sistema, que contempla los elementos clave a validar, las exclusiones, la clasificación de pruebas y un listado básico de casos de prueba vinculados a requerimientos funcionales.

### Se va a probar:

Funcionalidades principales del sistema:

- Registro de usuarios.

- Inicio de sesión.

- Publicación de servicios por parte de profesionales.

- Búsqueda de servicios por categoría o nombre.

- Agendamiento de citas con validación de horarios disponibles.

- Valoración de servicios finalizados.

### No se va a probar:

- Integración con pasarelas de pago externas (no se contempla).

- Procesos automáticos de verificación de identidad profesional (se asume como externo).

- Notificaciones por canales externos como correo electrónico o SMS (de momento).

### Tipos de pruebas:

- Pruebas funcionales: Verifican que las funciones del sistema cumplan con los requerimientos definidos. Alta prioridad.

- Pruebas no funcionales: Evalúan aspectos como rendimiento del sistema y usabilidad de la interfaz.

- Pruebas de integración: Validan la correcta comunicación entre frontend y backend.

- Pruebas de aceptación: Validación final del sistema por parte del cliente o usuario final.

| CP  | Caso de Prueba                                                           | Requerimiento vinculado |
|:---:|:-------------------------------------------------------------------------|:------------------------:|
| CP1 | Verificar que un usuario pueda registrarse exitosamente                 | RF1                     |
| CP2 | Verificar que un usuario pueda iniciar sesión correctamente             | RF1                     |
| CP3 | Verificar que un profesional pueda publicar y editar un servicio        | RF2                     |
| CP4 | Verificar que la búsqueda por categoría o nombre arroje resultados      | RF3                     |
| CP5 | Verificar que se pueda agendar un servicio sin conflictos de horario    | RF4                     |
| CP6 | Verificar que un usuario pueda valorar un servicio completado           | RF6                     |
| CP7 | Verificar que los mensajes puedan enviarse y recibirse correctamente    | RF5                     |
| CP8 | Verificar que las notificaciones se muestren en el sistema              | RF7                     |
