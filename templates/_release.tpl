<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<p>Released ${release.date}, see <a href="${release.notes}">release notes</a> for details.</p>

<p>${release.info}</p>

<table class="dllist">
<thead>
    <tr>
        <th>File</th>
        <th>Size</th>
        <th>MD5 checksum</th>
        <th>Downloads</th>
    </tr>
</thead>
<tbody>
    <tr py:for="file in release.files">
        <td><a href="${file.url}#!md5!${file.md5}" class="piwik_download">${file.name}</a></td>
        <td class="size">${file.humansize}</td>
        <td>${file.md5}</td>
        <td class="count">${file.dlcount}</td>
    </tr>
</tbody>
</table> 

</html>
