# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    # A esta fecha se le restan 5 horas para que concoincida con la hora de Colombia
    fecha = fields.Datetime(default=fields.Datetime.now) 
    promesa = fields.Float() 
    mdh_selection = fields.Selection([
        ('minutos', 'Minutos'), 
        ('horas','Horas'),
        ('dias' ,'Días')], default='minutos')  

    # Para el widget gauge 
    progress_rate = fields.Integer(string='Progreso', store=True, recompute=True)
    maximum_rate = fields.Integer(string='Maximum Rate', default=100)

    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True
    
    @api.multi
    def do_clear_done(self):
        dones = self.search([('is_done', '=', True)], limit=1)
        dones.write({'active': False})
        return True 

    @api.model
    def get_all_data(self):
        result = {}
        datas = self.env['todo.task'].search([], order='create_date desc', limit=1)
        for d in datas:
            result['numero_promesa'] = d.promesa
            result['fecha_creacion'] = d.fecha
            result['seleccion'] = d.mdh_selection
 
        return result

    @api.model
    def write(self,values):
        #values = {}
        values['last_modification'] = self.progress_rate
        #values = self.progress_rate
        #campo = super(TodoTask, self).write(values)
        return super(TodoTask, self).write(values)
        #return campo

