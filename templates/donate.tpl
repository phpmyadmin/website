<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Donations</py:def>
<py:def function="page_rss">${rss_donations}</py:def>

<div py:match="content" id="body">
<h2>Donations</h2>
<p>
We invite you to <a href="http://sourceforge.net/donate/index.php?group_id=23067" rel="payment">contribute money</a> to our project. Donations will be used for
the promotion of phpMyAdmin. Thanks.
</p>

<h2>Recent donors</h2>

    <ul py:for="item in donations">
        <li>${Markup(item.title)} (${item.date})
        <span class="note" py:if="item.text">
        ${Markup(item.text)}
        </span>
        </li>
    </ul>
</div>

<xi:include href="_page.tpl" />
</html>
