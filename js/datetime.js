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
    // Fecha fin son 3 horas después
    const horaFin = String(fecha.getHours() + 3).padStart(2, '0');
    fechaFin.value = `${anio}-${mes}-${dia}T${horaFin}:${minutos}`;
}

//Llamo la funcion para que se ejecute al cargar la pagina con un event listener
document.addEventListener("DOMContentLoaded", setFechaInicioyFin());

