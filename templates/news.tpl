<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">News</py:def>
<py:def function="page_rss">${rss_news}</py:def>

<div py:match="content" id="body">

    <xi:include href="_littleboxes.tpl" />

    <py:for each="item in news">
        <h2><a name="${item.anchor}"></a>${item.title}</h2>
        <p class="date">${item.date}</p>
        <p>${Markup(item.text)}</p>
        <p class="comments"><a href="${item.comments_link}">${item.comments_number} comments</a></p>
    </py:for>
</div>

<xi:include href="_page.tpl" />
</html>
