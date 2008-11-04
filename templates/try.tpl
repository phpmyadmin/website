<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Try</py:def>

<div py:match="content" id="body">

<h2>Try</h2>

<p>
Best way to see phpMyAdmin in action is to try it on our demo server. You have
there full control on MySQL, default login is root with empty password.
</p>

<ul>
    <li><a href="http://pma.cihar.com/">Demos overview</a></li>
    <li><a href="http://pma.cihar.com/trunk">Latest development version</a></li>
    <li><a href="http://pma.cihar.com/TESTING">Latest released testing version</a></li>
    <li><a href="http://pma.cihar.com/STABLE">Latest released stable version</a></li>
</ul>


<h2>Screenshots</h2>

<div class="screenshot" py:for="screen in screenshots">
    <a href="${base_url}images/screenshots/${screen.name}.png"
    rel="lightbox[screenshots]" title="${screen.title}">
        <img src="${base_url}images/screenshots/${screen.name}-small.png"
        alt="${screen.title}" /><br />
    ${screen.title}
    </a>
</div>

<div class="clearer"></div>
</div>

<xi:include href="_page.tpl" />
</html>
