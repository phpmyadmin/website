<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Download box content -->

<span class="dlname"><a href="${release.notes}" title="Release notes">Download ${release.version}</a>:</span>
<ul class="dllist">
<py:for each="file in release.files"><py:if test="file.featured">
    <li><a href="${file.url}" title="Download ${file.ext} compressed release">${file.ext}</a></li>
</py:if></py:for>
</ul> 

</html>
