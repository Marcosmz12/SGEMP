from odoo import models, fields, api
from datetime import timedelta

class Sugerencia(models.Model):
    _name = 'sugerencias.sugerencia'
    _description = 'Sugerencia Principal'

    name = fields.Char(string='Identificación', required=True)
    description = fields.Text(string='Comentario de la sugerencia')
    responsible_id = fields.Many2one('res.users', string='Responsable')
    seguimiento_ids = fields.One2many('sugerencias.seguimiento', 'sugerencia_id', string='Seguimientos')

class Seguimiento(models.Model):
    _name = 'sugerencias.seguimiento'
    _description = 'Seguimiento de Sugerencia'

    name = fields.Char(string='Acción de Seguimiento', required=True)
    start_date = fields.Date(string='Fecha Inicio', default=fields.Date.context_today)
    duration = fields.Float(string='Duración (días)', digits=(6, 2))
    end_date = fields.Date(string='Fecha Fin', store=True, compute='_get_end_date')
    seats = fields.Integer(string='Prioridad/Puntos')
    active = fields.Boolean(default=True)
    color = fields.Integer()
    
    sugerencia_id = fields.Many2one('sugerencias.sugerencia', string='Sugerencia', required=True)
    tecnico_id = fields.Many2one('res.partner', string='Técnico Asignado')
    participante_ids = fields.Many2many('res.partner', string='Participantes')
    
    taken_seats = fields.Float(string="Progreso", compute='_compute_taken_seats')
    attendees_count = fields.Integer(string="Cantidad Participantes", compute='_get_attendees_count', store=True)

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            r.end_date = r.start_date + timedelta(days=r.duration)

    @api.depends('seats', 'participante_ids')
    def _compute_taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.participante_ids) / r.seats

    @api.depends('participante_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.participante_ids)

# Modelo para el Wizard (Asistente)
class SugerenciaWizard(models.TransientModel):
    _name = 'sugerencias.wizard'
    _description = "Asistente para añadir participantes"

    seguimiento_id = fields.Many2one('sugerencias.seguimiento', string="Seguimiento", required=True)
    participante_ids = fields.Many2many('res.partner', string="Participantes")

    def subscribe(self):
        self.seguimiento_id.participante_ids |= self.participante_ids
        return {}