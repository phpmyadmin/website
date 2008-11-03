<!--!  Sample page for creating new ones -->
<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<!--! Define this function to set page title -->
<py:def function="page_title">Page title</py:def>
<!--! Define this to URL for RSS feed for this page -->
<py:def function="page_rss">${rss_news}</py:def>

<!--! This way we inject content into template body -->
<div py:match="content" id="body">

    <!--! We can include another templates -->
    <xi:include href="_littleboxes.tpl" />

    <p>Content...</p>

</div>

<!--! At the end we include main page template -->
<xi:include href="_page.tpl" />

</html>
