<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Download</py:def>
<py:def function="page_rss">${rss_files}</py:def>

<div py:match="content" id="body">
    <py:for each="release in releases">
    <h2>${release.fullname}</h2>
    <xi:include href="_release.tpl" />
    </py:for>
    <h2>Older releases</h2>
    <py:for each="release in releases_older">
    <h3>${release.fullname}</h3>
    <xi:include href="_release.tpl" />
    </py:for>
</div>

<xi:include href="_page.tpl" />
</html>
