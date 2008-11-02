<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">News</py:def>
<py:def function="page_rss">${rss_news}</py:def>

<div py:match="content" id="body">
    <py:for each="item in news">
        <h2>${item.title} (${item.date})</h2>
        <p>${Markup(item.text)}</p>
    </py:for>
</div>

<xi:include href="_page.tpl" />
</html>
