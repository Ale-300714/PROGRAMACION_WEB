function validacion_contacto(){
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var telefono = document.getElementById("telefono").value;

    var modal = new bootstrap.Modal(document.getElementById('validationModal'));
    var modalBody = document.getElementById('validationMessage');

    if (!/^[a-zA-Z\s]+$/.test(nombre)) {
        modalBody.innerHTML = "El nombre debe contener solo letras";
        modal.show();
        return false;
    }

    if (!/^[a-zA-Z\s]+$/.test(apellido)) {
        modalBody.innerHTML = "El apellido debe contener solo letras";
        modal.show();
        return false;
    }
    
    if (!/^\d{9}$/.test(telefono)) {
        modalBody.innerHTML = "El número de teléfono debe tener exactamente 9 números y sin espacios";
        modal.show();
        return false;
    }

}
