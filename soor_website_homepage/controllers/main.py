# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


def _soor_blog_catalog():
    """Static demo posts (ordered → prev/next). Replace with blog.post when needed."""
    return [
        {
            "slug": "tackling-requirements-elicitation-odoo",
            "card_title": "Tackling Requirements Elicitation Challenges in Odoo ERP Projects",
            "title": "Tackling Requirements Elicitation Challenges in Odoo ERP Projects",
            "subtitle": "Structured discovery for Odoo ERP teams in Kuwait and the Gulf.",
            "excerpt": (
                "Practical ways to capture business needs before configuration starts—so your Odoo project stays on track."
            ),
            "date": "Jan 15, 2025",
            "read_time": "6 min read",
            "image": "https://placehold.co/354x212/png?text=Requirements",
            "cover_image": "https://placehold.co/1078x542/png?text=Requirements",
            "lead_paragraphs": [
                (
                    "Implementing an Odoo ERP system can transform how a business operates but only if the project "
                    "starts with clear, well-defined requirements. Many Odoo projects in Kuwait and across the wider "
                    "Gulf region struggle because requirements are gathered too quickly, incompletely, or based on "
                    "assumptions instead of real business processes. In this article, we'll explore the most common "
                    "requirements elicitation challenges in Odoo ERP projects and practical ways to tackle them."
                ),
            ],
            "sections": [
                {
                    "title": "Why requirements elicitation matters in Odoo",
                    "paragraphs": [
                        (
                            "Requirements elicitation is the process of discovering what a business actually needs from "
                            "its ERP system, not what someone thinks it needs. For Odoo, this means mapping real "
                            "workflows (Sales, Inventory, Accounting, HR, and related areas), identifying pain points and "
                            "automation opportunities, and aligning Odoo modules with specific business goals."
                        ),
                        (
                            "When requirements are unclear or poorly documented, the risk increases of scope creep and "
                            "budget overruns, misaligned customizations that don't match real-world usage, and user "
                            "dissatisfaction and low adoption after go-live."
                        ),
                        (
                            "Strong requirements at the start help ensure that your Odoo implementation delivers real "
                            "value, not just technical features."
                        ),
                    ],
                },
                {
                    "title": "Common requirements elicitation challenges in Odoo projects",
                    "paragraphs": [
                        (
                            "1. Unclear or changing business goals. Often, stakeholders say, \"We want Odoo to handle "
                            "everything,\" but they cannot clearly define what \"everything\" means. Without specific "
                            "goals, the project lacks focus and becomes reactive rather than strategic. Signs you're "
                            "facing this challenge: stakeholders describe the system in very broad terms, and "
                            "requirements change frequently during the project."
                        ),
                        (
                            "2. Multiple stakeholders with conflicting priorities. In many organizations, departments "
                            "such as Finance, Sales, and Operations have competing priorities. Sales may push for fast "
                            "quoting and quick approvals, while Finance insists on strict controls and audit trails. "
                            "If these priorities are not reconciled early, the Odoo configuration will satisfy no one "
                            "fully."
                        ),
                        (
                            "3. Lack of documented processes. Many companies still rely on informal, undocumented "
                            "processes. When you ask, \"How do you do this today?\" the answer is often, \"We just do "
                            "it.\" This makes it hard to design an Odoo workflow that truly replaces the old way of "
                            "working and adds measurable efficiency."
                        ),
                        (
                            "4. Assumption-driven requirements. Instead of observing real workflows, some projects jump "
                            "straight to solutions: \"We need this form in Odoo\" or \"We need this report.\" Without "
                            "understanding the underlying business need, you risk building features that go unused or "
                            "create new bottlenecks."
                        ),
                        (
                            "5. Over-expectation of \"one-size-fits-all\" Odoo. Odoo offers many powerful modules, but "
                            "it is not a magic template. Businesses sometimes expect out-of-the-box Odoo to fit their "
                            "unique processes perfectly without any configuration or training. This leads to "
                            "frustration when reality requires tailored setup and user adaptation."
                        ),
                    ],
                },
                {
                    "title": "How to tackle requirements elicitation challenges",
                    "paragraphs": [
                        (
                            "1. Conduct structured discovery workshops. Bring stakeholders together in focused "
                            "sessions to define clear business objectives for the Odoo implementation, list key "
                            "processes (Order to Cash, Procure to Pay, and similar), and agree on success metrics "
                            "(faster reporting, reduced manual data entry, fewer errors). These workshops create shared "
                            "understanding and help prioritize features instead of collecting every nice-to-have."
                        ),
                        (
                            "2. Use AS-IS and TO-BE process mapping. Before configuring Odoo, document how processes "
                            "work today (AS-IS), even if they are informal, and how they should work after Odoo is live "
                            "(TO-BE). This mapping helps you identify gaps and inefficiencies, define what Odoo must "
                            "support or change, and communicate changes to users more clearly."
                        ),
                        (
                            "3. Write user stories, not just feature lists. Instead of \"We need a report,\" write "
                            "user-centric sentences such as: \"As a sales manager, I want to see daily sales by region "
                            "so I can track targets.\" User stories keep the focus on business value and make it easier "
                            "to configure Odoo views and dashboards that match real user needs."
                        ),
                        (
                            "4. Validate requirements with scenarios. For each requirement, test it with realistic "
                            "scenarios: what happens under normal conditions, what if an order is urgent, what if a "
                            "customer wants a discount beyond the standard limit? Scenario-based validation reveals "
                            "edge cases and helps you design Odoo workflows that are robust, not just theoretically "
                            "correct."
                        ),
                        (
                            "5. Control scope with clear prioritization. Use a simple framework such as Must-Have / "
                            "Should-Have / Could-Have to separate core Odoo functionality from nice-to-have "
                            "customizations, focus configuration on the most critical processes first, and plan future "
                            "phases for less urgent features. This keeps the project manageable and allows you to "
                            "deliver visible value quickly."
                        ),
                    ],
                },
                {
                    "title": "Odoo-specific tips for better requirements",
                    "paragraphs": [
                        (
                            "Map modules to business processes. Clearly link each Odoo module (Sales, Inventory, "
                            "Accounting, HR, and so on) to specific business processes so stakeholders understand how "
                            "functions will be distributed. This also makes it easier to demonstrate ROI to "
                            "decision-makers."
                        ),
                        (
                            "Clarify integration needs early. If Odoo must connect with other systems (banking "
                            "platforms, POS, third-party tools), capture integration requirements upfront to avoid "
                            "last-minute surprises. Early planning reduces technical debt and keeps the project on "
                            "schedule."
                        ),
                        (
                            "Define data-migration rules. Decide which historical data is needed, how it will be "
                            "cleaned, and how it will be loaded into Odoo. Many Odoo projects fail to meet expectations "
                            "because of poor data-migration planning, not because of missing features."
                        ),
                        (
                            "Plan for user training and adoption. Good requirements don't just cover features; they "
                            "also include how users will be trained and supported. Proper training and change management "
                            "significantly improve long-term Odoo adoption and user satisfaction."
                        ),
                    ],
                },
                {
                    "title": "Call to action for SOOR Technologies",
                    "paragraphs": [
                        (
                            "If you're planning an Odoo ERP project in Kuwait and want to avoid requirements-related "
                            "delays and misalignment, start with a structured discovery process. At SOOR Technologies, "
                            "we help businesses capture clear, actionable requirements and translate them into "
                            "well-configured Odoo implementations that match real-world workflows in Kuwait and the "
                            "wider Gulf region."
                        ),
                        (
                            "Contact SOOR Technologies today to schedule a requirements-elicitation workshop and ensure "
                            "your Odoo ERP project starts on the right footing."
                        ),
                    ],
                },
            ],
        },
        {
            "slug": "simplifying-product-creation-odoo",
            "card_title": "Simplifying Product Creation in Odoo: A Quick Guide by Soor Technologies",
            "title": "Simplifying Product Creation in Odoo: A Quick Guide by Soor Technologies",
            "subtitle": "Templates, variants, and clean catalogs for teams in Kuwait and beyond.",
            "excerpt": "A concise walkthrough for setting up products, variants, and attributes in Odoo.",
            "date": "Jan 22, 2025",
            "read_time": "8 min read",
            "image": "https://placehold.co/354x212/png?text=Odoo+Product",
            "cover_image": "https://placehold.co/1078x542/png?text=1078x542",
            "lead_paragraphs": [
                (
                    "Setting up products correctly in Odoo is one of the most important steps in any ERP "
                    "implementation. Whether you're managing inventory, sales, purchases, or e-commerce, every "
                    "transaction flows through your product definitions. In this quick guide, Soor Technologies will "
                    "show you how to simplify product creation in Odoo so your system stays accurate, easy to maintain, "
                    "and aligned with your business processes in Kuwait and beyond."
                ),
            ],
            "sections": [
                {
                    "title": "Why product creation matters in Odoo",
                    "paragraphs": [
                        (
                            "In Odoo, a product is not just an item in a catalog: it is the central record that connects "
                            "inventory levels; sales and purchase prices; bill of materials (for manufacturing); "
                            "variants, units of measure, and barcodes; and e-commerce and POS visibility."
                        ),
                        (
                            "If products are created inconsistently or with incomplete information, you'll see issues "
                            "such as incorrect pricing on invoices, stock-level mismatches, and confusing navigation for "
                            "sales and warehouse teams."
                        ),
                        (
                            "Simplifying product creation means standardizing how you create products and using Odoo "
                            "features correctly from day one."
                        ),
                    ],
                },
                {
                    "title": "Step 1: Decide your product strategy",
                    "paragraphs": [
                        (
                            "Before you start creating products, define your product types—for example consumables "
                            "(including services and other non-stock items), stockable products managed in inventory, "
                            "and storable products with tracking such as lot or serial numbers where your operations "
                            "require it."
                        ),
                        (
                            "Set up product categories to group products into buckets such as Raw Materials, Finished "
                            "Goods, Services, or Digital Products. This helps with reporting and warehouse picking."
                        ),
                        (
                            "Decide units of measure (UoM): pick the main unit (for example Each, Kg, or Box) and any "
                            "secondary units (for example a box of 12 units) so purchases and sales can be tracked in "
                            "real-world terms."
                        ),
                    ],
                },
                {
                    "title": "Step 2: Use templates and variants correctly",
                    "paragraphs": [
                        (
                            "Odoo lets you create product templates and variants, which saves time and keeps data "
                            "consistent. On the product template, define shared attributes—for example a laptop "
                            "computer—including category, base price, taxes, and supplier information."
                        ),
                        (
                            "Use variants for colors, sizes, models, or SKUs. Instead of creating separate products "
                            "manually, you set up attributes and attribute values once, and Odoo generates the variants "
                            "automatically. This reduces errors and keeps your catalog easy to manage."
                        ),
                    ],
                },
                {
                    "title": "Step 3: Fill in essential product fields",
                    "paragraphs": [
                        (
                            "When creating a product, focus on the must-have fields. Use a clear, consistent naming "
                            "convention and internal reference (SKU), for example LAP-001 or MTR-005, so users can search "
                            "and identify products quickly."
                        ),
                        (
                            "Complete sales and purchase information: sales price and currency, cost price if you track "
                            "costs, and default supplier where you want auto-fills on purchase orders."
                        ),
                        (
                            "Configure inventory settings: inventory valuation approach (such as standard, real time, "
                            "or FIFO where applicable), reordering rules when auto-replenishment should run, and "
                            "barcodes and packaging when relevant—including internal barcodes and packaging units such "
                            "as a box of 12."
                        ),
                        (
                            "By filling in these fields systematically, you avoid manual overrides later and keep "
                            "reports and price lists accurate."
                        ),
                    ],
                },
                {
                    "title": "Step 4: Keep product data clean and organized",
                    "paragraphs": [
                        (
                            "Over time, catalogs grow and become messy. To simplify product creation and maintenance, "
                            "use a naming and numbering standard—for example prefixes by category such as RAW-, FIN-, "
                            "or SRV-, and consistent formatting for SKUs."
                        ),
                        (
                            "Use product categories and tags: group products into logical categories such as Office "
                            "Supplies, IT Equipment, or Services, and use tags for quick filters."
                        ),
                        (
                            "Review and archive old products. Instead of deleting products with history, mark them as "
                            "inactive so old documents such as invoices and sales orders stay intact but the product "
                            "is no longer visible in new transactions."
                        ),
                        (
                            "Standardize product templates for similar items—for example all services can follow the "
                            "same template with the same pricing and tax rules, while finished goods follow another "
                            "template."
                        ),
                    ],
                },
                {
                    "title": "Step 5: Train your team on product creation best practices",
                    "paragraphs": [
                        (
                            "Even the best Odoo setup can break if users create products incorrectly. Soor Technologies "
                            "recommends training sessions for sales and warehouse teams, purchasing managers, and admins "
                            "who create or modify products."
                        ),
                        (
                            "Provide a simple checklist for new products: name and SKU, category, sales price and cost, "
                            "inventory settings, and barcodes or packaging when needed."
                        ),
                        (
                            "Consider a small product creation team: in many companies, only one or two people are "
                            "allowed to create new product templates, while others use existing ones. This keeps the "
                            "catalog clean and standardized."
                        ),
                    ],
                },
                {
                    "title": "Odoo-specific tips from Soor Technologies",
                    "paragraphs": [
                        (
                            "Use imports for bulk products. If you have more than a hundred SKUs, use Odoo's import "
                            "feature (CSV or Excel) with a well-structured template so you do not create products one by "
                            "one."
                        ),
                        (
                            "Link products to your chart of accounts so revenues and costs map to the right accounts "
                            "and your financial reports reflect reality."
                        ),
                        (
                            "Think ahead about variants versus separate products. Before creating many individual "
                            "products, ask whether an item can be a variant of an existing template. This reduces clutter "
                            "and makes reporting easier."
                        ),
                        (
                            "Test product creation in a staging environment first. If you are customizing product "
                            "workflows or automations, validate them in a non-live Odoo environment before applying "
                            "changes to production."
                        ),
                    ],
                },
                {
                    "title": "Call to action for Soor Technologies",
                    "paragraphs": [
                        (
                            "If your team is struggling with messy product data, inconsistent pricing, or slow catalog "
                            "setup in Odoo, Soor Technologies can help simplify product creation for your business in "
                            "Kuwait."
                        ),
                        (
                            "From standardizing product templates to training your team and cleaning up existing "
                            "catalogs, we make sure your Odoo system is easy to use and aligned with your operations."
                        ),
                        (
                            "Contact Soor Technologies today to schedule a free Odoo consultation and product creation "
                            "review session."
                        ),
                    ],
                },
            ],
        },
        {
            "slug": "odoo-first-sales-quotation",
            "card_title": "Getting Started with Odoo: How to Create Your First Sales Quotation in Minutes",
            "title": "Getting Started with Odoo: How to Create Your First Sales Quotation in Minutes",
            "subtitle": "Order to Cash in Odoo—from draft quote to invoice—for Kuwait and the Gulf.",
            "excerpt": "Step-by-step: from customer to confirmed quotation using Sales and optional CRM.",
            "date": "Jan 28, 2025",
            "read_time": "10 min read",
            "image": "https://placehold.co/354x212/png?text=Quotation",
            "cover_image": "https://placehold.co/1078x542/png?text=Quotation",
            "lead_paragraphs": [
                (
                    "If you're new to Odoo, one of the easiest ways to get started is by creating your first sales "
                    "quotation. A quotation in Odoo is not just a simple price list: it is a structured sales document "
                    "that links your customers, products, pricing, and tax rules in one place. In this in-depth guide, "
                    "Soor Technologies will walk you through how to create your first sales quotation in Odoo step by "
                    "step, so you can start using Odoo confidently for your business in Kuwait and the wider Gulf "
                    "region."
                ),
            ],
            "sections": [
                {
                    "title": "Why sales quotations matter in Odoo",
                    "paragraphs": [
                        (
                            "In Odoo, a sales quotation plays a central role in the Order to Cash cycle. It helps you "
                            "present professional, formatted offers to customers; define quantities, unit prices, "
                            "discounts, and taxes clearly; track which quotes are pending, approved, or rejected; and "
                            "later convert quotations into sales orders and then into invoices."
                        ),
                        (
                            "Using quotations correctly from the beginning helps you avoid manual pricing mistakes, "
                            "keep a clear audit trail of offers sent to each customer, and build a clean, repeatable "
                            "sales workflow that your team can follow every time."
                        ),
                        (
                            "For businesses in Kuwait, Odoo quotations also make it easy to handle VAT-inclusive "
                            "pricing, multi-currency offers, and multi-branch operations in a consistent way."
                        ),
                    ],
                },
                {
                    "title": "Step 1: Navigate to the Sales app",
                    "paragraphs": [
                        (
                            "Before you create your first quotation, make sure you're in the right place. Log in to "
                            "your Odoo instance using your credentials. On the main dashboard, click the Sales app "
                            "icon (usually represented by a shopping cart or invoice icon). In the Sales module, make "
                            "sure you are in the Quotations view. In Odoo, quotations are often listed under a "
                            "Quotations tab or menu on the left-hand side."
                        ),
                        (
                            "If this is your first time in Odoo, confirm that at least one customer and one product "
                            "exist in the system. If not, create them first (we explain that briefly in the next step)."
                        ),
                    ],
                },
                {
                    "title": "Step 2: Create a new customer (if needed)",
                    "paragraphs": [
                        (
                            "Odoo quotations are always linked to a customer record. If you don't have one yet, while "
                            "in the Sales app click Create (or New Quotation). In the Customer field, start typing the "
                            "customer's name. If the customer doesn't exist, click Create a new customer."
                        ),
                        (
                            "Fill in basic details such as customer name, email address, phone number, and address "
                            "(billing and shipping, if different). By creating a proper customer record, you'll later be "
                            "able to track all quotations and sales for that customer and apply customer-specific "
                            "pricelists and payment terms automatically."
                        ),
                    ],
                },
                {
                    "title": "Step 3: Start a new quotation",
                    "paragraphs": [
                        (
                            "Once you've selected or created a customer, Odoo will open the quotation form. You'll "
                            "see customer information at the top; quotation date and expiration date (you can change "
                            "these if needed); pricelist (if configured) that defines how prices are calculated; and an "
                            "empty product lines section where you will add items."
                        ),
                        (
                            "At this stage, your quotation is in draft mode and not yet sent to the customer. You can "
                            "save it and come back later if you're not ready to send it immediately."
                        ),
                    ],
                },
                {
                    "title": "Step 4: Add products to the quotation",
                    "paragraphs": [
                        (
                            "In the Order Lines (or Product Lines) section, click Add a product (or Add a line). Start "
                            "typing the product name or internal reference (SKU) and select the correct item from the "
                            "dropdown. For each selected product, Odoo will automatically fill the product name, unit of "
                            "measure, unit price (from the product's sales price or pricelist), and taxes (based on the "
                            "product's tax template)."
                        ),
                        (
                            "You can then adjust the quantity to match what the customer needs; change the unit price if "
                            "this is a special case (for example a one-time discount); add a discount (percentage or "
                            "fixed amount) in the Discount field, if your Odoo setup allows it; and add notes specific to "
                            "that line, such as delivery conditions or remarks."
                        ),
                        (
                            "If your quotation includes multiple products, repeat the process and add as many lines as "
                            "needed. Odoo will keep the subtotal, taxes, and total updated in real time."
                        ),
                    ],
                },
                {
                    "title": "Step 5: Customize quotation details",
                    "paragraphs": [
                        (
                            "Modern Odoo versions let you customize the quotation to match your brand and terms. Set "
                            "quotation date and validity: use a clear expiration date (for example valid for 7 days) "
                            "to encourage timely decisions."
                        ),
                        (
                            "Assign payment terms if your company has standards (for example Net 30 days) so the customer "
                            "understands when to pay after order confirmation. Add delivery and shipping details such "
                            "as delivery notes, delivery method, or shipping remarks if relevant."
                        ),
                        (
                            "Use the Internal Notes field (if available) to add comments for your team that won't "
                            "appear in the customer-facing PDF."
                        ),
                    ],
                },
                {
                    "title": "Step 6: Review pricing and taxes",
                    "paragraphs": [
                        (
                            "Before sending the quotation, double-check the numbers. Look at the Summary section at "
                            "the bottom of the form: subtotal, taxes (for example VAT, if applicable), and total amount."
                        ),
                        (
                            "Confirm that prices match your agreed commercial terms, taxes are applied correctly for "
                            "your region (for example Kuwaiti VAT settings), and any discounts are applied only where "
                            "intended—not to the whole quotation by mistake."
                        ),
                        (
                            "If something looks wrong, go back to product settings to adjust the sales price or tax "
                            "template, or check pricelists to ensure the right price list is assigned to this customer "
                            "or quotation."
                        ),
                    ],
                },
                {
                    "title": "Step 7: Save, preview, and send the quotation",
                    "paragraphs": [
                        (
                            "When everything looks correct, click Save to store the quotation in Odoo. The quotation "
                            "will appear in your Quotations list with a status such as Draft or Quotation Sent, depending "
                            "on your workflow."
                        ),
                        (
                            "To send it to the customer, click Send by Email (or Send & Print, depending on your "
                            "version). Odoo will open a customizable email composer with a clear subject line (for "
                            "example Your Odoo Sales Quotation), a short message body, and the quotation attached as a "
                            "PDF."
                        ),
                        (
                            "Edit the subject and message if needed—for example to say that the quotation is attached "
                            "for review and confirmation before proceeding with the order—then click Send. Your customer "
                            "receives a professional-looking PDF quotation, and the record stays in Odoo for follow-up."
                        ),
                    ],
                },
                {
                    "title": "Step 8: Convert quotation to sales order",
                    "paragraphs": [
                        (
                            "If the customer approves the quotation, open it in Odoo and click Confirm Quotation (or "
                            "Create Sales Order, depending on labels in your version). Odoo will create a sales order "
                            "linked to the same customer and products and carry over the pricing, quantities, and notes "
                            "from the original quotation."
                        ),
                        (
                            "From there, your team can manage delivery via stock or shipping rules, confirm delivery "
                            "orders if inventory is involved, and later create an invoice (manually or automatically) "
                            "based on the sales order."
                        ),
                        (
                            "This end-to-end flow ensures that everything from the initial quotation to the final "
                            "invoice is traceable and consistent."
                        ),
                    ],
                },
                {
                    "title": "Advanced tips for better quotation management in Odoo",
                    "paragraphs": [
                        (
                            "1. Use pricelists for multiple customers. Instead of manually changing prices for every "
                            "customer, create different pricelists—for regular customers, VIP or long-term clients, or "
                            "regions and branches—and assign the right pricelist to each customer or quotation so Odoo "
                            "auto-calculates prices."
                        ),
                        (
                            "2. Standardize quotation templates. Design a standard quotation template (header, logo, "
                            "terms, footer) so every quote looks professional and consistent, with clear payment terms, "
                            "validity period, and contact details."
                        ),
                        (
                            "3. Automate approval workflows. If your company needs manager approval for high-value "
                            "quotations, configure approval workflows in Odoo so quotations move through defined steps "
                            "before being sent."
                        ),
                        (
                            "4. Track quotation statuses. Use Odoo's status tags (for example Draft, Sent, Expired, "
                            "Won, Lost) to track which quotes are pending, which have been converted into orders, and "
                            "which have been rejected—helping you analyze your sales pipeline and conversion rates."
                        ),
                        (
                            "5. Test in a staging environment. If you're customizing quotation templates, email "
                            "layouts, or approval rules, test everything in a non-live staging environment first. This "
                            "prevents mistakes in your production system and keeps real customer data safe."
                        ),
                    ],
                },
                {
                    "title": "Call to action for Soor Technologies",
                    "paragraphs": [
                        (
                            "If you're just getting started with Odoo and want to make sure your sales quotations, "
                            "orders, and invoices are set up correctly, Soor Technologies can help. We provide Odoo "
                            "setup, configuration, and training services tailored to businesses in Kuwait and the Gulf "
                            "region, so your team can create quotations quickly and accurately from day one."
                        ),
                        (
                            "Contact Soor Technologies today to schedule a free Odoo onboarding session and learn how "
                            "to create your first sales quotation and many more with confidence."
                        ),
                    ],
                },
            ],
        },
        {
            "slug": "effective-brand-storytelling",
            "card_title": "5 strategies for effective brand storytelling",
            "title": "5 strategies for effective brand storytelling",
            "subtitle": "Purpose, customer focus, and simple structure for human-centered brand stories.",
            "excerpt": (
                "Products and features alone are not enough—a clear, authentic story builds trust and long-term "
                "relationships with your audience."
            ),
            "date": "Jan 28, 2025",
            "read_time": "9 min read",
            "image": "https://placehold.co/354x212/png?text=Brand",
            "cover_image": "https://placehold.co/1078x542/png?text=Brand",
            "lead_paragraphs": [
                (
                    "In today's crowded digital world, products and features alone are not enough to win customer "
                    "loyalty. What truly sticks in people's minds is a story. A brand that tells a clear, authentic, and "
                    "emotionally engaging story can stand out from competitors, build trust, and create long-term "
                    "relationships with its audience."
                ),
                (
                    "For businesses that want to grow through content, marketing, and reputation, mastering brand "
                    "storytelling is not optional—it is essential. The good news is that effective brand storytelling "
                    "follows a few repeatable strategies. Here are five practical, human-centered strategies you can use "
                    "to build your own compelling brand story."
                ),
            ],
            "sections": [
                {
                    "title": "1. Start with who you are, not just what you sell",
                    "paragraphs": [
                        (
                            "Many brands make the same mistake: they jump straight into what we do and what we offer "
                            "without explaining who they are and why they exist. Effective brand storytelling begins "
                            "with your core identity."
                        ),
                        (
                            "Ask yourself: What problem do you genuinely want to solve? Why did you start this business "
                            "in the first place? What values drive your team every day? Then translate those answers into "
                            "a simple, human statement. Instead of leading with technical features, open with purpose. "
                            "For example, instead of saying \"We provide Odoo ERP implementation,\" you might say "
                            "\"We help businesses in Kuwait work smarter by simplifying their daily operations through "
                            "smart technology.\""
                        ),
                        (
                            "When your audience understands your values and motivations, they are more likely to "
                            "remember you and feel connected, even if they're not ready to buy yet."
                        ),
                    ],
                },
                {
                    "title": "2. Put your customer at the center of the story",
                    "paragraphs": [
                        (
                            "The best brand stories are not about the company; they are about the customer. Effective "
                            "brand storytelling focuses on the customer's journey: their challenges, their goals, and "
                            "how your brand supports them along the way."
                        ),
                        (
                            "To do this, think in scenarios: What does a typical customer deal with before discovering "
                            "your brand? What pain points or frustrations do they face? How does your product, service, "
                            "or advice make their life easier, safer, or more efficient? Use real-world situations your "
                            "audience can recognize. For example, instead of only listing features like custom Odoo "
                            "workflows, describe how a small business owner in Kuwait finally stops wasting hours on "
                            "manual spreadsheets and starts trusting their inventory data."
                        ),
                        (
                            "When customers see themselves in your story, they feel seen. That emotional connection is "
                            "far more powerful than a bullet list of benefits."
                        ),
                    ],
                },
                {
                    "title": "3. Be consistent, but not robotic",
                    "paragraphs": [
                        (
                            "Consistency is essential for brand storytelling, but it should not feel mechanical or "
                            "repetitive. Being consistent means keeping the same tone, values, and overall message across "
                            "your website, blogs, social posts, and emails—but within that consistency, there is room for "
                            "variety, personality, and natural flow."
                        ),
                        (
                            "A brand that feels too scripted or too on-message starts to sound artificial. A brand that "
                            "feels human admits imperfections, learns from mistakes, and sometimes uses a lighter tone, "
                            "a bit of humor, or a candid observation."
                        ),
                        (
                            "To keep your storytelling consistent yet natural: decide on a clear tone (professional, "
                            "friendly, confident, or approachable) and stick to it; use real examples and case-style "
                            "stories instead of generic slogans; and let your content reflect genuine experience, not "
                            "only polished marketing lines. When your audience senses authenticity, they are more likely "
                            "to trust you and share your story with others."
                        ),
                    ],
                },
                {
                    "title": "4. Use simple structure, not complex jargon",
                    "paragraphs": [
                        (
                            "Great brand storytelling is easy to follow. It does not need complicated language or "
                            "industry buzzwords to work. In fact, the more simply you tell your story, the more clearly "
                            "it travels."
                        ),
                        (
                            "Good brand stories often follow a simple structure: Situation—what is happening in the "
                            "customer's life or business? Struggle—what is the problem or challenge? Solution—how does "
                            "your brand help? Outcome—what changes after working with you? You can apply this structure "
                            "to your homepage, blogs, case studies, and social posts."
                        ),
                        (
                            "For example, a blog post might start by describing a common frustration in managing business "
                            "data, then show how clear processes and the right tools make a difference, and end with a "
                            "realistic, human outcome rather than a perfect overnight success promise. When your story "
                            "is easy to read and easy to understand, more people will actually finish it and remember "
                            "it."
                        ),
                    ],
                },
                {
                    "title": "5. Connect your story to real places and people",
                    "paragraphs": [
                        (
                            "People remember people, not logos. They remember faces, voices, and names. To make your "
                            "brand story feel human, include real people, real places, and real moments whenever you "
                            "can."
                        ),
                        (
                            "Share short stories about your team, your clients, or your daily work environment. Mention "
                            "the city or region where your business operates and how local needs shape what you do. "
                            "Highlight real projects, not only generic descriptions of successful implementations."
                        ),
                        (
                            "You do not need to sound like a documentary, but a few concrete details—like a small retail "
                            "business in Kuwait City struggling with inventory counts, or a family-run manufacturing "
                            "company tired of manual order tracking—help your audience place your story in the real "
                            "world. When your brand story feels grounded in real life, it becomes more relatable, more "
                            "memorable, and easier to trust."
                        ),
                    ],
                },
                {
                    "title": "How Soor Technologies tells its story",
                    "paragraphs": [
                        (
                            "At Soor Technologies, brand storytelling is not separate from service delivery. The story "
                            "is built around real businesses in Kuwait and the Gulf region that need clearer processes, "
                            "smarter workflows, and technology that actually fits their daily operations. Instead of "
                            "only talking about Odoo as a platform, the focus is on how it helps people and teams work "
                            "with less stress and more confidence."
                        ),
                        (
                            "Every project, every blog, and every client interaction becomes part of a larger story: "
                            "about trust, clarity, and long-term partnership. The goal is not to sound like a perfect, "
                            "polished machine but to feel like a real, human-driven business that understands local "
                            "challenges and thinks ahead."
                        ),
                    ],
                },
                {
                    "title": "Call to action",
                    "paragraphs": [
                        (
                            "If you want your brand to stand out through clear, authentic storytelling, start with "
                            "these five strategies and revisit them with every new piece of content. You do not need to "
                            "sound like a sales pitch—you only need to be honest, clear, and thoughtful."
                        ),
                        (
                            "If you would like help shaping your brand story for your website, blogs, or social media, "
                            "reach out to Soor Technologies. We work with businesses in Kuwait and the Gulf region to "
                            "turn everyday experiences into compelling, human-centered brand stories that connect with "
                            "the right audience."
                        ),
                        (
                            "Contact Soor Technologies today to talk about your brand narrative and how we can support "
                            "your content, website, and marketing with a clearer, more authentic story."
                        ),
                    ],
                },
            ],
        },
        {
            "slug": "digital-transformation-odoo",
            "card_title": "Digital transformation without the chaos",
            "title": "Digital transformation without the chaos",
            "subtitle": "Vision, phases, and people—for predictable change in Kuwait and the Gulf.",
            "excerpt": (
                "How phased rollouts, clear ownership, and training keep teams productive when you modernize systems "
                "and processes."
            ),
            "date": "Feb 2, 2025",
            "read_time": "11 min read",
            "image": "https://placehold.co/354x212/png?text=Transform",
            "cover_image": "https://placehold.co/1078x542/png?text=Transform",
            "lead_paragraphs": [
                (
                    "Digital transformation is no longer a buzzword. For businesses in Kuwait and across the Gulf, it is "
                    "a necessary step to stay competitive, efficient, and relevant. Yet, many companies start the "
                    "journey with high hopes and quickly end up dealing with confusion, delays, and frustrated teams. "
                    "The good news is that digital transformation does not have to be chaotic. With the right approach, "
                    "it can be clear, structured, and even predictable."
                ),
                (
                    "This blog from Soor Technologies will show you how to pursue digital transformation without the "
                    "usual chaos, focusing on real-world strategies that work for growing businesses and established "
                    "organizations alike."
                ),
            ],
            "sections": [
                {
                    "title": "Why digital transformation often feels chaotic",
                    "paragraphs": [
                        (
                            "Before you can fix the chaos, you need to understand where it comes from. Common reasons "
                            "include: no clear goal—many companies start by buying digital tools or ERP systems without "
                            "agreeing on what success looks like, so every new feature or system feels like a detour."
                        ),
                        (
                            "Too many priorities at once: digital transformation can mean anything from automating "
                            "inventory to upgrading CRM, paying bills online, or moving to cloud-based collaboration. "
                            "When teams try to do everything at the same time, nothing gets completed properly."
                        ),
                        (
                            "Unclear roles and responsibilities mean people do not know who is responsible for decisions, "
                            "approvals, or training, so everything depends on who is available today—creating "
                            "bottlenecks and confusion."
                        ),
                        (
                            "Changing requirements mid-project: stakeholders often discover new needs only after "
                            "implementation has started. Without a structured process to manage changes, every new "
                            "request becomes a disruption."
                        ),
                        (
                            "Lack of training and support: the best technology fails when users do not understand how to "
                            "use it or do not feel supported during the shift."
                        ),
                        (
                            "When these issues combine, digital transformation starts to feel like a never-ending "
                            "project with no clear end. But the problem is not technology; it is how the change is "
                            "managed."
                        ),
                    ],
                },
                {
                    "title": "1. Start with a clear vision, not a tool",
                    "paragraphs": [
                        (
                            "The first step to avoiding chaos is to reverse the common order many companies follow. "
                            "Instead of \"what system should we buy?\", start with \"what do we want to achieve?\" Ask "
                            "questions like: What processes are causing the most delays or errors? Where do employees "
                            "waste the most time on manual work? What information is the hardest to get, yet most "
                            "important for decisions?"
                        ),
                        (
                            "Once you define your top priorities, you can choose tools that support those goals, not the "
                            "other way around. For example: if sales teams struggle with quote and order errors, focus "
                            "on a clean sales and quotation workflow. If inventory counts are always wrong, prioritize "
                            "a system that tracks real-time stock and integrates with sales and purchases."
                        ),
                        (
                            "When your digital transformation is guided by a clear vision, every new feature or module "
                            "serves a defined purpose, and the project feels focused instead of messy."
                        ),
                    ],
                },
                {
                    "title": "2. Plan in phases, not in one big bang",
                    "paragraphs": [
                        (
                            "Chaotic transformations often try to fix everything at once. The opposite of chaos is "
                            "phased execution. Break your transformation into manageable stages—for example Phase 1: "
                            "core processes (finance, inventory, sales); Phase 2: customer-facing systems (e-commerce, "
                            "CRM, service management); Phase 3: advanced analytics and automation (dashboards, "
                            "reporting, approvals)."
                        ),
                        (
                            "Within each phase, define a small, concrete milestone (for example, create products and "
                            "quotations in Odoo within four weeks), set a timeline and assign clear responsibilities, "
                            "and agree on a simple way to measure success (for example, reduce manual data entry by "
                            "fifty percent or cut invoice processing time to two days)."
                        ),
                        (
                            "By moving in phases, you give teams time to learn, adapt, and stabilize before moving to the "
                            "next step. This turns an overwhelming project into a series of achievable goals."
                        ),
                    ],
                },
                {
                    "title": "3. Align people, not just software",
                    "paragraphs": [
                        (
                            "Technology does not transform a business—people do. To avoid chaos, make sure your teams "
                            "are involved early and consistently. Involve key stakeholders from different departments: "
                            "finance, sales, operations, and IT all see the business differently; bring them together at "
                            "the start to share their needs and expectations."
                        ),
                        (
                            "Appoint clear owners: decide who will own the budget, make decisions about priorities, and "
                            "approve changes and new requirements. This prevents endless discussions and last-minute "
                            "decisions."
                        ),
                        (
                            "Communicate the why and the how: people accept change more easily when they understand why "
                            "it is happening and how it will affect their daily work. Use simple language and real-world "
                            "examples instead of technical jargon. When teams feel part of the journey, resistance "
                            "decreases and adoption increases."
                        ),
                    ],
                },
                {
                    "title": "4. Use the right tools in the right order",
                    "paragraphs": [
                        (
                            "Chaotic transformations often jump between tools, hoping one will solve everything. The "
                            "smarter approach is to choose the right tool for the right stage—for example, start with a "
                            "core ERP system such as Odoo that can handle finance, inventory, and sales, then add "
                            "complementary tools (e-mail marketing, CRM, e-commerce, or field service) only when the "
                            "core is stable."
                        ),
                        (
                            "To avoid tool overload, ask whether a new system talks to your existing one; avoid tools "
                            "that create extra manual work (like exporting data to Excel every day); and prefer "
                            "platforms that can grow with your business instead of forcing you to replace them later."
                        ),
                        (
                            "When your tools follow a logical order, your digital transformation feels like a coherent "
                            "plan, not a collection of random experiments."
                        ),
                    ],
                },
                {
                    "title": "5. Build a simple roadmap and stick to it",
                    "paragraphs": [
                        (
                            "A clear roadmap is the antidote to chaos. Even a simple one-page plan can make a big "
                            "difference. Your digital transformation roadmap can include: What—the main capabilities "
                            "you want to build (for example digital invoicing, stock management, electronic approvals); "
                            "When—a rough timeline (for example Q2: core ERP setup; Q3: rollout to branches); Who—the "
                            "main people responsible for each step; and how to measure success—a few key metrics (for "
                            "example faster order processing, fewer errors, fewer manual reports)."
                        ),
                        (
                            "Then review the roadmap regularly (monthly or quarterly), allow small adjustments but "
                            "avoid big last-minute changes, and celebrate milestones when they are achieved—even if they "
                            "are small."
                        ),
                        (
                            "A visible roadmap gives everyone a sense of direction and progress, which reduces the "
                            "feeling of chaos."
                        ),
                    ],
                },
                {
                    "title": "6. Invest in training and support, not just installation",
                    "paragraphs": [
                        (
                            "Many companies think digital transformation ends when the software is installed. In "
                            "reality, it begins when people start using it. To keep the process calm and predictable, "
                            "plan training sessions for each user group (admins, finance, warehouse, sales); provide "
                            "simple manuals, checklists, or short video guides; and offer a clear channel for support "
                            "(for example a dedicated contact or helpdesk)."
                        ),
                        (
                            "When users can quickly get answers to their questions, they feel confident instead of "
                            "frustrated. Chaos tends to rise when people are stuck, not when they have the support they "
                            "need."
                        ),
                    ],
                },
                {
                    "title": "How Soor Technologies brings order to digital transformation",
                    "paragraphs": [
                        (
                            "At Soor Technologies, we help businesses in Kuwait and the wider Gulf region transform "
                            "digitally without the usual chaos. Instead of pushing technology for its own sake, we focus "
                            "on clarifying what success looks like for each business, designing a step-by-step roadmap "
                            "that fits current operations, and implementing systems that are easy to use and easy to "
                            "support."
                        ),
                        (
                            "Our goal is not to create a perfect, theoretical system. It is to deliver a practical, "
                            "stable environment that teams can actually use every day."
                        ),
                    ],
                },
                {
                    "title": "Call to action",
                    "paragraphs": [
                        (
                            "If you are considering digital transformation but want to avoid confusion, delays, and "
                            "frustration, start with a simple, clear plan. You do not need to do everything at once—you "
                            "only need to start with the right priorities and the right support."
                        ),
                        (
                            "Contact Soor Technologies today to discuss how we can help you pursue digital transformation "
                            "without the chaos—whether that means implementing Odoo, redesigning workflows, or guiding your "
                            "team through the full change process."
                        ),
                    ],
                },
            ],
        },
        {
            "slug": "scaling-operations-odoo",
            "card_title": "Scaling operations with Odoo at the core",
            "title": "Scaling operations with Odoo at the core",
            "subtitle": "One integrated core for sales, stock, finance, and HR as you grow in Kuwait and the Gulf.",
            "excerpt": (
                "Connect sales, inventory, finance, and more in one Odoo backbone—fewer spreadsheets, clearer control."
            ),
            "date": "Feb 8, 2025",
            "read_time": "12 min read",
            "image": "https://placehold.co/354x212/png?text=Scale",
            "cover_image": "https://placehold.co/1078x542/png?text=Scale",
            "lead_paragraphs": [
                (
                    "For growing businesses in Kuwait and across the Gulf, one of the biggest challenges is scaling "
                    "operations without losing control. As you add more customers, products, branches, or services, "
                    "manual processes quickly become unmanageable. Spreadsheets overflow, communication gaps grow, and "
                    "simple tasks like checking stock or sending invoices start taking longer than they should."
                ),
                (
                    "This is where Odoo can play a central role. When you place Odoo at the core of your operations, it "
                    "becomes the backbone that connects sales, inventory, finance, HR, and more. This blog from Soor "
                    "Technologies will show you how to scale your business with Odoo at the center, while keeping "
                    "everything clear, integrated, and easy to manage."
                ),
            ],
            "sections": [
                {
                    "title": "Why Odoo is the right core for growing operations",
                    "paragraphs": [
                        (
                            "Odoo is not just an ERP. It is a flexible suite of applications that can grow with your "
                            "business. Instead of replacing your system every time your needs change, you can expand "
                            "Odoo by adding new modules or apps as you need them: Sales and CRM to manage customer "
                            "relationships; inventory and purchasing to track stock and orders; accounting to close books "
                            "faster and with fewer errors; HR and payrolls to manage teams and onboarding; e-commerce and "
                            "POS to sell online and from physical locations."
                        ),
                        (
                            "When you build your operations around Odoo, all of these functions use the same data, the "
                            "same customers, and the same products. This eliminates duplicate entries, inconsistent "
                            "records, and messy spreadsheets that break as you grow."
                        ),
                    ],
                },
                {
                    "title": "1. Start with a clean, scalable foundation",
                    "paragraphs": [
                        (
                            "The first step to scaling operations is not to add features—it is to set up a clean base. "
                            "For Odoo, this means: define a consistent chart of accounts so your financial data is clear "
                            "and easy to report on; create a clear product catalog including categories, units of measure, "
                            "and variants; and standardize customer and vendor records so every team works from the same "
                            "information."
                        ),
                        (
                            "When these foundations are in place, scaling becomes easier. New branches, new products, "
                            "and new users can be added without recreating the entire setup from scratch."
                        ),
                    ],
                },
                {
                    "title": "2. Automate repetitive tasks from the start",
                    "paragraphs": [
                        (
                            "As you grow, manual work becomes the biggest bottleneck. Odoo helps you scale by automating "
                            "many of the tasks that used to be done in spreadsheets or via email. Examples include "
                            "quotations and sales orders that move from quote to order to invoice with minimal intervention; "
                            "inventory movements that update stock levels in real time when sales, purchases, or internal "
                            "transfers happen; accounting entries that are created automatically when you confirm sales, "
                            "purchases, or journal entries; and reorder rules that trigger purchase orders when stock "
                            "reaches a minimum level, reducing stockouts."
                        ),
                        (
                            "By configuring these automations early, your team can focus on higher-value work instead of "
                            "checking spreadsheets and updating numbers manually."
                        ),
                    ],
                },
                {
                    "title": "3. Use the same data across all departments",
                    "paragraphs": [
                        (
                            "One of the main reasons scaling operations feels chaotic is that different teams use "
                            "different data sources. Sales might track orders in one place, inventory in another, and "
                            "finance in a third. When you place Odoo at the core, everyone works from the same data."
                        ),
                        (
                            "Key benefits: when a sales order is created, inventory is reserved automatically. When an "
                            "invoice is generated, accounting is updated in real time. When HR records a new employee, "
                            "payroll and user access can be created from the same record."
                        ),
                        (
                            "This single-source-of-truth model reduces errors, speeds up closing periods, and makes "
                            "management reporting far more accurate."
                        ),
                    ],
                },
                {
                    "title": "4. Add modules as you grow, not because they look cool",
                    "paragraphs": [
                        (
                            "Odoo offers many modules, but scaling effectively means adding them for a clear business "
                            "reason, not just because they are available."
                        ),
                        (
                            "A smarter approach: start with core modules that match your most critical needs—Sales, "
                            "Inventory, Accounting, and Purchasing. Once these are stable and your team is comfortable, "
                            "add CRM, Projects, HR, or e-commerce when you truly need them."
                        ),
                        (
                            "Avoid over-customizing every module at the beginning; instead, standardize on Odoo's "
                            "built-in workflows where possible. This keeps your Odoo setup simple and maintainable, even "
                            "as your business grows larger and more complex."
                        ),
                    ],
                },
                {
                    "title": "5. Scale by locations, not by chaos",
                    "paragraphs": [
                        (
                            "If you operate in multiple branches, warehouses, or franchises, Odoo can help you scale "
                            "operations in a structured way: define warehouses and locations for each branch or storage "
                            "area so stock movements are tracked clearly; use inter-company rules when you have multiple "
                            "legal entities or subsidiaries; and set up multi-company and multi-currency support if you "
                            "serve international customers."
                        ),
                        (
                            "Instead of treating each location as a separate, disconnected unit, you manage them from a "
                            "single Odoo instance with clear rules and controls. This makes it easier to compare "
                            "performance, share resources, and grow in a controlled way."
                        ),
                    ],
                },
                {
                    "title": "6. Let reporting and dashboards guide your growth",
                    "paragraphs": [
                        (
                            "As operations scale, the only way to stay on top of everything is through clear visibility. "
                            "Odoo's built-in reporting and dashboards help you do this without extra tools."
                        ),
                        (
                            "Common reports and dashboards that help you scale include: sales and margin reports by "
                            "product, customer, or salesperson; inventory and stock-valuation reports to track stock "
                            "levels and cash tied up in inventory; financial statements that can be generated quickly at "
                            "the end of each period; and KPIs and dashboards on your main screen showing key metrics like "
                            "overdue invoices, open orders, or low-stock items."
                        ),
                        (
                            "When you make data-driven decisions, your growth is guided by facts, not guesswork. This "
                            "reduces the risk of sudden bottlenecks or cash-flow surprises."
                        ),
                    ],
                },
                {
                    "title": "7. Train teams once, then keep updating once a month",
                    "paragraphs": [
                        (
                            "Scaling does not only mean adding more users—it also means helping existing teams use Odoo "
                            "effectively. To support smooth growth, train your core users first (admin, finance, "
                            "warehouse, sales); create simple, easy-to-follow training materials or checklists; and hold "
                            "short monthly refresh sessions to introduce new modules or best practices."
                        ),
                        (
                            "Consistent training keeps your team confident and reduces the number of \"What do I do "
                            "now?\" moments that often paralyze growth."
                        ),
                    ],
                },
                {
                    "title": "How Soor Technologies helps you scale with Odoo",
                    "paragraphs": [
                        (
                            "At Soor Technologies, we help businesses in Kuwait and the Gulf region place Odoo at the "
                            "core of their operations. Rather than treating Odoo as a one-time project, we design Odoo "
                            "to be the long-term backbone of your business."
                        ),
                        (
                            "Our focus is on: building a clean, scalable foundation; automating repetitive tasks; "
                            "ensuring all departments use the same data; and training your team so they can grow with the "
                            "system. This makes it easier for you to add new products, new branches, or new customers "
                            "without constant fear of losing control."
                        ),
                    ],
                },
                {
                    "title": "Call to action",
                    "paragraphs": [
                        (
                            "If you are ready to scale your operations but want to avoid the chaos that often comes "
                            "with growth, start by building a clear, integrated system. Odoo, when implemented and used "
                            "correctly, can become the stable core that supports your expansion across Kuwait and beyond."
                        ),
                        (
                            "Contact Soor Technologies today to discuss how we can help you scale your operations with "
                            "Odoo at the core. Whether you are just starting or already using Odoo, we can help you turn "
                            "it into a powerful engine for sustainable growth."
                        ),
                    ],
                },
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
