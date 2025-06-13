## Link (Github Pages): ???

# Tarea 3

### Consideraciones:
- No se dedicó tiempo a mejorar los estilos.
- Cada vista permite volver a la portada.

### Vistas:

#### **Portada:**
- El menú está planteado como una lista de enlaces.
- Se muestran la últimas 5 actividades segun su fecha de inicio.

#### **Agregar Actividad:**
- La confirmación del formulario aparece en un modal.
- Si el formulario se envía correctamente, se muestra un mensaje de confirmación y la página se redirige a la portada.
- Si el usuario presiona "No, no estoy seguro...", el modal se cierra y se muestra nuevamente el formulario en el estado en el que estaba trabajando.

#### **Listado de Actividades:**
- Se muestran las actividades agregadas en distintas páginas, con un maximo de 5 por cada una de ellas, las cuales uno puede cambiar. Se manejan entradas no permitidas (?page=0).
- Al hacer clic en una fila de actividad, se redirige a una página con más detalles de la actividad seleccionada.

#### **Detalles de la Actividad:**
- Esta vista muestra toda la información relevante de la actividad.
- Permite volver a la portada o a la lista de actividades.
- Se han agregado funcionalidades para **agregar comentarios** a cada actividad.
  - Los usuarios pueden agregar un comentario sobre la actividad, que incluye el nombre del comentarista y un texto.
  - Al enviar el comentario, se validan los datos antes de enviarlos al servidor, y si son correctos, el comentario se guarda en la base de datos.
  - Además, se visualizan todos los comentarios previos asociados a la actividad, mostrando la fecha, el nombre del comentarista y el texto de cada comentario.
  - Todas las funcionalidades de comentarios estan implementadas en el lado cliente, comunicandose con el servidor a traves de endpoints habilitados. Se trabaja con llamadas asincronas (FETCH).

#### **Estadísticas:**
- Se despliegan tres gráficos que permiten visualizar diferentes aspectos de las actividades:
  1. **Gráfico de líneas**: Muestra la cantidad de actividades por día. 
  2. **Gráfico de torta**: Muestra el total de actividades agrupadas por tipo.
  3. **Gráfico de barras**: Muestra la cantidad de actividades iniciadas por la mañana, al mediodía y por la tarde por meses.

-Los graficos fueron implementados con "HighCharts" en el lado del cliente. Obteniendo los datos del servidor a traves de endpoint habilitados. (Se usan llamadas asincronas)
-Se incluye un enlace al final para volver a la portada.

---
