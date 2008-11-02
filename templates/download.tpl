<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Download</py:def>
<py:def function="page_rss">${rss_files}</py:def>

<div py:match="content" id="body">
    <py:for each="release in releases">
    <h2>${release.fullname}</h2>
        <p>Released ${release.date}, see <a href="${release.notes}">release notes</a> for details.</p>
        <ul class="dl">
            <py:for each="file in release.files">
            <li><a href="${file.url}">${file.name}</a> (${file.size} bytes, ${file.dlcount} downloads)</li>
            </py:for>
        </ul> 
    </py:for>
</div>

<xi:include href="_page.tpl" />
</html>
