<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Little boxes with downloads and other quick links -->

<div class="rightbuttons">
<div class="rightbutton downloadbutton" py:for="release in releases_featured">
    <xi:include href="_dlbox.tpl" />
</div>

<div class="rightbutton downloadbutton" py:for="release in releases_beta">
    <xi:include href="_dlbox.tpl" />
</div>

<div class="rightbutton">
    <span class="dlname"><a href="http://demo.phpmyadmin.net/trunk-config/" title="Go to demo server">Try phpMyAdmin</a></span>
</div>

<div class="rightbutton">
    <span class="dlname"><a href="${base_url}donate.${file_ext}" rel="payment">Donate to phpMyAdmin</a></span>
</div>

</div>

<div class="rightsponsors">
<p><strong>Top <a href="${base_url}sponsors.${file_ext}">sponsors</a></strong></p>
<a href="http://www.aoemedia.de"><img src="${server}${base_url}images/aoemedia_200x68.jpg" alt="AOE media GmbH" /></a>
<a href="http://www.navicat.com"><img src="${server}${base_url}images/navicat_200x68.jpg" alt="Navicat" /></a>
</div>

</html>
