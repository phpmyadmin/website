
/**
 * Shows only subset of divs with class "theme" which have class passed 
 * as a parameter.
 */
function show_theme(version) {
    if (version == "all") {
        $$("div.theme").setStyle("display", "block");
        return;
    }
    $$("div.theme." + version).setStyle("display", "block");
    $$("div.theme:not(." + version + ")").setStyle("display", "none");
}

// AUTOLOAD CODE BLOCK
function theme_load() {
    /* Is this document with themes? */
    if ($$("div.theme").length == 0) return;

    /* Do we have some parameter? */
    if (self.document.location.hash.length < 1) return;

    /* Is the parameter existing class for theme? */
    var hash = self.document.location.hash.substring(1);
    if ($$("div.theme." + hash).length==0) return;

    /* Finally show chosen schema */
    show_theme(hash);
}

function dl_hint() {
    /* Is this document with themes? */
    if ($$("div.downloadbutton").length == 0) return;
    var myTips = new Tips('div.downloadbutton');
    $$("div.downloadbutton").store('tip:text', 'There are more download options available on the downloads page.');
}

window.addEvent("domready", theme_load);
window.addEvent("domready", dl_hint);
