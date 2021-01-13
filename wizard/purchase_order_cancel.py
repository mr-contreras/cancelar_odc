# -*- coding: utf-8 -*-abs
from odoo import api, models, _
from odoo.exceptions import UserError

class PurchaseOrderCancel(models.TransientModel):
    _name = "purchase.order.cancel"
    _description = "Cancelar Ordenes de Compra"

    @api.multi
    def cancel_order(self):
        if self.env.uid == 101 or self.env.uid == 1 or self.env.uid == 114 or self.env.uid == 24:
            purchase_orders = self.env['purchase.order'].browse(
                self._context.get('active_ids', []))
            purchase_orders.write({'state': 'cancel'})
            return purchase_orders
        
        else:
            raise UserError(_('No tiene permisos para cancelar ordenes de compra.'))
