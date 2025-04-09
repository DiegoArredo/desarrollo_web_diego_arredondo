const fechaInicio = document.getElementById("fecha_inicio");
const fechaFin = document.getElementById("fecha_fin");
const setFechaInicioyFin = () => {
    const fecha = new Date();
    const dia = String(fecha.getDate()).padStart(2, '0');
    const mes = String(fecha.getMonth() + 1).padStart(2, '0'); // Enero es 0
    const anio = fecha.getFullYear();
    const hora = String(fecha.getHours()).padStart(2, '0');
    const minutos = String(fecha.getMinutes()).padStart(2, '0');
    fechaInicio.value = `${anio}-${mes}-${dia}T${hora}:${minutos}`;
    //sumar 3 horas a la fecha de inicio
    const fechaFinDate = new Date(fechaInicio.value);
    fechaFinDate.setHours(fechaFinDate.getHours() + 3);
    fechaFin.value = `${fechaFinDate.getFullYear()}-${String(fechaFinDate.getMonth() + 1).padStart(2, '0')}-${String(fechaFinDate.getDate()).padStart(2, '0')}T${String(fechaFinDate.getHours()).padStart(2, '0')}:${String(fechaFinDate.getMinutes()).padStart(2, '0')}`;

    // console.log("Fecha de inicio y fin establecidas correctamente.");
    // console.log("Fecha de inicio: " + fechaInicio.value);
    // console.log("Fecha de fin: " + fechaFin.value);
}

//Llamo la funcion para que se ejecute al cargar la pagina con un event listener
document.addEventListener("DOMContentLoaded", setFechaInicioyFin());

