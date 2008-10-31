<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Download</py:def>

<div py:match="content" id="body">
    <py:for each="pma in files.phpMyAdmin">
    <h2>${pma.name}</h2>
        <p>Released ${pma.date}, see <a href="${pma.notes}">release notes</a> for details.</p>
        <ul class="dl">
            <py:for each="file in pma.files">
            <li><a href="${file.url}">${file.name}</a> (${file.size} bytes, ${file.dlcount} downloads)</li>
            </py:for>
        </ul> 
    </py:for>
</div>

<xi:include href="_page.tpl" />
</html>
