from odoo import models, fields
from odoo.exceptions import UserError

class Order(models.Model):
    _name = 'nursery.order'
    description = 'Nursery Order'

    name = fields.Datetime(default=fields.Datetime.now)
    plant_id = fields.Many2one("nursery.plant", required=True)
    customer_id = fields.Many2one("nursery.customer")
    state = fields.Selection([
        ('draft','Draft'), 
        ('confirm', 'Confirmed'), 
        ('cancel','Canceled'),
    ], default='draft')
    # state=fields.Char("EstadoS")    
    last_modification = fields.Datetime(readonly=True) 
     
    def write(self,values):
        # date format is "YYYY-MM-DD"
        values['last_modification'] = fields.Datetime.now()

        return super(Order, self).write(values)

    
    def unlink(self):
        # self is a recordset
        for order in self:
            if order.state == 'confirm':
                raise UserError("You can not delete confirmed orders")

        return super(Order, self).unlink()
                     