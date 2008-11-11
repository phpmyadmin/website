<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Little boxes with downloads and other quick links -->

<div class="rightbuttons">
<div class="downloadbutton" py:for="release in releases_featured">
    <xi:include href="_dlbox.tpl" />
</div>

<div class="downloadbutton" py:for="release in releases_beta">
    <xi:include href="_dlbox.tpl" />
</div>

<div class="downloadbutton">
    <span class="dlname"><a href="${base_url}try.${file_ext}">Try phpMyAdmin</a></span>
</div>

<div class="downloadbutton">
    <span class="dlname"><a href="${base_url}donate.${file_ext}">Donate to phpMyAdmin</a></span>
</div>
</div>

</html>
