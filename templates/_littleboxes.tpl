<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Little boxes with downloads and other quick links -->

<div class="downloadbutton" py:for="release in releases_featured">
    <xi:include href="_dlbox.tpl" />
</div>

<div class="downloadbutton" py:for="release in releases_beta">
    <xi:include href="_dlbox.tpl" />
</div>

<div>
    <a href="http://demo.phpmyadmin.net/master-config/" title="Go to demo server">Try demo</a>
</div>

<div>
    <a href="${base_url}donate.${file_ext}" rel="payment">Donate</a>
</div>

<div>
    <a href="http://wiki.phpmyadmin.net/pma/GSoC_2013_Projects" title="Google Summer of Code 2013 projects">GSoC 2013</a>
</div>

</html>
