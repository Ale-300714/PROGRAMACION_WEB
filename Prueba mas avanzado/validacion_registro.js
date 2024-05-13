
        function validateForm() {
            var nombre = document.getElementById("nombre").value;
            var password = document.getElementById("password").value;

            if (!/^[a-zA-Z\s]+$/.test(nombre)) {
                var modal = new bootstrap.Modal(document.getElementById('validationModal'));
                var modalBody = document.getElementById('validationMessage');
                modalBody.innerHTML = "El nombre debe contener solo letras";
                modal.show();
                return false;
            }

            if (!/^(?=.*[A-Z])(?=.*\d).{8,20}$/.test(password)) {
                var modal = new bootstrap.Modal(document.getElementById('validationModal'));
                var modalBody = document.getElementById('validationMessage');
                modalBody.innerHTML = "La contraseña debe tener al menos una letra mayúscula y un número, y tener entre 8 y 20 caracteres";
                modal.show();
                return false;
            }

            return true;
        }