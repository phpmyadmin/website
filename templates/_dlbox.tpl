<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Download box content -->

<span class="dlname">Download <a href="${release.notes}">${release.version}</a>:</span>
<ul class="dllist">
<py:for each="file in release.files"><py:if test="file.featured">
    <li><a href="${file.url}">${file.ext}</a></li>
</py:if></py:for>
</ul> 

</html>
