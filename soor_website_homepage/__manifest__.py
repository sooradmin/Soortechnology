# -*- coding: utf-8 -*-
{
    "name": "SOOR Website",
    "version": "16.0.1.0.0",
    "summary": "Custom  design for SOOR website",
    "category": "Website",
    "author": "Qasim Ali",
    "license": "LGPL-3",
    "website":"kashiawan0042@gmail.com(+923144171940)",
    "depends": ["website", "website_crm"],
    "data": [
        "data/partner_logos_attachments.xml",
        "views/website_homepage.xml",
        "views/website_contact.xml",
        "views/website_services.xml",
        "views/website_about.xml",
        "views/website_hessapay.xml",
        "views/website_odoo.xml",
        "views/website_blogs.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "soor_website_homepage/static/src/js/soor_counters.js",
            "soor_website_homepage/static/src/scss/soor_homepage.scss",
            "soor_website_homepage/static/src/scss/soor_contact.scss",
            "soor_website_homepage/static/src/scss/soor_services.scss",
            "soor_website_homepage/static/src/scss/soor_about.scss",
            "soor_website_homepage/static/src/scss/soor_hessapay.scss",
            "soor_website_homepage/static/src/scss/soor_odoo.scss",
            "soor_website_homepage/static/src/scss/soor_blogs.scss",
        ],
    },
    "installable": True,
    "application": False,
}

