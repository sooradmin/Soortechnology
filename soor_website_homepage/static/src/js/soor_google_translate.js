/**
 * Google Website Translator: compact bottom-left trigger + flyout (AR/EN).
 * Cookie googtrans + reload. Dropdown closes on outside click / Escape.
 */
(function () {
    "use strict";

    const COOKIE = "googtrans";
    const SOURCE_LANG = "en";

    function getCookie(name) {
        const m = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([.$?*|{}()[\]\\/+^])/g, "\\$1") + "=([^;]*)"));
        return m ? decodeURIComponent(m[1]) : "";
    }

    function getActiveTargetLang() {
        const v = getCookie(COOKIE);
        if (!v || v === "/en/en") {
            return SOURCE_LANG;
        }
        const parts = v.split("/").filter(Boolean);
        const target = parts[parts.length - 1];
        return target === "ar" ? "ar" : SOURCE_LANG;
    }

    function clearGoogTransCookies() {
        const host = window.location.hostname;
        const expires = "expires=Thu, 01 Jan 1970 00:00:01 GMT";
        const pairs = [
            COOKIE + "=;" + expires + ";path=/",
            COOKIE + "=;" + expires + ";path=/;domain=" + host,
            COOKIE + "=;" + expires + ";path=/;domain=." + host,
        ];
        pairs.forEach(function (c) {
            document.cookie = c;
        });
    }

    function setTargetLang(lang) {
        if (lang === "ar") {
            document.cookie = COOKIE + "=/en/ar;path=/;max-age=31536000";
        } else {
            clearGoogTransCookies();
        }
        window.location.reload();
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
        const active = getActiveTargetLang();
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
