$(document).ready(function(){
    $('#table_ejemploList').DataTable({
     
        ordering: false,
     
       // para cambiar al lenguaje español
       language: {
              
            lengthMenu: "Mostrar _MENU_ registros",
            search: "Buscar...",
            zeroRecords: "No se encuentran resultados",
            info: "registros del _START_ al _END_ de un total de _TOTAL_ registros",
            infoEmpty: "mostrando registros del 0 a 0 de un total de 0 registros",
            infoFiltered: "(filtrado de un total de _MAX_ registros)",
            oPaginate: {
              sFirst:"primero",
              sLast: "último",
              sNext:"siguiente",
              sPrevious: "anterior",

            },
            sProcessing:"Procesando...",

           
        }
      

    });
});