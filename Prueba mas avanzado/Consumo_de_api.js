$(document).ready(function(){
    // Función para cargar los datos de la raza de perro 1
    function cargarDatosRaza1() {
        // Limpiar la tabla antes de agregar nuevos datos
        $("#raza1 tbody").empty();

        // Llamada a la API para obtener datos de la raza de perro
        $.get("https://dogapi.dog/api/v2/breeds",
            function(data){
                $.each(data.data, function(i, item){
                    // Verificar si el ID coincide
                    if (item.id === "68f47c5a-5115-47cd-9849-e45d3c378f12") {
                        // Obtener los datos de la raza
                        var id = item.id;
                        var name = item.attributes.name;
                        var description = item.attributes.description;

                        // Agregar los datos a la tabla
                        $("#raza1 tbody").append(
                            "<tr>" +
                                "<td>"+id+"</td>" +
                                "<td>"+name+"</td>" +
                                "<td>"+description+"</td>" +
                            "</tr>"
                        );
                    }
                });
            });
        $("#raza1").show();
    }

    // Evento al hacer clic en el botón para mostrar los datos de la raza 1
    $("#perro1").click(function(){
        cargarDatosRaza1();
    });

    function ocultardatosraza1(){
        $("#raza1").hide();
    }

    // Evento al hacer clic en el botón para ocultar los datos de la raza 1
    $("#ocultar1").click(function(){
        ocultardatosraza1();
    });

    // Función para cargar los datos de la segunda raza de perro
    function cargarDatosRaza2() {
        // Limpiar la tabla antes de agregar nuevos datos
        $("#raza2 tbody").empty();

        // Llamada a la API para obtener datos de la raza de perro
        $.get("https://dogapi.dog/api/v2/breeds",
            function(data){
                $.each(data.data, function(i, item){
                    // Verificar si el ID coincide
                    if (item.id === "4ddbe251-72af-495e-8e9d-869217e1d92a") {
                        // Obtener los datos de la raza
                        var id = item.id;
                        var name = item.attributes.name;
                        var description = item.attributes.description;

                        // Agregar los datos a la tabla
                        $("#raza2 tbody").append(
                            "<tr>" +
                                "<td>"+id+"</td>" +
                                "<td>"+name+"</td>" +
                                "<td>"+description+"</td>" +
                            "</tr>"
                        );
                    }
                });
            });
        $("#raza2").show();
    }

    // Evento al hacer clic en el botón para mostrar los datos de la raza 2
    $("#perro2").click(function(){
        cargarDatosRaza2();
    });

    function ocultardatosraza2(){
        $("#raza2").hide();
    }

    // Evento al hacer clic en el botón para ocultar los datos de la raza 2
    $("#ocultar2").click(function(){
        ocultardatosraza2();
    });

    // Función para cargar los datos del tercer perro
    function cargarDatosRaza3() {
        $("#raza3 tbody").empty();

        $.get("https://dogapi.dog/api/v2/breeds",
            function(data){
                $.each(data.data, function(i, item){
                    if (item.id === "f534c847-bed1-4b58-b194-dc06ecfe20f9") {
                        var id = item.id;
                        var name = item.attributes.name;
                        var description = item.attributes.description;
                        $("#raza3 tbody").append(
                            "<tr>" +
                                "<td>"+id+"</td>" +
                                "<td>"+name+"</td>" +
                                "<td>"+description+"</td>" +
                            "</tr>"
                        );
                    }
                });
            });
        $("#raza3").show();
    }

    
    $("#perro3").click(function(){
        cargarDatosRaza3();
    });

    function ocultardatosraza3(){
        $("#raza3").hide();
    }

    
    $("#ocultar3").click(function(){
        ocultardatosraza3();
    });

    function cargarDatosRaza4() {
        $("#raza4 tbody").empty();

        $.get("https://dogapi.dog/api/v2/breeds",
            function(data){
                $.each(data.data, function(i, item){
                    if (item.id === "30f62219-e225-42cd-bd07-02425f944c07") {
                        var id = item.id;
                        var name = item.attributes.name;
                        var description = item.attributes.description;
                        $("#raza4 tbody").append(
                            "<tr>" +
                                "<td>"+id+"</td>" +
                                "<td>"+name+"</td>" +
                                "<td>"+description+"</td>" +
                            "</tr>"
                        );
                    }
                });
            });
        $("#raza4").show();
    }

    
    $("#perro4").click(function(){
        cargarDatosRaza4();
    });

    function ocultardatosraza4(){
        $("#raza4").hide();
    }

    
    $("#ocultar4").click(function(){
        ocultardatosraza4();
    });
    // Mostrar la foto del primer perro
    var image1 = "https://www.thesprucepets.com/thmb/xnymOFVuv4F0O7AdLK6K6mozkkg=/2124x1411/filters:fill(auto,1)/CaucasianOvcharka-GettyImages-999579156-63ec1efdf2e1420dabdbcf2e83a70475.jpg"; // URL de la imagen obtenida manualmente
    $("#foto_perro1").html("<img src='"+image1+"' alt='Foto de Perro 1' style='max-width: 300px;'>");

    // Mostrar la foto del segundo perro
    var image2 = "https://www.dailypaws.com/thmb/ffEDQuVmvVshkCEXiBGerEcFDQQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/bouvier-des-flandres-sitting-snow-1037527928-2000-551fc58aac034de5b7523d439e6da0e4.jpg"; // URL de la imagen obtenida manualmente
    $("#foto_perro2").html("<img src='"+image2+"' alt='Foto de Perro 2' style='max-width: 300px;'>");
    //Mostrar la foto del tercer perro
    var image3 = "https://www.houdenvanhonden.nl/globalassets/rassen/fci-6/grand-basset-griffon-vendeen/grand-basset-griffon-vendeen-a3.jpg"; // URL de la imagen obtenida manualmente
    $("#foto_perro3").html("<img src='"+image3+"' alt='Foto de Perro 2' style='max-width: 300px;'>");

    var image4 = "https://breedadvisor.com/wp-content/uploads/2020/02/HOKKAIDO-PUPPY.jpg"; // URL de la imagen obtenida manualmente
    $("#foto_perro4").html("<img src='"+image4+"' alt='Foto de Perro 2' style='max-width: 300px;'>");
    
});
