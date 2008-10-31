<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Security</py:def>

<div py:match="content" py:strip="">
<xi:include href="_list.tpl" />

<div id="body">

  We seriously take care about any security issues found in our code. <br />In left box you can check security issues we already dealt with. <br /><br />If you find any  security problem in our code, please contact the <a href="mailto:security@phpmyadmin.net">phpMyAdmin security team</a> (this is <strong>not a support list</strong>, use one of ways mentioned on <a href="../feedback.html">feedback</a> page to get support).
</div>
<div class="clearer"></div>
</div>

<xi:include href="../_page.tpl" />
</html>
