<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Documentation</py:def>

<div py:match="content" id="body">

<h2>Documentation</h2>

<div class="floatbox">
<h3>Official Documentation</h3>
<ul>
    <li><b><a href="http://docs.phpmyadmin.net/">Main documentation</a></b> (from the development version)</li>
    <li><b><a href="https://readthedocs.org/projects/phpmyadmin/downloads/">Downloadable documentation</a></b> (from the development version)</li>
    <li><b><a href="http://wiki.phpmyadmin.net/">Official phpMyAdmin wiki</a></b></li>
    <li><a href="https://phpmyadmin.readthedocs.org/en/latest/faq.html">Frequently Asked Questions</a></li>
    <li><a href="http://www.phpmyadmin.net/documentation/changelog.php">ChangeLog</a></li>
    <li><a href="${base_url}translations.${file_ext}">Translations overview</a></li>
</ul>
</div>

<div class="floatbox">
<h3>Localized Documentation</h3>

<p>Please note that these translations are not always complete, but you can <a
href="${base_url}improve.${file_ext}#translate">help</a>.</p>

<ul>
    <li><a href="https://phpmyadmin-english-united-kingdom.readthedocs.org/en/latest/">English (United Kingdom)</a></li>
    <li><a href="https://phpmyadmin-spanish.readthedocs.org/en/latest/">Spanish</a></li>
    <li><a href="https://phpmyadmin-french.readthedocs.org/en/latest/">French</a></li>
    <li><a href="https://phpmyadmin-greek.readthedocs.org/en/latest/">Greek</a></li>
    <li><a href="https://phpmyadmin-czech.readthedocs.org/en/latest/">Czech</a></li>
    <li><a href="https://phpmyadmin-japanese.readthedocs.org/en/latest/">Japanese</a></li>
    <li><a href="https://phpmyadmin-turkish.readthedocs.org/en/latest/">Turkish</a></li>
    <li><a href="https://phpmyadmin-chinese-china.readthedocs.org/en/latest/">Simplified Chinese</a></li>
</ul>
</div>

<div class="floatbox">
<h3>Third Party Tutorials and Articles</h3>
<ul>
    <li><a href="https://cloud.google.com/sql/docs/phpmyadmin-on-app-engine">Using phpMyAdmin with Google Cloud SQL on Google App Engine</a></li>
    <li><a href="http://www.garvinhicking.de/tops/texte/mimetutorial">Having fun with phpMyAdmin's MIME-transformations &amp; PDF-features</a></li>
    <li><a href="http://www.linuxsoft.cz/article_list.php?id_kategory=215">Seriál o phpMyAdminovi (Česky)</a></li>
    <li><a href="http://www.devshed.com/c/a/PHP/Doing-More-With-phpMyAdmin-Part-1/">Doing More With phpMyAdmin: part 1</a>,
        <a href="http://www.devshed.com/c/a/PHP/Doing-More-with-phpMyAdmin-Part-2/">part 2</a></li>
    <li><a href="http://www.php-editors.com/articles/sql_phpmyadmin.php">Learning SQL Using phpMyAdmin</a></li>
</ul>
</div>

<div class="floatbox">
<h3>Sites Dedicated to phpMyAdmin</h3>
<ul>
    <li><a href="http://php-myadmin.ru">php-myadmin.ru: Russian site dedicated to phpMyAdmin</a>
    <ul>
    <li py:for="item in short_news_ru">
        <a href="${item.link}" lang="ru" xml:lang="ru">${item.title}</a>
    </li>
    </ul>
    </li>
    <li><a href="http://science.webhostinggeeks.com/phpmyadmin">Serbo-Croatian page about phpMyAdmin</a></li>
</ul>
</div>

<div class="clearer"></div>

<h2><a id="books"></a>Books</h2>

<div class="floatbox book">

<h3>Mastering phpMyAdmin 3.4 for Effective MySQL Management</h3>

<a href="http://link.packtpub.com/XJdqZr"><img src="${base_url}images/books/pma_en_3.4_150x185.png" alt="Book cover" width="150" height="185" style="border: 0px;" /></a>

<p>
A percentage of the book's sales is <a href="http://www.packtpub.com/article/open_source_receives_royalties_boost">donated</a> to help phpMyAdmin.
</p>

</div>

<div class="floatbox book">

<h3>phpMyAdmin Starter</h3>

<a href="http://www.amazon.com/phpMyAdminStarter-ebook/dp/B007RMWJSA/ref=sr_1_1?ie=UTF8&amp;qid=1333715561&amp;sr=8-1"><img src="${base_url}images/books/pma_starter_150x184.jpg" alt="Book cover" width="150" height="184" style="border: 0px;" /></a>

<p>
A percentage of the book's sales is <a href="http://www.packtpub.com/article/open_source_receives_royalties_boost">donated</a> to help phpMyAdmin.
</p>

</div>

<div class="floatbox book">

<h3>Mastering phpMyAdmin 2.11 for Effective MySQL Management</h3>

<a href="http://www.packtpub.com/phpmyadmin-3rd-edition/book"><img src="${base_url}images/books/pma_en_100x123.png" alt="Book cover" width="100" height="123" /></a>

<p>
A percentage of the book's sales is <a href="http://www.packtpub.com/article/open_source_receives_royalties_boost">donated</a> to help phpMyAdmin.
</p>

</div>

<div class="floatbox book">
<h3>Dominar phpMyAdmin para una administraci&oacute;n efectiva de MySQL</h3>

<a href="http://www.packtpub.com/dominary-phpMyAdmin-es"><img src="${base_url}images/books/pma_es_100x123.png" alt="Book cover" width="100" height="123" /></a>

<p xml:lang="es">
Este libro es una gu&iacute;a completa que le ayuda a sacar partido del potencial de phpMyAdmin. Ya sea un programador experimentado, un administrador de sistemas, un dise&ntilde;ador Web o nuevo a las tecnolog&iacute;as de MySQL y phpMyAdmin, este libro le mostrar&aacute; como aumentar su productividad y control cuando trabaje con MySQL. Por ello se ha traducido, de modo que esta gu&iacute;a completa sea m&aacute;s accesible al lector espa&ntilde;ol.
</p>

</div>

<div class="clearer"></div>

</div>

<xi:include href="_page.tpl" />
</html>
