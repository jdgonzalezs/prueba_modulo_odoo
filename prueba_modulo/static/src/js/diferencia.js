odoo.define('prueba_modulo.diferencia', function (require) {
    
    "use strict";
    console.log("Welcome to my_module")
    // var self = this 
    var rpc = require('web.rpc')
    // //var new_rpc = new rpc('todo.task')
    // rpc.query({ 

//         model: 'todo.task', 
   
//         method: 'get_datos_fecha', 

//         args: [[]]
   
//         }).then(function(result){
   
//           let my_list = []
//           my_list = result
//           console.log(result)
//         // Result 
//          console.log("Inside rpc.query")
   
//    });

//     // let my_list = []
//     // my_list = custom_model.call('get_datos_fecha')

//     console.log("Welcome to my_module")
//     //console.log(my_list)

//     //(new Model('todo.task')).call('diferencia_de_fecha').then(function (valor_de_retorno) {
//       //  console.log(valor_de_retorno);
//         // operacion de porcetaje
//    // });
// 

    var FormController = require('web.FormController');
    FormController.include({
        saveRecord: function () {
            var res = this._super.apply(this, arguments);
            if(this.modelName == 'todo.task'){
                var self = this;
                res.then(function(){
                    //console.log("_rcp");
                    // you can call a method on the server like this
                    self._rpc({
                            model: 'todo.task',
                            method: 'get_all_data',
                            args: [[]],
                            fields: ['promesa', 'fecha', 'mdh_selection'],
                            context: self.context,
                        }).then(function(result){

                                console.log(result);

                                var num_promesa = result['numero_promesa'];
                                var fecha_inicio = result['fecha_creacion'];  
                                var seleccion = result['seleccion'];

                                // crear otro .js que calcule el porcentaje
                                var fecha_ahora = new Date();
                                var fecha_creacion_tarea = new Date(fecha_inicio) - (5*60*60*1000);
                                var tiempo_transcurrido = fecha_ahora - fecha_creacion_tarea; // queda en milisengundos
                                
                                // factor para convertir de ms a lo que se haya indicado en "seleccion"
                                if (seleccion == "minutos"){
                                    var factor = 60*1000;
                                } 
                                else if (seleccion == "horas"){
                                    var factor = 60*60*1000;
                                } 
                                else if(seleccion == "dias"){
                                    var factor = 24*60*60*1000;
                                } 
                                var tiempo_diferencia = tiempo_transcurrido/factor;
                                // console.log("Fecha_ahora: ",  fecha_ahora);
                                // console.log("Fecha_creacion_tarea: ",  fecha_creacion_tarea);
                                // console.log("Tiempo_diferencia: ",  tiempo_diferencia);
                                // console.log("Num_promesa: ",  num_promesa);
                                var porcentaje_transcurrido = tiempo_diferencia * (100/num_promesa);

                                self.porcentaje_transcurrido = porcentaje_transcurrido;
                                res.porcentaje_transcurrido = porcentaje_transcurrido;

                                console.log("Porcentaje: ", porcentaje_transcurrido)

                                //return porcentaje_transcurrido;
                                
                                // ejecutar write() para sobreescribir el campo ['progress_rate']
                                // heredar el widget para luego modificarlo, aplicar css para los colores
                                //return porcentaje_transcurrido;

                                // self._rpc({
                                //     model: 'todo.task',
                                //     method: 'write',
                                //     args: [porcentaje_transcurrido],
                                //     fields: ['progress_rate'],
                                //     context: self.context,

                                // }).then(function(){
                                //     console.log("Metodo write");
                                // });


                            });
                            
                            
                });
            }
            //return self.porcentaje_transcurrido, this.porcentaje_transcurrido;
            console.log("res 1", res);
            return res;
        },





    });


});