<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Donations</py:def>

<div py:match="content" id="body">
<h2>Donations</h2>
<p>
As an free software project, phpMyAdmin has almost no revenues itself. On the
other side, we have some expenses. Currently most of project funds are used
for travel costs for team members to allow them attend various conferences.
</p>
<p>
We invite you to <a href="https://sourceforge.net/donate/index.php?group_id=23067" rel="payment">contribute money</a> 
to our project (or just send money using PayPal to donate@phpmyadmin.net).
PayPal is one of most used online payments methods, it also accepts all major
credit cards.
</p>
<p>
Alternatively you can appreciate our work using 
<a href="https://flattr.com/thing/56976/phpMyAdmin">Flattr</a>. Flattr is a
microdonation system allowing users to easily appreciate others.
</p>
<p>
Donations will be used for the promotion of phpMyAdmin, mostly by allowing team members to visit various conferences. Thanks.
</p>

<h2>Sponsors</h2>

<p>If you want to sponsor phpMyAdmin in a recurring way, please check our 
<a href="${base_url}sponsors.${file_ext}">sponsorship page</a>.</p>

<xi:include href="_page.tpl" />
</html>
