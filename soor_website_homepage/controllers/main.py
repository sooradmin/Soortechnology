# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


def _soor_blog_catalog():
    """Static demo posts (ordered → prev/next). Replace with blog.post when needed."""
    section_odoo_paras = [
        (
            "Losing natural teeth affects both function and appearance. While traditional dentures serve a purpose, "
            "they often come with drawbacks such as poor fit, discomfort, and instability when eating or speaking. "
            "Additionally, they do not stimulate the jawbone, leading to gradual bone loss and facial structure changes. "
            "Routine maintenance is also required to keep removable dentures clean and functional."
        ),
        (
            "Implant-retained dentures offer a superior alternative. Instead of relying on adhesives, these dentures "
            "are anchored by dental implants, providing a stable and secure fit. This eliminates many of the challenges "
            "posed by conventional dentures and significantly improves quality of life."
        ),
    ]
    lead_odoo = (
        "Implant-retained dentures are revolutionizing tooth replacement, blending the reliability of traditional "
        "dentures with advanced dental implant technology. By addressing common issues associated with conventional "
        "dentures, implant-supported dentures offer a more secure, comfortable, and long-lasting solution."
    )
    generic_lead = (
        "In today's rapidly evolving digital landscape, businesses must embrace change to stay competitive. "
        "Soor Technologies helps teams implement Odoo with clarity, from discovery through go-live and beyond."
    )
    generic_section = (
        "Clear requirements, iterative delivery, and hands-on training reduce risk and accelerate time-to-value. "
        "We align Odoo modules with your processes so adoption sticks and reporting stays trustworthy."
    )

    return [
        {
            "slug": "tackling-requirements-elicitation-odoo",
            "card_title": "Tackling Requirements Elicitation Challenges in Odoo ERP Projects",
            "title": "Tackling Requirements Elicitation Challenges in Odoo ERP Projects",
            "subtitle": "One of Soor Technologies posts on LinkedIn",
            "excerpt": "Practical ways to capture business needs before configuration starts—so your Odoo project stays on track.",
            "date": "Jan 15, 2025",
            "read_time": "6 min read",
            "image": "https://placehold.co/354x212/png?text=Requirements",
            "cover_image": "https://placehold.co/1078x542/png?text=Requirements",
            "lead_paragraphs": [generic_lead],
            "sections": [
                {"title": "Why requirements matter in ERP", "paragraphs": [generic_section]},
                {"title": "Workshops that surface real workflows", "paragraphs": [generic_section]},
            ],
        },
        {
            "slug": "simplifying-product-creation-odoo",
            "card_title": "Simplifying Product Creation in Odoo: A Quick Guide by Soor Technologies",
            "title": "Simplifying Product Creation in Odoo: A Quick Guide by Soor Technologies",
            "subtitle": "One of Soor Technologies posts on LinkedIn",
            "excerpt": "A concise walkthrough for setting up products, variants, and attributes in Odoo.",
            "date": "Jan 22, 2025",
            "read_time": "8 min read",
            "image": "https://placehold.co/354x212/png?text=Odoo+Product",
            "cover_image": "https://placehold.co/1078x542/png?text=1078x542",
            "lead_paragraphs": [lead_odoo],
            "sections": [
                {"title": "Why Choose Implant-Retained Dentures?", "paragraphs": list(section_odoo_paras)},
                {"title": "Why Choose Implant-Retained Dentures?", "paragraphs": list(section_odoo_paras)},
            ],
        },
        {
            "slug": "odoo-first-sales-quotation",
            "card_title": "Getting Started with Odoo: How to Create Your First Sales Quotation in Minutes",
            "title": "Getting Started with Odoo: How to Create Your First Sales Quotation in Minutes",
            "subtitle": "One of Soor Technologies posts on LinkedIn",
            "excerpt": "Step-by-step: from customer to confirmed quotation using Sales and optional CRM.",
            "date": "Jan 28, 2025",
            "read_time": "5 min read",
            "image": "https://placehold.co/354x212/png?text=Quotation",
            "cover_image": "https://placehold.co/1078x542/png?text=Quotation",
            "lead_paragraphs": [generic_lead],
            "sections": [
                {"title": "Create the customer record", "paragraphs": [generic_section]},
                {"title": "Build and send the quotation", "paragraphs": [generic_section]},
            ],
        },
        {
            "slug": "effective-brand-storytelling",
            "card_title": "5 strategies for effective brand storytelling",
            "title": "5 strategies for effective brand storytelling",
            "subtitle": "Insights from Soor Technologies",
            "excerpt": (
                "In today's rapidly evolving digital landscape, businesses must embrace change to stay competitive. "
                "Digital transformatio"
            ),
            "date": "Jan 28, 2025",
            "read_time": "8 min read",
            "image": "https://placehold.co/354x212/png?text=Brand",
            "cover_image": "https://placehold.co/1078x542/png?text=Brand",
            "lead_paragraphs": [generic_lead],
            "sections": [
                {"title": "Lead with a clear narrative", "paragraphs": [generic_section]},
                {"title": "Measure what resonates", "paragraphs": [generic_section]},
            ],
        },
        {
            "slug": "digital-transformation-odoo",
            "card_title": "Digital transformation without the chaos",
            "title": "Digital transformation without the chaos",
            "subtitle": "One of Soor Technologies posts on LinkedIn",
            "excerpt": "How phased rollouts and change management keep teams productive during ERP change.",
            "date": "Feb 2, 2025",
            "read_time": "7 min read",
            "image": "https://placehold.co/354x212/png?text=Transform",
            "cover_image": "https://placehold.co/1078x542/png?text=Transform",
            "lead_paragraphs": [generic_lead],
            "sections": [
                {"title": "Phase zero: discovery", "paragraphs": [generic_section]},
                {"title": "Pilot, then scale", "paragraphs": [generic_section]},
            ],
        },
        {
            "slug": "scaling-operations-odoo",
            "card_title": "Scaling operations with Odoo at the core",
            "title": "Scaling operations with Odoo at the core",
            "subtitle": "One of Soor Technologies posts on LinkedIn",
            "excerpt": "Integrations, inventory, and manufacturing patterns we use for growing companies.",
            "date": "Feb 8, 2025",
            "read_time": "9 min read",
            "image": "https://placehold.co/354x212/png?text=Scale",
            "cover_image": "https://placehold.co/1078x542/png?text=Scale",
            "lead_paragraphs": [generic_lead],
            "sections": [
                {"title": "Single source of truth", "paragraphs": [generic_section]},
                {"title": "Automation that saves hours", "paragraphs": [generic_section]},
            ],
        },
    ]


