<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_rss">${rss_news}</py:def>
<py:def function="page_rss_title">phpMyAdmin project news</py:def>
<py:def function="page_title">Page not found</py:def>

<div py:match="content" id="body">

<xi:include href="_littleboxes.tpl" />

<h2>Page Not Found</h2>

<p>
The requested URL was not found on this server. This might have several
causes, but if you found this link on some page, you should notify it's author
that it no longer works. Please follow to our <a href="${base_url}">main
page</a> to find information you were looking for or use navigation bar above.
</p>

<script type="text/javascript">
<![CDATA[
var GOOG_FIXURL_LANG = 'en';
var GOOG_FIXURL_SITE = 'http://www.phpmyadmin.net/';
]]>
</script>
<script type="text/javascript" src="http://linkhelp.clients.google.com/tbproxy/lh/wm/fixurl.js"></script>

</div>

<xi:include href="_page.tpl" />
</html>
