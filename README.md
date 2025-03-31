# SHOPpy

## Descripción

El programa ´shop.py´ permite gestionar una tienda virtual de manera sencilla. Con esta herramienta, puedes agregar productos al inventario, procesar compras y generar reportes de ventas. Es ideal para pequeños negocios o para gestionar listas de compras personales.

## Instalación

El programa no requiere una instalación, pero se necesita instalar [Python3](https://www.python.org/downloads/) para su ejecución.

Además, es necesario instalar los siguientes paquetes:

- [cryptography](https://cryptography.io/en/latest/)
- [sentry-sdk](https://sentry.io/welcome/?utm_source=google&utm_medium=cpc&utm_id={9657410528}&utm_campaign=Google_Search_Brand_ROW_Alpha&utm_content=g&utm_term=sentry%20sdk&gad_source=1&gclid=CjwKCAjw7pO_BhAlEiwA4pMQvOBaVjZIkHbEbNfxoyTAJPKcVF7teZ0wSGC7pklqElNDL6DIMXVX-xoCwzIQAvD_BwE)

Si deseas instalarlos manualmente, puedes ejecutar:

> pip install -r requirements.txt >

## Cómo usar

Para ejecutar el programa, simplemente abre una terminal o consola y escribe:

> python shop.py >

El programa comenzará solicitando registrarse (ingresar 1) o iniciar sesión (ingresar 2), si no desea registrarse puede ingresar las credenciales disponibles a continuación:

>Admin #Usuario>

>123 #Contraseña>

Posteriormente se abre un menú con diferentes opciones para gestionar la tienda. Para acceder a una función basta con ingresar su número en la consola según se solicite. Las funciones y su respectivo uso se describen a continuación:

- **1. Agregar producto**

Agrega un producto al inventario, para ello se deben rellenar los campos: `Nombre`, `Descripción`, `Unidades disponibles`, `Precio unitario` y `Categoría`.

- **2. Consultar lista de productos**

Entrega la lista de los productos ingresados (incluso si no tienen stock), y se muestran en el orden en que fueron ingresados con su respectivo índice.

- **3. Buscar y filtrar productos**

Si se desea omitir alguna de las opciones oprimir `Enter`.

Primero pide el nombre del producto para buscar. Y después comienza la opción de filtrado de productos por `Categoría` y un rango de precios.

- **4. Gestionar stock**

Se selecciona el número de índice del producto cuyo stock se desea modificar, después se ingresa la cantidad actualizada del producto y se actualiza en el inventario.

- **5. Eliminar producto**

Elimina un producto del inventario, se ingresa su índice y se actualiza el inventario.

- **6. Generar reporte de inventario**

Modifica el archivo `reporte_inventario.txt` ingresando un resumen con el total de productos en inventario, el valor total del inventario y los productos agotados.

- **7. Salir**

Cierra la sesión.

## Cómo contribuir

La manera recomendada de realizar contribuciones a este proyecto es a traves del flujo de trabajo ["fork and pull request"](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project).

## Licencia

Este proyecto está bajo la licencia MIT. Puedes consultar el archivo [LICENSE](https://github.com/vlepin/INF331/blob/Tarea_1/LICENSE) para más detalles.