def _soor_blog_posts_for_list():
    rows = []
    for p in _soor_blog_catalog():
        row = {k: v for k, v in p.items() if k not in ("lead_paragraphs", "sections")}
        row["title"] = p["card_title"]
        row["url"] = "/blog/%s" % p["slug"]
        rows.append(row)
    return rows


def _soor_blog_detail_ctx(slug):
    catalog = _soor_blog_catalog()
    for i, post in enumerate(catalog):
        if post["slug"] != slug:
            continue
        prev_post = catalog[i - 1] if i > 0 else None
        next_post = catalog[i + 1] if i + 1 < len(catalog) else None
        return {"post": post, "prev_post": prev_post, "next_post": next_post}
    return None


class SoorWebsiteServices(http.Controller):
    @http.route("/services", type="http", auth="public", website=True, sitemap=True)
    def services(self, **kwargs):
        return request.render("soor_website_homepage.soor_services_page", {})

    @http.route("/about", type="http", auth="public", website=True, sitemap=True)
    def about(self, **kwargs):
        return request.render("soor_website_homepage.soor_about_page", {})

    @http.route("/hessapay", type="http", auth="public", website=True, sitemap=True)
    def hessapay(self, **kwargs):
        return request.render("soor_website_homepage.soor_hessapay_page", {})

    @http.route("/odoo", type="http", auth="public", website=True, sitemap=True)
    def odoo_erp(self, **kwargs):
        return request.render("soor_website_homepage.soor_odoo_page", {})

    @http.route("/blogs", type="http", auth="public", website=True, sitemap=True)
    def blogs(self, **kwargs):
        return request.render(
            "soor_website_homepage.soor_blogs_page",
            {"posts": _soor_blog_posts_for_list()},
        )

    @http.route(
        ["/blog/<string:slug>"],
        type="http",
        auth="public",
        website=True,
        sitemap=False,
    )
    def blog_post(self, slug, **kwargs):
        ctx = _soor_blog_detail_ctx(slug)
        if not ctx:
            return request.not_found()
        return request.render("soor_website_homepage.soor_blog_post_page", ctx)
