
/**
 * Shows only subset of divs with class "theme" which have class passed
 * as a parameter.
 */
function show_theme(version) {
    $$('.themelink').setStyle('background', 'none').setStyle('color', 'inherit');
    $$('.themelink.' + version).setStyle('background', '#666699').setStyle('color', 'white');
    if (version === "all") {
        $$("div.themediv").setStyle("display", "block");
        return;
    }
    $$("div.themediv." + version).setStyle("display", "block");
    $$("div.themediv:not(." + version + ")").setStyle("display", "none");
}

/* Auto load blocks */

function theme_load() {
    /* Is this document with themes? */
    if ($$("div.themediv").length === 0) {
        return;
    }

    var hash = null;

    /* Do we have some parameter? */
    if (self.document.location.hash.length > 1) {
        hash = self.document.location.hash.substring(1);
    } else {
        var links = $$('.themelink');
        hash = links[links.length - 1].get('href').substring(1);
    }

    /* Finally show chosen schema */
    show_theme(hash);
}

window.addEvent("domready", theme_load);

function fader_autoload() {
    if ($("fader") === null) {
        return;
    }

    new Fader('fader');
}

window.addEvent('domready', fader_autoload);
