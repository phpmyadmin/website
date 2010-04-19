<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Download box content -->

<span class="dlname">Download <a href="${release.notes}" title="Release notes">${release.version}</a>:</span>
<ul class="dllist">
<py:for each="file in release.files"><py:if test="file.featured">
    <li><a href="${file.url}#!md5!${file.md5}" title="Download ${file.ext} compressed release, ${file.humansize}" rel="quick-download" class="piwik_download">${file.ext}</a></li>
</py:if></py:for>
</ul> 

</html>
