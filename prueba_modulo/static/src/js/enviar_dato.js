odoo.define('prueba_enviar_dato',function (require) { 

    "use strict";
    console.log("Dentro de enviar_dato.js");
    var dato_porcentaje = require('prueba_modulo.escribir')
    var rpc = require('web.rpc');
    //console.log("RPC", rpc);
    console.log("porcentaje", dato_porcentaje);
    //model('todo.task').call('write',[dato_porcentaje]).then(function(result){
    //     console.log("Result_enviar_dato", result);
    //     return result;
    // });
    

//     //this.call('write', [[self.id], { 'progress_rate': percent }]).done(function() {

//     //    console.log("Revisar Write");
    rpc.query({

        model: 'todo.task',
        method: 'write',
        args: [[],[dato_porcentaje]],
        fields: ['progress_rate'],
        context: self.context,

        }).then(function(result){
            
            console.log("result_enviar_datos",result);
        })  
        
    
        
});

