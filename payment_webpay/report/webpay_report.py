from odoo import fields, models, api, tools


class WebpayPaymentReport(models.Model):
    _name = 'webpay.payment.report'
    _auto = False

    id = fields.Integer("Id", readonly=True)
    name = fields.Char("Name", readonly=True)
    amount = fields.Float("Amount", readonly=True)
    client = fields.Char("Client", readonly=True)
    ref = fields.Char("Reference", readonly=True)
    write_date = fields.Datetime("Date", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE OR REPLACE VIEW %s AS (
            SELECT am.id as id, am.name as name, am.amount_total_signed as amount, 
                rp.name as client, am.ref as ref, am.write_date as write_date 
                FROM account_move as am
                INNER JOIN res_users ru on am.invoice_user_id = ru.id
                INNER JOIN res_partner rp on ru.partner_id = rp.id
                INNER JOIN account_payment as ap on am.id = ap.move_id
                INNER JOIN payment_transaction pt on ap.id = pt.payment_id
                WHERE webpay_token != ''
                ORDER BY am.id, am.name, am.ref
        )""" % self._table)
