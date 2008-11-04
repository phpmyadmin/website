<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Little boxes with downloads and other quick links -->

<div class="rightbuttons">
<div class="downloadbutton" py:for="release in releases">
    <span class="dlname">Download <a href="${release.notes}">${release.version}</a>:</span>
    <ul class="dllist">
    <py:for each="file in release.files"><py:if test="file.featured">
        <li><a href="${file.url}">${file.ext}</a></li>
    </py:if></py:for>
    </ul> 
</div>

<div class="downloadbutton">
    <span class="dlname"><a href="${base_url}try.${file_ext}">Try phpMyAdmin now</a></span>
</div>

<div class="downloadbutton">
    <span class="dlname"><a href="${base_url}donate.${file_ext}">Donate to phpMyAdmin</a></span>
</div>
</div>

</html>
