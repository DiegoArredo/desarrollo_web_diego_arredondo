# Tarea 4 – Evaluación de Actividades

Esta entrega agrega la opción de poner notas a las actividades que ya existían en la app.  

---

## Que hacer:

- Ver la lista de actividades realizadas (las que terminaron antes de hoy) con las columnas: ID, Fecha Inicio, Sector, Nombre, Tema y la nota promedio.  Si la actividad aún no tiene notas debe mostrar un “‐”.
- Al hacer clic en “evaluar” se debe pedir una nota del 1 al 7.
- La nota nueva tiene que guardarse en la base de datos.
- Después de guardar hay que recalcular el promedio y actualizar la celda en la misma página, sin recargarla completa.

## Descripción de la entrega:

### Backend (Spring Boot, Java 21) — localhost:8080

- Usé Spring Boot solo como API.
- Modelé tres tablas con JPA: `Actividad`, `ActividadTema` y la nueva `Nota`.
- Creé sus repositorios.
- En `ApiController` definí `/actividad_notas`  
  - **GET** devuelve las actividades que ya empezaron, el tema de cada actividad y la lista de notas por actividad de forma separada.(Los datos necesarios para crear la tabla) 
  - **POST** recibe `{ actividadId, nota }` y guarda la nota, verificando previamente los datos.  
- `ApiService` se encarga de entregar los datos obteniendolos de la BD y en el caso de agregar, de validar que la nota sea un entero entre 1 y 7 antes de guardarla y de que la actividad que se le asigna la nota exista en la BD.

### Frontend (Flask) — localhost:5000

- En Flask hice una vista nueva: `/actividad_notas`.
- Con JS (fetch) pido los datos al endpoint **GET** y creo la tabla,de estos datos obtenidos se calcula el promedio de notas de la actividad para mostrarlo en la tabla.
- Cada fila tiene un link **“evaluar”**. Al hacer clic aparece un *prompt* donde el usuario ingresa la nota (solo acepta números del 1 al 7, validado en JS).
- El script envía la nota al endpoint **POST** y, si el servidor responde OK, vuelve a pedir los datos con **GET** y actualiza la tabla.

Se trabajo usando Flask como Front-End y SpringBoot como un microservicio/API (Back-End).
