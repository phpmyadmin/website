<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Themes</py:def>

<div py:match="content" id="body">
    <py:for each="theme in files.theme">
    <h2>${theme.name}</h2>
        <p>Released ${theme.date}, see <a href="${theme.notes}">release notes</a> for details.</p>
        <ul class="dl">
            <py:for each="file in theme.files">
            <li><a href="${file.url}">${file.name}</a> (${file.size} bytes, ${file.dlcount} downloads)</li>
            </py:for>
        </ul> 
    </py:for>
</div>

<xi:include href="_page.tpl" />
</html>
