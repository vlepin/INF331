# SHOPpy: Tienda Virtual

## Descripción

´shop.py´ es un programa en Python que permite gestionar una tienda virtual de manera sencilla. Con esta herramienta, puedes agregar productos al inventario, procesar compras y generar reportes de ventas. Es ideal para pequeños negocios o para gestionar listas de compras personales.

## Instalación

El programa no requiere una instalación, pero se necesita instalar [Python3](https://www.python.org/downloads/) para su ejecución.

Además, es necesario instalar los siguientes paquetes:

- [cryptography](https://cryptography.io/en/latest/)
- [sentry-sdk](https://sentry.io/welcome/?utm_source=google&utm_medium=cpc&utm_id={9657410528}&utm_campaign=Google_Search_Brand_ROW_Alpha&utm_content=g&utm_term=sentry%20sdk&gad_source=1&gclid=CjwKCAjw7pO_BhAlEiwA4pMQvOBaVjZIkHbEbNfxoyTAJPKcVF7teZ0wSGC7pklqElNDL6DIMXVX-xoCwzIQAvD_BwE)

Si deseas instalarlos manualmente, puedes ejecutar:

> pip install -r requirements.txt >

## Cómo usar

Para ejecutar el programa, abre una terminal o consola y escribe:

> python shop.py >

Al iniciar, el programa solicita registrarse (´1´) o iniciar sesión (´2´). Si no deseas registrarte, puedes usar las siguientes credenciales predeterminadas::

- Usuario: ´Admin´

- Contraseña: ´123´

Posteriormente se abre un menú con diferentes opciones para gestionar la tienda. Para acceder a una función basta con ingresar su número en la consola según se solicite. Las funciones y su respectivo uso se describen a continuación:

- **1. Agregar producto**

Permite agregar productos al inventario ingresando los siguientes datos: `Nombre`, `Descripción`, `Unidades disponibles`, `Precio unitario` y `Categoría`.

- **2. Consultar lista de productos**

Muestra la lista de productos ingresados, incluyendo aquellos sin stock, en el orden en que fueron agregados junto con su índice.

- **3. Buscar y filtrar productos**

Se puede buscar un producto por nombre y aplicar filtros por `Categoría` y `Rango de precios`. Si se desea omitir algún filtro, basta con presionar `Enter`.

- **4. Gestionar stock**

Permite actualizar la cantidad de unidades disponibles de un producto ingresando su índice y el nuevo valor.

- **5. Eliminar producto**

Permite eliminar un producto del inventario ingresando su índice.

- **6. Generar reporte de inventario**

Genera un informe en el archivo `reporte_inventario.txt` con la fecha de emisión, la lista de productos en stock, el valor total del inventario y los productos sin stock.

- **7. Salir**

Finaliza la ejecución del programa y cierra la sesión.

## Cómo contribuir

Para contribuir a este proyecto, se recomienda seguir el flujo de trabajo ["fork and pull request"](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project).

## Licencia

Este proyecto está bajo la licencia MIT. Puedes consultar más detalles en el archivo [LICENSE](https://github.com/vlepin/INF331/blob/Tarea_1/LICENSE) .


