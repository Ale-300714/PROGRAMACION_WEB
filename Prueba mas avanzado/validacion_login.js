function validateForm(){
    var password = document.getElementById("password").value;


    var modal = new bootstrap.Modal(document.getElementById('validationModal'));
    var modalBody = document.getElementById('validationMessage');


    if (!/^(?=.*[A-Z])(?=.*\d).{8,20}$/.test(password)) {
        modalBody.innerHTML = "La contraseña debe tener al menos una letra mayúscula y un número, y tener entre 8 y 20 caracteres";
        modal.show();
        return false;
    }
    return true;
}
function togglePassword() {
    var passwordInput = document.getElementById("password");
    var toggleButton = document.getElementById("Mostrar_Contraseña");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleButton.textContent = "Ocultar";
    } else {
        passwordInput.type = "password";
        toggleButton.textContent = "Mostrar";
    }
}