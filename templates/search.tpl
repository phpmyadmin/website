<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_rss">${rss_summary}</py:def>
<py:def function="page_rss_title">phpMyAdmin project summary</py:def>

<py:def function="page_title">About</py:def>

<div py:match="content" id="body">

<h2>Search</h2>

<p>
This page uses Google Custom Search to give you best results related to
phpMyAdmin. You can also use it <a
href="http://www.google.com/coop/cse?cx=008688692096734274889:2un4bs4yxjm">directly
on Google</a>.
</p>

<!-- Non javascript version to use directly Goole (and leave phpmyadmin.net) -->
<noscript>
<style type="text/css">
@import url(http://www.google.com/cse/api/branding.css);
</style>
<div class="cse-branding-bottom" style="background-color:#FFFFFF;color:#000000">
  <div class="cse-branding-form">
    <form action="http://www.google.com/cse" id="cse-search-box">
      <div>
        <input type="hidden" name="cx" value="008688692096734274889:2un4bs4yxjm" />
        <input type="hidden" name="ie" value="UTF-8" />
        <input type="text" name="q" size="31" />
        <input type="submit" name="sa" value="Search" />
      </div>
    </form>
  </div>
  <div class="cse-branding-logo">
    <img src="http://www.google.com/images/poweredby_transparent/poweredby_FFFFFF.gif" alt="Google" />
  </div>
  <div class="cse-branding-text">
    Custom Search
  </div>
</div>
</noscript>


<!-- AJAX version of search to display results inside our pages -->
<script src="http://www.google.com/jsapi" type="text/javascript"></script>
<script language="Javascript" type="text/javascript">//<![CDATA[
  document.write('<div id="search_control">Loading...</div>');
  google.load('search', '1.0');

  function OnLoad() {

    // create a search control
    var searchControl = new google.search.SearchControl();

    // web search, open, custom search
    options = new google.search.SearcherOptions();
    options.setExpandMode(google.search.SearchControl.EXPAND_MODE_OPEN);
    ws = new google.search.WebSearch();
    ws.setSiteRestriction("008688692096734274889:2un4bs4yxjm");
    searchControl.addSearcher(ws, options);
    ws.setResultSetSize(google.search.Search.LARGE_RESULTSET);

    // tell the searcher to draw itself and tell it where to attach
    searchControl.draw(document.getElementById("search_control"));
  }
  google.setOnLoadCallback(OnLoad, true);
//]]>
</script>
    
</div>

<xi:include href="_page.tpl" />
</html>
