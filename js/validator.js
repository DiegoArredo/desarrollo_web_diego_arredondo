const validateRegion = (region) => {
    if (!region) return false;
};
const validateComuna = (comuna) => {
    if (!comuna) return false;
};
const validateSector = (sector) => {
    let validLength = sector.trim().length <= 100;
    return validLength;
};
const validateNombre = (nombre) => {
    if (!nombre) return false;
    let validLength = nombre.trim().length <= 200;
    return validLength;
};
const validateEmail = (email) => {
    if (!email) return false;
    let validLength = email.trim().length <= 100;
    let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    let formatValid = re.test(email);
    return validLength && formatValid;
}

const validateTelefono = (telefono) => {
    if (!telefono) return false;
    let validLength = telefono.trim().length >= 8;
    let re = /^[0-9]+$/;
    let formatValid = re.test(telefono);
    return validLength && formatValid;
}

const validateContactar = (contacto) => {
    if (!contacto) return false;
    let validLength = contacto.trim().length > 4 && contacto.trim().length <= 50;
    return validLength;
};

const validarFechaInicio = (fechaInicio) => {
    if (!fechaInicio) return false;
}
const validarFechaFin = (fechaFin) => {
    fechaInicio = document.getElementById("fecha_inicio").value;
    if(fechaFin.value < fechaInicio) return false;
}

const validateTema = (tema) => {
    if (!tema) return false;
    if (tema.value == "otro") {
        let otroTema = document.getElementById("otro_tema").value;
        if (!otroTema) return false;
        let validLength = otroTema.trim().length <= 15 && otroTema.trim().length >= 2;
        return validLength;
    }
}

const validarFiles = (files) => {
    if (!files) return false;
    let validLength = files.length <= 5;
    return validLength && validSize;
}