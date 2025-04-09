const validateRegion = (region) => {
    if (!region) return false;
    return true;
};
const validateComuna = (comuna) => {
    if (!comuna) return false;
    return true;
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
    return true;
}
const validarFechaFin = (fechaFin) => {
    let fechaInicio = document.getElementById("fecha_inicio").value;
    if(fechaFin.value < fechaInicio) return false;
    return true;
}

const validateTema = (tema) => {
    if (!tema) return false;
    if (tema.value == "otro") {
        let otroTema = document.getElementById("otro_tema").value;
        if (!otroTema) return false;
        let validLength = otroTema.trim().length <= 15 && otroTema.trim().length >= 2;
        return validLength;
    }
    return true;
}

const validarFiles = (files) => {
    if (!files) return false;
    let validLength = files.length <= 5 && files.length > 0;
    return validLength;
}

const validateForm = () => {
    console.log("Validando formulario...");
    // obtener elementos del DOM usando el nombre del formulario.
    let myForm = document.forms["actividad-form"];
    let region = myForm["region"].value;
    let comuna = myForm["comuna"].value;
    let sector = document.getElementById("sector").value;
    let nombre = document.getElementById("nombre").value;
    let email = document.getElementById("email").value;
    let telefono = document.getElementById("numero").value;


    let fechaInicio = document.getElementById("fecha_inicio").value;
    let fechaFin = document.getElementById("fecha_fin").value;
    let tema = document.getElementById("tema").value;
    let otroTema = document.getElementById("otro_tema").value;
    let files = document.getElementById("foto").files;
     
    // variables auxiliares de validación y función.
    let invalidInputs = [];
    let isValid = true;
    const setInvalidInput = (inputName) => {
      invalidInputs.push(inputName);
      isValid &&= false;
    };
  
    // lógica de validación
    // validar los campos del contacto ((especial))
    if (document.getElementById("chk-whatsapp").checked) {
        let whatsapp = document.getElementById("whatsapp").value;
        console.log("whatsapp: " + whatsapp);
        if (!validateContactar(whatsapp)) {
            setInvalidInput("Whatsapp");
        }
    }
    if (document.getElementById("chk-instagram").checked) {
        let instagram = document.getElementById("instagram").value;
        console.log("instagram: " + instagram);
        if (!validateContactar(instagram)) {
            setInvalidInput("Instagram");
        }
    }
    if (document.getElementById("chk-x").checked) {
        let x = document.getElementById("x").value;
        console.log("x: " + x);
        if (!validateContactar(x)) {
            setInvalidInput("X");
        }
    }
    if (document.getElementById("chk-telegram").checked) {
        let telegram = document.getElementById("telegram").value;
        console.log("telegram: " + telegram);
        if (!validateContactar(telegram)) {
            setInvalidInput("Telegram");
        }
    }
    if (document.getElementById("chk-tiktok").checked) {
        let tiktok = document.getElementById("tiktok").value;
        if (!validateContactar(tiktok)) {
            setInvalidInput("Tiktok");
        }
    };
    // validar los campos del formulario
    if (!validateNombre(nombre)) {
      setInvalidInput("Nombre");
    }
    if (!validateEmail(email)) {
        setInvalidInput("Email");
    }
    if (!validateTelefono(telefono)) {
        setInvalidInput("Teléfono");
    }
    if (!validateRegion(region)) {
        console.log(region);
        setInvalidInput("Región");
    }
    if (!validateComuna(comuna)) {
        setInvalidInput("Comuna");
    }
    if (!validateSector(sector)) {
        setInvalidInput("Sector");
    }
    if (!validarFechaInicio(fechaInicio)) {
        setInvalidInput("Fecha Inicio");
    }
    if (!validarFechaFin(fechaFin)) {
        setInvalidInput("Fecha Fin");
    }
    if (!validateTema(tema)) {
        setInvalidInput("Tema");
    }
    if (tema.value == "otro" && !validateTema(otroTema)) {
        setInvalidInput("Otro Tema");
    }
    if (!validarFiles(files)) {
        setInvalidInput("Archivos");
    }
    // si el formulario es válido, se envía el formulario.
    // si no es válido, se muestran los errores.

  
    // finalmente mostrar la validación
    let validationBox = document.getElementById("val-box");
    let validationMessageElem = document.getElementById("val-msg");
    let validationListElem = document.getElementById("val-list");
  
    if (!isValid) {
      validationListElem.textContent = "";
      // agregar elementos inválidos al elemento val-list.
      for (input of invalidInputs) {
        let listElement = document.createElement("li");
        listElement.innerText = input;
        validationListElem.append(listElement);
      }
      // establecer val-msg
      validationMessageElem.innerText = "Los siguientes campos son inválidos:";
  
      // aplicar estilos de error
      validationBox.style.backgroundColor = "#ffdddd";
      validationBox.style.borderLeftColor = "#f44336";
  
      // hacer visible el mensaje de validación
      validationBox.hidden = false;

      var modal = document.getElementById("myModal");
      modal.style.display = "none";
      // ir al principio del formulario
      window.scrollTo(0, 0);

    } else {
      
        // ocultar el mensaje de validación si el formulario es válido
        validationBox.hidden = true;
        // alertar al usuario que el formulario es válido "hemos recibido su información, muchas gracias, suerte en su actividad"
        alert("Hemos recibido su información, muchas gracias, suerte en su actividad.");
        //llevar a la pagina de inicio
        window.location.href = "/index.html";
        // enviar el formulario
        document.getElementById("actividad-form").submit();
    }
  };
  
  