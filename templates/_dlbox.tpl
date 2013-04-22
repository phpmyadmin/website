<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Download box content -->

<py:for each="file in release.files"><py:if test="file.featured">
    <a href="${file.url}#!md5!${file.md5}" title="Download ${file.ext} compressed release, ${file.humansize}" rel="quick-download" class="piwik_download">Download ${release.version}</a>
</py:if></py:for>

</html>
