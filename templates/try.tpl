<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Try</py:def>

<div py:match="content" id="body">

<h2>Demo Server</h2>

<p>
The best way to see phpMyAdmin in action is to try it on our demo server, where you have
full control on MySQL. The default login is root with empty password.
</p>

<ul>
    <li><a href="http://demo.phpmyadmin.net/">Demos overview</a></li>
    <li><a href="http://demo.phpmyadmin.net/trunk">Latest development version</a></li>
    <li><a href="http://demo.phpmyadmin.net/STABLE">Latest released stable version</a></li>
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
