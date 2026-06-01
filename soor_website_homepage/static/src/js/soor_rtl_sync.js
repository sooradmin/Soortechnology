(function () {
    "use strict";

    function syncRtl() {
        var ww = document.getElementById("wrapwrap");
        if (!ww) return;
        var isRtl = ww.classList.contains("o_rtl") || ww.getAttribute("dir") === "rtl";
        document.documentElement.setAttribute("dir", isRtl ? "rtl" : "ltr");
    }

    // Run once the DOM is ready
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", syncRtl);
    } else {
        syncRtl();
    }

    // Watch #wrapwrap for class/dir changes (e.g. dynamic language switch)
    var observer = new MutationObserver(syncRtl);
    function attachObserver() {
        var ww = document.getElementById("wrapwrap");
        if (ww) {
            observer.observe(ww, { attributes: true, attributeFilter: ["class", "dir"] });
        }
    }
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", attachObserver);
    } else {
        attachObserver();
    }
})();
