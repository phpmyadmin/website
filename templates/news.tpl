<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">News</py:def>
<py:def function="page_rss">${rss_news}</py:def>
<py:def function="page_rss_title">phpMyAdmin project news</py:def>

<div py:match="content" id="body">

<p>Bored of official project news? Then check out developers blogs at 
<a href="http://planet.phpmyadmin.net/">planet phpMyAdmin</a>.</p>

<p>You can also follow us on <a
href="http://identi.ca/phpmyadmin">identi.ca</a> or <a
href="http://twitter.com/phpmya">twitter</a>.
</p>

<div class="hitbuttons">
    <xi:include href="_littleboxes.tpl" />
</div>

<div class="hentry" id="${item.anchor}" py:for="item in news">
        <h2 class="entry-title"><a rel="bookmark" href="${item.link}">${item.title}</a></h2>
        <p class="date"><abbr class="published" title="${item.date.w3cdtf()}">${item.date}</abbr></p>
        <p class="entry-content">${Markup(item.text)}</p>
</div>

    <p>
    Older news are available at <a href="https://sourceforge.net/news/?group_id=23067">news archive at SourceForge</a>.
    </p>
</div>

<xi:include href="_page.tpl" />
</html>
