# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

# class plant_nursery(models.Model):
#     _name = 'plant_nursery.plant_nursery'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Plants(models.Model):
    _name = 'nursery.plant'
    description = "Nursery Plant"

    name = fields.Char("Plant Name")
    price = fields.Float()
    order_ids = fields.One2many("nursery.order", "plant_id", string="Orders")

    order_count = fields.Integer(compute='_compute_order_count', store=True, string="Total sold")

    number_in_stock = fields.Integer()

    @api.depends('order_ids')
    def _compute_order_count(self):
        for plant in self:
            plant.order_count = len(plant.order_ids)

    @api.constrains('order_count', 'number_in_stock')
    def _check_avalible_in_stock(self):
        for plant in self:
            if plant.number_in_stock and plant.order_count > plant.number_in_stock:
                raise UserError("There is only %s %s in stock burt %s were sold" %(plant.number_in_stock, plant.name, plant.order_count))

class Customer(models.Model):
    _name = "nursery.customer"
    description = "Nursery Customer"

    name = fields.Char("Customer Name", required=True)
    email = fields.Char(help="To receive newsletter")



















