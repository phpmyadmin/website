<!DOCTYPE HTML>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"
      xmlns:py="http://genshi.edgewall.org/"
      xmlns:xi="http://www.w3.org/2001/XInclude">
<!--! This is main page template used for all other pages. -->
 <head profile="http://purl.org/uF/2008/03/ http://purl.org/uF/hAtom/0.1/">
  <meta charset="utf-8" />
  <meta name="author" content="phpMyAdmin devel team" />
  <meta name="copyright" content="Copyright &copy; 2003 - ${current_year} phpMyAdmin devel team" />
  <link rel="copyright" href="${base_url}license.${file_ext}" />
  <title>phpMyAdmin<py:if test="defined('page_title')"> - ${page_title()}</py:if></title>
  <py:if test="defined('page_rss')"><link rel="alternate" type="application/rss+xml" href="${page_rss()}" title="${page_rss_title()}"/></py:if>
  <link rel="stylesheet" type="text/css" href="${base_url}css/style.css" />
  <link rel="stylesheet" type="text/css" href="${base_url}css/slimbox.css" media="screen" />
  <link rel="shortcut icon" href="${base_url}favicon.ico" type="image/x-icon" />
  <link rel="icon" href="${base_url}favicon.ico" type="image/x-icon" />
  <link rel="vcs-git" href="git://github.com/phpmyadmin/phpmyadmin.git" title="phpMyAdmin Git repository" />
  <link rel="vcs-browse" href="http://github.com/phpmyadmin/" title="phpMyAdmin Git repository browser" />
  <link href="https://plus.google.com/112870346549275765217/" rel="publisher" />
  <script src="${base_url}js/mootools.js" type="text/javascript"></script>
  <script src="${base_url}js/mootools-more.js" type="text/javascript"></script>
  <script src="${base_url}js/slimbox.js" type="text/javascript"></script>
  <script src="${base_url}js/fader.js" type="text/javascript"></script>
  <script src="${base_url}js/master_sorting_table.js" type="text/javascript"></script>
  <script src="${base_url}js/utils.js" type="text/javascript"></script>
  <meta http-equiv="X-Generated" content="${generated}" />
  <meta name="verify-v1" content="3AM2eNj0zQ1Ao/N2eGE02S45V3p5KQxAyMIxdUJhtEQ=" />
  <meta name="robots" content="index, follow" />
<script type="text/javascript">
/* <![CDATA[ */
    (function() {
        var s = document.createElement('script'), t = document.getElementsByTagName('script')[0];
        
        s.type = 'text/javascript';
        s.async = true;
        s.src = 'http://api.flattr.com/js/0.6/load.js?mode=auto';
        
        t.parentNode.insertBefore(s, t);
    })();
/* ]]> */
</script>
 </head>
 <body>
  <header>
    <xi:include href="_menu.tpl" />
    <h1><a href="${base_url}" rel="home"><span id="logo">phpMyAdmin</span></a> Bringing MySQL to the web</h1>
  </header>

  <content>
    Placeholder.

  </content>

  <ul id="footer">
    <li>Copyright &copy; 2003 - ${current_year} <span class="vcard"><a class="url org fn" href="${base_url}team.${file_ext}">phpMyAdmin devel team</a><a href="mailto:phpmyadmin-devel@lists.sourceforge.net" class="email"></a></span></li>
    <li><a href="${base_url}license.${file_ext}" rel="license">License</a></li>
    <li><a href="${base_url}donate.${file_ext}" rel="payment" title="Support phpMyAdmin by donating money!">Donate</a></li>
    <li><a href="${base_url}sitemap.${file_ext}" rel="contents">Sitemap</a></li>
    <li><a href="${base_url}search.${file_ext}" title="Search for phpMyAdmin related questions">Search</a></li>
    <li><a href="${base_url}about-website.${file_ext}" title="Information about website">About</a></li>
    <li class="last">Valid <a href="http://validator.w3.org/check/referer">HTML</a> and <a href="http://jigsaw.w3.org/css-validator/check/referer">CSS</a></li>
    <li class="logo"><a href="http://sourceforge.net/projects/phpmyadmin"><img src="http://sflogo.sourceforge.net/sflogo.php?group_id=23067&amp;type=10" width="80" height="15" alt="Get phpMyAdmin at SourceForge.net. Fast, secure and Free Open Source software downloads" /></a></li>
    <li class="logo"><a class="FlattrButton" style="display:none;" rev="flattr;button:compact;" href="http://www.phpmyadmin.net/"></a></li>
    <li class="logo"><a href="http://google.com/+phpmyadmin" style="text-decoration: none;"><img src="https://ssl.gstatic.com/images/icons/gplus-16.png" width="16" height="16" style="border: 0;" alt="Google+"/></a></li>
  </ul>
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-2718724-14']);
_gaq.push(['_trackPageview']);
(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
<!-- Piwik -->
<script type="text/javascript">
  var _paq = _paq || [];
  _paq.push(["trackPageView"]);
  _paq.push(["enableLinkTracking"]);

  (function() {
    var u=(("https:" == document.location.protocol) ? "https" : "http") + "://stats.cihar.com/";
    _paq.push(["setTrackerUrl", u+"piwik.php"]);
    _paq.push(["setSiteId", "2"]);
    var d=document, g=d.createElement("script"), s=d.getElementsByTagName("script")[0]; g.type="text/javascript";
    g.defer=true; g.async=true; g.src=u+"piwik.js"; s.parentNode.insertBefore(g,s);
  })();
</script>
<!-- End Piwik Code -->
<!-- Piwik Image Tracker -->
<noscript><img src="https://stats.cihar.com/piwik.php?idsite=2&amp;rec=1" style="border:0" alt="" /></noscript>
<!-- End Piwik -->
 </body>
</html>

