<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Security</py:def>
<py:def function="page_rss">${rss_security}</py:def>
<py:def function="page_rss_title">phpMyAdmin security issues</py:def>

<div py:match="content">
<xi:include href="_list.tpl" />

<div id="body">
<h2>Security</h2>

<p>
We take seriously any security issues found in our code. On the left
side, you can see past security issues which were discovered and fixed.
For critical issues, we publish a security release (whose number contains
a fourth digit like 3.3.10.5).
</p>

<xi:include href="../_security_contact.tpl" />

<p>
Please note that any support requests on this address will not be answered;
you should use the standard support ways mentioned on the
<a href="${base_url}support.${file_ext}">support</a> page.
</p>

<p>
To follow latest security releases you can use a <a href="${rss_security}">RSS feed</a>.
</p>

</div>
<div class="clearer"></div>
</div>

<xi:include href="../_page.tpl" />
</html>
