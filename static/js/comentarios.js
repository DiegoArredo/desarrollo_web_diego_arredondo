 function obtener_comentarios() {
  let myForm = document.getElementById('comentario-form');
  let actividadId = myForm.actividad_id.value;

  fetch(`http://127.0.0.1:5000/obtener_comentarios`, {
    method: "POST",
    body: JSON.stringify({ actividad_id: actividadId }),
    credentials: "include",
    cache: "no-cache",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
        console.log(data);
        const comentariosContainer = document.getElementById("comentarios_container");
        comentariosContainer.innerHTML = ""; // Limpiar el contenedor antes de agregar nuevos comentarios
        console.log("Agregando comentarios al contenedor");
        data.forEach((comentario) => {
            const comentarioDiv = document.createElement("div");
            comentarioDiv.className = "comentario";
            comentarioDiv.innerHTML = `
                <p class="encabezado"><strong class="fecha">${comentario.nombre}</strong> (${comentario.fecha}):</p>
                <p class="cuerpo">${comentario.texto}</p>
            `; 
            comentariosContainer.appendChild(comentarioDiv);
        });
    })
    .catch((error) => {
      console.error(
        "There has been a problem with your fetch operation:",
        error
      );
    });
 };
// Función para enviar un nuevo comentario
function agergar_comentario(data) {
  console.log("Enviando comentario:", data);
  fetch(`http://127.0.0.1:5000/agregar_comentario`, {
    method: "POST",
    body: JSON.stringify(data),
    credentials: "include",
    cache: "no-cache",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {

        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      if (data.errores) {
        let valList = document.getElementById('val-list');
         let valBox = document.getElementById('val-box');
        valList.innerHTML = ''; 
        valBox.hidden = false; 
        data.errores.forEach(function(error) {
          let li = document.createElement('li');
          li.textContent = error;
          valList.appendChild(li);
        });
        console.error("Error al agregar el comentario:", data.errores);
        return;
      }
      if (data.success) {
        console.log("Comentario agregado exitosamente");
      }
      // Recargar los comentarios después de enviar uno nuevo
      obtener_comentarios();
      limpiar_formulario();
    })
    .catch((error) => {

      console.error("Error al enviar el comentario:", error);
    });
};
