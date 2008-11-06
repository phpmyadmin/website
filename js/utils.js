
/**
 * Shows only subset of divs with class "theme" which have class passed 
 * as a parameter.
 */
function show_theme(version) {
	var divs1 = $$("div").filter(function(el) {
		return el.hasClass("theme") && el.hasClass(version);
	});
	var divs2 = $$("div").filter(function(el) {
		return el.hasClass("theme") && !el.hasClass(version);
	});
    $$(divs1).setStyle("display", "block")
    $$(divs2).setStyle("display", "none")
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

window.addEvent("domready", theme_load);
