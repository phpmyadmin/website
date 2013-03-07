<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Little boxes with downloads and other quick links -->

<div class="rightbutton downloadbutton" py:for="release in releases_featured">
    <xi:include href="_dlbox.tpl" />
</div>

<div class="rightbutton downloadbutton" py:for="release in releases_beta">
    <xi:include href="_dlbox.tpl" />
</div>

<div class="rightbutton">
    <span class="dlname"><a href="${base_url}contest.${file_ext}" >Contest: win books!</a></span>
</div>

<div class="rightbutton">
    <span class="dlname"><a href="http://demo.phpmyadmin.net/trunk-config/" title="Go to demo server">Try phpMyAdmin</a></span>
</div>

<div class="rightbutton">
    <span class="dlname"><a href="${base_url}donate.${file_ext}" rel="payment">Donate to phpMyAdmin</a></span>
</div>

</html>
