<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
        <p>Released ${release.date}, see <a href="${release.notes}">release notes</a> for details.</p>
        <ul class="dl">
            <py:for each="file in release.files">
            <li><a href="${file.url}#!md5!${file.md5}">${file.name}</a><div class="filedetails">${file.size} bytes, ${file.dlcount} downloads, ${file.md5}</div></li>
            </py:for>
        </ul> 
</html>
