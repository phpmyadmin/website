<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Download box content -->

<span class="dlname">Download ${release.version}:</span>
<ul class="dllist">
<py:for each="file in release.files"><py:if test="file.featured">
    <li><a href="${file.url}#!md5!${file.md5}" title="Download ${file.ext} compressed release, ${file.humansize}" rel="quick-download" class="piwik_download">${file.ext}</a></li>
</py:if></py:for>
    <li><a href="${release.notes}" title="Release notes">notes</a></li>
    <li><a href="${base_url}downloads.${file_ext}" title="More download options">&hellip;</a></li>
</ul> 

</html>
