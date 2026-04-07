/**
 * Google Website Translator: compact trigger + flyout (AR/EN).
 * Resets all goog* translation cookies/storage; optional Odoo /ar/ URL strip for English.
 */
(function () {
    "use strict";

    var COOKIE = "googtrans";
    var SOURCE_LANG = "en";

    function getCookie(name) {
        var m = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([.$?*|{}()[\]\\/+^])/g, "\\$1") + "=([^;]*)"));
        return m ? decodeURIComponent(m[1]) : "";
    }

    function getActiveTargetLang() {
        var v = getCookie(COOKIE);
        if (!v || v === "/en/en" || v === "/auto/en") {
            return SOURCE_LANG;
        }
        var parts = v.split("/").filter(Boolean);
        if (parts.length < 2) {
            return SOURCE_LANG;
        }
        var target = parts[parts.length - 1];
        return target === "ar" ? "ar" : SOURCE_LANG;
    }

    /** Remove googtrans and any cookie whose name starts with goog (Translate sets several). */
    function clearGoogleTranslateCookies() {
        var host = window.location.hostname;
        var expire = "expires=Thu, 01 Jan 1970 00:00:01 GMT";
        var paths = ["/"];
        var domains = ["", host, "." + host];

        function kill(name, value) {
            paths.forEach(function (path) {
                domains.forEach(function (dom) {
                    var c = name + "=" + (value || "") + ";" + expire + ";path=" + path;
                    if (dom) {
                        c += ";domain=" + dom;
                    }
                    document.cookie = c;
                });
            });
        }

        kill(COOKIE, "");
        try {
            document.cookie.split(";").forEach(function (chunk) {
                var eq = chunk.indexOf("=");
                var name = (eq >= 0 ? chunk.slice(0, eq) : chunk).replace(/^\s+/, "");
                if (name.indexOf("goog") === 0) {
                    kill(name, "");
                }
            });
        } catch (e) {
            /* ignore */
        }
    }

    function clearTranslateStorage() {
        try {
            var i;
            var k;
            for (i = sessionStorage.length - 1; i >= 0; i--) {
                k = sessionStorage.key(i);
                if (k && (k.indexOf("goog") >= 0 || k.indexOf("translate") >= 0)) {
                    sessionStorage.removeItem(k);
                }
            }
            for (i = localStorage.length - 1; i >= 0; i--) {
                k = localStorage.key(i);
                if (k && (k.indexOf("goog") >= 0 || k.indexOf("translate") >= 0)) {
                    localStorage.removeItem(k);
                }
            }
        } catch (e) {
            /* ignore */
        }
    }

    /**
     * If Odoo serves Arabic under /ar/... or /ar_SY/..., return URL without the lang prefix so English loads.
     */
    function urlForEnglishSamePage() {
        var path = window.location.pathname;
        var search = window.location.search || "";
        if (!/^\/ar(?:_[A-Za-z0-9]+)?(?=\/|$)/.test(path)) {
            return null;
        }
        var rest = path.replace(/^\/ar(?:_[A-Za-z0-9]+)?/, "");
        if (rest === "") {
            rest = "/";
        }
        return window.location.origin + rest + search;
    }

    function goToEnglish() {
        clearGoogleTranslateCookies();
        clearTranslateStorage();
        var stripped = urlForEnglishSamePage();
        if (stripped) {
            window.location.replace(stripped);
            return;
        }
        var href = window.location.pathname + window.location.search;
        window.location.replace(href);
    }

    function setTargetLang(lang) {
        if (lang === "ar") {
            document.cookie = COOKIE + "=/en/ar;path=/;max-age=31536000;SameSite=Lax";
            window.location.reload();
            return;
        }
        goToEnglish();
    }

    function setOpen(root, menu, trigger, open) {
        root.classList.toggle("soor-gtranslate--open", open);
        trigger.setAttribute("aria-expanded", open ? "true" : "false");
        if (open) {
            menu.removeAttribute("hidden");
        } else {
            menu.setAttribute("hidden", "hidden");
        }
    }

    function syncActiveState(root) {
        var active = getActiveTargetLang();
        root.classList.remove("soor-gtranslate--active-en", "soor-gtranslate--active-ar");
        root.classList.add(active === "ar" ? "soor-gtranslate--active-ar" : "soor-gtranslate--active-en");

        root.querySelectorAll("[data-soor-lang]").forEach(function (el) {
            var l = el.getAttribute("data-soor-lang");
            el.classList.toggle("soor-gtranslate__opt--active", l === active);
        });
    }

    window.googleTranslateElementInit = function googleTranslateElementInit() {
        var g = window.google;
        if (window._soorGtInited || !g || !g.translate) {
            return;
        }
        window._soorGtInited = true;
        new g.translate.TranslateElement(
            {
                pageLanguage: SOURCE_LANG,
                includedLanguages: "ar,en",
                layout: g.translate.TranslateElement.InlineLayout.SIMPLE,
                autoDisplay: false,
            },
            "soor_google_translate_element"
        );
    };

    function loadScript() {
        if (document.querySelector('script[src*="translate.google.com"]')) {
            return;
        }
        var s = document.createElement("script");
        s.src = "https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
        s.async = true;
        document.head.appendChild(s);
    }

    function init() {
        var root = document.getElementById("soor-gtranslate-root");
        var menu = document.getElementById("soor-gtranslate-menu");
        var trigger = document.getElementById("soor-gtranslate-trigger");
        if (!root || !menu || !trigger) {
            return;
        }

        syncActiveState(root);
        loadScript();

        trigger.addEventListener("click", function (ev) {
            ev.stopPropagation();
            var open = !root.classList.contains("soor-gtranslate--open");
            setOpen(root, menu, trigger, open);
        });

        root.querySelectorAll("[data-soor-lang]").forEach(function (btn) {
            btn.addEventListener("click", function (ev) {
                ev.preventDefault();
                ev.stopPropagation();
                var lang = btn.getAttribute("data-soor-lang");
                setOpen(root, menu, trigger, false);
                if (!lang || lang === getActiveTargetLang()) {
                    return;
                }
                setTargetLang(lang);
            });
        });

        document.addEventListener("click", function () {
            setOpen(root, menu, trigger, false);
        });

        document.addEventListener("keydown", function (ev) {
            if (ev.key === "Escape") {
                setOpen(root, menu, trigger, false);
            }
        });

        root.addEventListener("click", function (ev) {
            ev.stopPropagation();
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
