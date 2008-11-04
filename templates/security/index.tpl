<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Security</py:def>
<py:def function="page_rss">${base_url}security/index.xml</py:def>

<div py:match="content">
<xi:include href="_list.tpl" />

<div id="body">
<h2>Security</h2>

<p>
We seriously take care about any security issues found in our code. On left
side, you can see past security issues which were discovered and fixed.
</p>

<xi:include href="../_security_contact.tpl" />

<p>
Please note that any support requests on this address will not be answered,
you should use standard support ways mentioned on 
<a href="${base_url}support.${file_ext}">support</a> page.
</p>

</div>
<div class="clearer"></div>
</div>

<xi:include href="../_page.tpl" />
</html>
