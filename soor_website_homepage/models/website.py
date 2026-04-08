# -*- coding: utf-8 -*-
from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    soor_route_default_lang_only = fields.Boolean(
        string="SOOR: Default language URLs only",
        default=True,
        help="When enabled, the website frontend ignores extra installed languages for URL "
        "matching (no redirect to /ar/… from the browser language). Use this when Arabic "
        "is handled only via Google Translate, not Odoo translations.",
    )
