<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Security - ${issue}</py:def>

<div py:match="content" py:strip="">

<xi:include href="_list.tpl" />

<div id="body">
    <h2>${issue}</h2>
    ${Markup(content)}
</div>
<div class="clearer"></div>
</div>

<xi:include href="../_page.tpl" />
</html>
