<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Themes</py:def>
<py:def function="page_rss">${rss_files}</py:def>

<div py:match="content" id="body">
    <div class="theme" py:for="theme in themes">
        <h2>${theme.fullname}</h2>
            <p>Released ${theme.date}, see <a href="${theme.notes}">release notes</a> for details.</p>
            <ul class="dl">
                <li><a href="${theme.file.url}">${theme.file.name}</a> (${theme.file.size} bytes, ${theme.file.dlcount} downloads)</li>
            </ul> 
            <div class="themeimgborder">
            <div class="themeimg">
                <a href="${base_url}images/themes/${theme.name}.png"
                rel="lightbox[themes]" title="${theme.name}">
                    <img src="${base_url}images/themes/${theme.name}.png" alt="${theme.name} thumbnail" />
                </a>
            </div>
            </div>
    </div>
    <div class="clearer"></div>
</div>

<xi:include href="_page.tpl" />
</html>
