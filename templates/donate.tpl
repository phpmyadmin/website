<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Donations</py:def>

<div py:match="content" id="body">
<h2>Donations</h2>
<p>
As an free software project, phpMyAdmin has almost no revenues itself. On the
other side, we have some expenses. Currently most of project funds are used
for travel costs for team members to allow them attend various conferences.
</p>

<div class="subscribe">
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick" />
<input type="hidden" name="hosted_button_id" value="UUZWPJLQ9D4E8" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!" />
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form>
</div>

<p>
We invite you to contribute moneyto our project using PayPal button above.
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
</div>

<xi:include href="_page.tpl" />
</html>
