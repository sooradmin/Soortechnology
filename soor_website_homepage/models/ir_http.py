# -*- coding: utf-8 -*-
from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    # @classmethod
    # def _get_frontend_langs(cls):
    #     """Limit installed URL languages to default when SOOR Google-Translate mode is on.
    #
    #     Otherwise Accept-Language: ar matches installed Arabic → Odoo redirects new browsers
    #     to /ar/… even though Arabic is only meant for machine translation.
    #     """
    #     if getattr(request, "is_frontend", True):
    #         try:
    #             website = request.env["website"].sudo().get_current_website()
    #         except Exception:
    #             website = None
    #         if (
    #             website
    #             and website.soor_route_default_lang_only
    #             and website._get_cached("default_lang_id")
    #         ):
    #             default_lang = cls._get_default_lang()
    #             if default_lang:
    #                 return [default_lang.code]
    #     return super()._get_frontend_langs()
