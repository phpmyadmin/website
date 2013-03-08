
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

/* Auto load blocks */

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

function fader_autoload() {
    if ($("fader") == null) return;

    var f = new Fader('fader');
}

window.addEvent('domready', fader_autoload);

/*
function dl_hint() {
    if ($$("div.downloadbutton").length == 0) return;
    var myTips = new Tips('div.downloadbutton');
    $$("div.downloadbutton").store('tip:text', 'There are more download options available on the downloads page.');
}

window.addEvent("domready", dl_hint);
*/

var dl_match = /https?:\/\/prdownloads\.sourceforge\.net\/phpmyadmin\/(.*)\?download.*/;
var notes_match = /https?:\/\/sourceforge\.net\/project\/shownotes.php\?release_id=([0-9]*)/

/**
 * Returns tracking string for the URL.
 */
function get_track_string(href, rel) {
    if (href.search(dl_match) != -1) {
        if (rel == 'quick-download') {
            pageTracker._trackPageview('/external/sf/quick-download/' + href.replace(dl_match, '$1'));
        }
        return '/external/sf/download/' + href.replace(dl_match, '$1');
    }
    if (href.search(notes_match) != -1) {
        return '/external/sf/release-notes/' + href.replace(notes_match, '$1');
    }
    if (href.indexOf('/sourceforge.net/project/showfiles.php?group_id=23067') != -1) {
        return '/external/sf/downloads';
    }
    if (href.indexOf('/sourceforge.net/services/project_services.php?project_id=23067&showListings=true') != -1) {
        return '/external/sf/services';
    }
    if (href.indexOf('/sourceforge.net/donate/index.php?group_id=23067') != -1) {
        return '/external/sf/donate';
    }
    if (href.indexOf('/sourceforge.net/news/?group_id=23067') != -1) {
        return '/external/sf/news';
    }
    if (href.indexOf('/sourceforge.net/tracker/?atid=377408&group_id=23067') != -1) {
        return '/external/sf/tracker/bugs';
    }
    if (href.indexOf('/sourceforge.net/tracker/?atid=377411&group_id=23067') != -1) {
        return '/external/sf/tracker/features';
    }
    if (href.indexOf('/sourceforge.net/tracker/?atid=377410&group_id=23067') != -1) {
        return '/external/sf/tracker/patches';
    }
    if (href.indexOf('/sourceforge.net/tracker/?atid=689412&group_id=23067') != -1) {
        return '/external/sf/tracker/themes';
    }
    if (href.indexOf('/sourceforge.net/tracker/?atid=377409&group_id=23067') != -1) {
        return '/external/sf/tracker/support';
    }
    if (href.indexOf('/sourceforge.net/tracker/?atid=387645&group_id=23067') != -1) {
        return '/external/sf/tracker/translations';
    }
    if (href.indexOf('/sourceforge.net/forum/forum.php?forum_id=72909') != -1) {
        return '/external/sf/forum/english';
    }
    if (href.indexOf('/sourceforge.net/forum/forum.php?forum_id=296543') != -1) {
        return '/external/sf/forum/french';
    }
    if (href.indexOf('/sourceforge.net/forum/forum.php?forum_id=297172') != -1) {
        return '/external/sf/forum/german';
    }
    if (href.indexOf('http://pma.cihar.com/') != -1) {
        return '/external/demo/' + href.substr(21);
    }
    if (href.indexOf('http://cve.mitre.org/cgi-bin/cvename.cgi?name=') != -1) {
        return '/external/cve/' + href.substr(46);
    }
    return '/external/' + href.replace('http://','').replace('https://','');
}

/**
 * Callback when user clicks on external link.
 */
function onclick_callback(e) {
    var href = this.get('href');
    var rel = this.get('rel');
    var track = get_track_string(href, rel);
    pageTracker._trackPageview(track);
}

/**
 * Iinitalizes tracking for external links.
 */
window.addEvent('domready',function(){
    $$('a').each(function(anchor){
        var href = anchor.get('href');
        // if it matches my site or is an absolute path it's outgoing
        if(href
            && href.indexOf('http://www.phpmyadmin.net') == -1
            && href.indexOf('http://phpmyadmin.net') == -1
            && (href.indexOf('http://') != -1 || href.indexOf('https://') != -1)) {
                anchor.addEvent('click', onclick_callback);
        }
    });
});
