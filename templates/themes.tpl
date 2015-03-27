<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Themes</py:def>
<py:def function="page_rss">${rss_files}</py:def>
<py:def function="page_rss_title">phpMyAdmin file releases</py:def>

<div py:match="content" id="body">
<h2>Themes</h2>
<p>
phpMyAdmin supports themes since version 2.6.0. All themes are not compatible
with all phpMyAdmin versions; you should select below which version you are
using.
</p>
<p>
Please note that themes contain PHP code and you should download them only
from trusted servers. All themes available on this page have been checked by
phpMyAdmin team members.
</p>
<p>
To install a theme, unzip your downloaded theme into the directory /themes/ of
your phpMyAdmin folder. When you open phpMyAdmin, you should be able to select the theme.
Please read the documentation for more details.
</p>
<p>
You can try the themes in action on our <a
href="${base_url}try.${file_ext}">demo server</a>.
</p>

<h2>Submit Theme</h2>
<p>
You've made a new theme and you want to share it?  Please send your pull 
request to <a href="https://github.com/phpmyadmin/themes/pulls">https://github.com/phpmyadmin/themes/pulls</a>. The team will check and prepare your theme for downloading here.
</p>

<h2>Available Themes</h2>
<p>Select your phpMyAdmin version (requires JavaScript):
<a py:for="css in themecssversions" class="themelink" href="#${css.css}" onclick="show_theme('${css.css}')">${css.name}</a>
</p>
    <div py:for="theme in themes" class="theme ${theme.classes}">
        <h3>${theme.fullname}</h3>
            <div class="themeimgborder">
            <div class="themeimg">
                <a href="${base_url}${theme.imgname}"
                rel="lightbox[themes]" title="${theme.name}">
                    <img src="${base_url}${theme.imgname}" alt="${theme.name} thumbnail" />
                </a>
            </div>
            </div>
            <p>Released on ${theme.date}</p>
            <p>Compatible with phpMyAdmin <strong>${theme.support}</strong>.</p>
            <p py:if="theme.author">Author: ${theme.author}</p>
            <p>${Markup(theme.info)}</p>
            <ul class="dl">
                <li><a href="${theme.file.url}#!md5!${theme.file.md5}">${theme.file.name}</a> (${theme.file.humansize}, MD5: ${theme.file.md5})</li>
            </ul> 
    </div>
    <div class="clearer"></div>
</div>

<xi:include href="_page.tpl" />
</html>
