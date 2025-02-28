from odoo import api, fields, models
from odoo.tools.misc import OrderedSet, unique

class ActWindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

    view_mode = fields.Selection(selection_add=[('ganttview', 'Gantt View')], ondelete={'ganttview': 'cascade'})

class View(models.Model):
    _inherit = 'ir.ui.view'
    
    type = fields.Selection(selection_add=[('ganttview', "Gantt View")], ondelete={'ganttview': 'cascade'})

    def _get_view_info(self):
        return {'ganttview': {'icon': 'fa fa-tasks'}} | super()._get_view_info()
    