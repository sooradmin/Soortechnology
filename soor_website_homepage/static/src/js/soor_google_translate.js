/**
 * Google Website Translator (AR/EN).
 * Loads translate.google.com only when the user chose Arabic in this browser (localStorage/sessionStorage)
 * AND googtrans=/en/ar. Stale googtrans cookies alone must not auto-translate on every visit.
 */
(function () {
    "use strict";

    var COOKIE = "googtrans";
    var SOURCE_LANG = "en";
    /** Set only when the user clicks Arabic; without this we ignore googtrans=/en/ar on load. */
    var LS_USER_OPTED_AR = "soor_gt_user_opted_ar";

    function isHttps() {
        return window.location.protocol === "https:";
    }

    function cookieSecureSuffix() {
        return isHttps() ? ";Secure" : "";
    }

    function getCookie(name) {
        var m = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([.$?*|{}()[\]\\/+^])/g, "\\$1") + "=([^;]*)"));
        return m ? decodeURIComponent(m[1]) : "";
    }

    /** True when cookie says “show this page translated to Arabic”. */
    function wantsArabicFromCookie() {
        var v = getCookie(COOKIE);
        if (!v || v === "/en/en" || v === "/auto/en") {
            return false;
        }
        var parts = v.split("/").filter(Boolean);
        if (parts.length < 2) {
            return false;
        }
        return parts[parts.length - 1] === "ar";
    }

    function userOptedGoogleArabic() {
        try {
            if (window.localStorage.getItem(LS_USER_OPTED_AR) === "1") {
                return true;
            }
        } catch (e) {
            /* ignore */
        }
        try {
            return window.sessionStorage.getItem(LS_USER_OPTED_AR) === "1";
        } catch (e2) {
            return false;
        }
    }

    function setUserOptedGoogleArabic(yes) {
        try {
            if (yes) {
                window.localStorage.setItem(LS_USER_OPTED_AR, "1");
            } else {
                window.localStorage.removeItem(LS_USER_OPTED_AR);
            }
        } catch (e) {
            /* ignore */
        }
        try {
            if (yes) {
                window.sessionStorage.setItem(LS_USER_OPTED_AR, "1");
            } else {
                window.sessionStorage.removeItem(LS_USER_OPTED_AR);
            }
        } catch (e2) {
            /* ignore */
        }
    }

    /**
     * Apply dir="rtl" or dir="ltr" to the <html> element.
     * Called immediately on script load (no FOUC) and again inside syncActiveState().
     */
    function applyDirection(lang) {
        try {
            var html = document.documentElement;
            if (lang === "ar") {
                html.setAttribute("dir", "rtl");
            } else {
                // Only reset if we actually set rtl before — avoids touching pages
                // that never loaded Arabic.
                if (html.getAttribute("dir") === "rtl") {
                    html.setAttribute("dir", "ltr");
                }
            }
        } catch (e) {
            /* ignore */
        }
    }

    /** Load Google script / apply machine translation only after explicit Arabic choice in this browser. */
    function shouldLoadGoogleArabicTranslate() {
        return wantsArabicFromCookie() && userOptedGoogleArabic();
    }

    /**
     * Old googtrans=/en/ar (1y max-age) survives for months; without opt-in it must not trigger Arabic on open.
     */
    function stripStaleArabicCookieWithoutOptIn() {
        if (!wantsArabicFromCookie()) {
            return;
        }
        if (userOptedGoogleArabic()) {
            return;
        }
        clearGoogleTranslateCookies();
        document.cookie =
            COOKIE +
            "=/en/en;path=/;max-age=31536000" +
            cookieSameSiteSuffix() +
            cookieSecureSuffix();
    }

    function getLangPrefixesFromRoot(root) {
        var el = root || document.getElementById("soor-gtranslate-root");
        if (!el) return [];
        var raw = el.getAttribute("data-soor-lang-url-codes") || "";
        return raw.split(",").map(function (s) { return s.trim(); }).filter(Boolean);
    }

    function stripOdooLangPrefix(pathname, prefixes) {
        if (!prefixes || !prefixes.length) return pathname;
        if (pathname === "/") return pathname;
        var parts = pathname.split("/").filter(Boolean);
        if (!parts.length) return pathname;
        if (prefixes.indexOf(parts[0]) === -1) return pathname;
        parts.shift();
        return parts.length ? "/" + parts.join("/") : "/";
    }

    /** Google marks translated pages on html (and sometimes body). */
    function isGoogleTranslatedPage() {
        try {
            var html = document.documentElement;
            var body = document.body;
            if (html.classList.contains("translated-rtl") || html.classList.contains("translated-ltr")) {
                return true;
            }
            if (body && (body.classList.contains("translated-rtl") || body.classList.contains("translated-ltr"))) {
                return true;
            }
        } catch (e) {
            /* ignore */
        }
        return false;
    }

    function isOdooNonDefaultLangPath(pathname, root) {
        var prefixes = getLangPrefixesFromRoot(root);
        return stripOdooLangPrefix(pathname, prefixes) !== pathname;
    }

    /** True if the UI should offer “switch to English” (cookie, Google DOM, or Odoo /ar/… URL). */
    function needsEnglishSwitch(root) {
        if (wantsArabicFromCookie()) return true;
        if (isGoogleTranslatedPage()) return true;
        return isOdooNonDefaultLangPath(window.location.pathname, root);
    }

    function getActiveTargetLang(root) {
        if (wantsArabicFromCookie() && userOptedGoogleArabic()) return "ar";
        var el = root || document.getElementById("soor-gtranslate-root");
        if (!el) return SOURCE_LANG;
        var defaultCode = el.getAttribute("data-soor-default-lang-url-code") || "";
        var urlLang = el.getAttribute("data-soor-url-lang") || "";
        if (urlLang && defaultCode && urlLang !== defaultCode && urlLang === "ar") {
            return "ar";
        }
        return SOURCE_LANG;
    }

    /** SameSite as used when setting googtrans for Arabic — deletion must match or some browsers keep the old cookie. */
    function cookieSameSiteSuffix() {
        return ";SameSite=Lax";
    }

    /** Expire a cookie; must mirror flags used when it was set (SameSite+Lax, Secure on HTTPS). */
    function killCookie(name, value) {
        var expire = "expires=Thu, 01 Jan 1970 00:00:01 GMT";
        var maxAge0 = "max-age=0";
        var host = window.location.hostname;
        var paths = ["/"];
        var domains = ["", host, "." + host];
        var secure = cookieSecureSuffix();
        var sameSite = cookieSameSiteSuffix();

        function one(c) {
            document.cookie = c + sameSite + secure;
        }

        paths.forEach(function (path) {
            domains.forEach(function (dom) {
                var base = name + "=" + (value || "") + ";path=" + path + ";" + expire + ";" + maxAge0;
                if (dom) {
                    one(base + ";domain=" + dom);
                } else {
                    one(base);
                }
            });
        });
    }

    function clearGoogleTranslateCookies() {
        killCookie(COOKIE, "");
        try {
            document.cookie.split(";").forEach(function (chunk) {
                var eq = chunk.indexOf("=");
                var name = (eq >= 0 ? chunk.slice(0, eq) : chunk).replace(/^\s+/, "");
                if (name.indexOf("goog") === 0) {
                    killCookie(name, "");
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

    function urlForEnglishSamePage(root) {
        var path = window.location.pathname;
        var search = window.location.search || "";
        var prefixes = getLangPrefixesFromRoot(root);
        var strippedOdoo = stripOdooLangPrefix(path, prefixes);
        if (strippedOdoo !== path) {
            return window.location.origin + strippedOdoo + search;
        }
        if (!/^\/ar(?:_[A-Za-z0-9]+)?(?=\/|$)/.test(path)) {
            return null;
        }
        var rest = path.replace(/^\/ar(?:_[A-Za-z0-9]+)?/, "");
        if (rest === "") {
            rest = "/";
        }
        return window.location.origin + rest + search;
    }

    /**
     * Force "original English" for Google Translate: overwrite googtrans with /en/en (not only delete).
     * Deleting alone often fails on HTTPS when attributes do not match; a stale /en/ar then reloads Arabic.
     */
    function goToEnglish() {
        setUserOptedGoogleArabic(false);
        clearTranslateStorage();
        clearGoogleTranslateCookies();
        document.cookie =
            COOKIE +
            "=/en/en;path=/;max-age=31536000" +
            cookieSameSiteSuffix() +
            cookieSecureSuffix();
        var root = document.getElementById("soor-gtranslate-root");
        var stripped = urlForEnglishSamePage(root);
        var pathAndSearch = stripped ? stripped.replace(/^https?:\/\/[^/]+/, "") : window.location.pathname + window.location.search;
        var target = window.location.origin + pathAndSearch;
        window.setTimeout(function () {
            window.location.replace(target);
        }, 0);
    }

    function setTargetLang(lang) {
        if (lang === "ar") {
            setUserOptedGoogleArabic(true);
            document.cookie =
                COOKIE +
                "=/en/ar;path=/;max-age=31536000" +
                cookieSameSiteSuffix() +
                cookieSecureSuffix();
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
        var active = getActiveTargetLang(root);
        root.classList.remove("soor-gtranslate--active-en", "soor-gtranslate--active-ar");
        root.classList.add(active === "ar" ? "soor-gtranslate--active-ar" : "soor-gtranslate--active-en");

        // Keep html[dir] in sync with active language
        applyDirection(active);

        root.querySelectorAll("[data-soor-lang]").forEach(function (el) {
            var l = el.getAttribute("data-soor-lang");
            el.classList.toggle("soor-gtranslate__opt--active", l === active);
        });
    }

    window.googleTranslateElementInit = function googleTranslateElementInit() {
        if (!shouldLoadGoogleArabicTranslate()) {
            return;
        }
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
        if (!shouldLoadGoogleArabicTranslate()) {
            return;
        }
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

        stripStaleArabicCookieWithoutOptIn();
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
                if (!lang) {
                    return;
                }
                if (lang === "en") {
                    if (!needsEnglishSwitch(root)) {
                        return;
                    }
                    goToEnglish();
                    return;
                }
                if (lang === "ar") {
                    if (shouldLoadGoogleArabicTranslate() && isGoogleTranslatedPage()) {
                        return;
                    }
                    setTargetLang("ar");
                }
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

    // ── Early direction: run immediately so the page renders with the
    // correct dir attribute — no flash of LTR layout when user is on Arabic.
    // Uses function hoisting (all helpers above are function declarations).
    (function earlyApplyDirection() {
        try {
            if (wantsArabicFromCookie() && userOptedGoogleArabic()) {
                applyDirection("ar");
            }
        } catch (e) {
            /* ignore */
        }
    }());

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
