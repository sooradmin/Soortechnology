/** SOOR: count-up stats when elements scroll into view (homepage + about KPIs). */
(function () {
    "use strict";

    function easeOutCubic(t) {
        return 1 - Math.pow(1 - t, 3);
    }

    function prefersReducedMotion() {
        return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    }

    function animateCounter(el, durationMs) {
        if (el.getAttribute("data-soor-count-done") === "1") {
            return;
        }
        var raw = el.getAttribute("data-soor-count");
        var suffix = el.getAttribute("data-soor-suffix") || "";
        var target = raw !== null ? parseFloat(String(raw)) : NaN;
        if (Number.isNaN(target)) {
            return;
        }
        el.setAttribute("data-soor-count-done", "1");

        var isInt = Math.floor(target) === target;

        function formatValue(current) {
            if (isInt) {
                return String(Math.round(current));
            }
            return (Math.round(current * 10) / 10).toFixed(1).replace(/\.0$/, "");
        }

        if (prefersReducedMotion()) {
            el.textContent = formatValue(target) + suffix;
            return;
        }

        var start = null;

        function step(ts) {
            if (start === null) {
                start = ts;
            }
            var elapsed = ts - start;
            var p = Math.min(1, elapsed / durationMs);
            var eased = easeOutCubic(p);
            var current = target * eased;
            el.textContent = formatValue(current) + suffix;
            if (p < 1) {
                window.requestAnimationFrame(step);
            } else {
                el.textContent = formatValue(target) + suffix;
            }
        }

        el.textContent = formatValue(0) + suffix;
        window.requestAnimationFrame(step);
    }

    function init() {
        var nodes = document.querySelectorAll(".soor-js-count");
        if (!nodes.length) {
            return;
        }

        if (!("IntersectionObserver" in window)) {
            nodes.forEach(function (el) {
                var t = el.getAttribute("data-soor-count");
                var s = el.getAttribute("data-soor-suffix") || "";
                if (t !== null && !Number.isNaN(parseFloat(String(t)))) {
                    el.textContent = t + s;
                }
            });
            return;
        }

        var observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (!entry.isIntersecting) {
                        return;
                    }
                    animateCounter(entry.target, 2000);
                    observer.unobserve(entry.target);
                });
            },
            { root: null, rootMargin: "0px 0px -10% 0px", threshold: 0.2 }
        );

        nodes.forEach(function (el) {
            observer.observe(el);
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
