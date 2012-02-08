<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Documentation</py:def>

<div py:match="content" id="body">

<h2>Documentation</h2>

<div class="floatbox">
<h3>Official Documentation</h3>
<ul>
    <li><b><a href="http://www.phpmyadmin.net/documentation/">Main documentation</a></b> (from the development version)</li>
    <li><b><a href="http://wiki.phpmyadmin.net/">Official phpMyAdmin wiki</a></b></li>
    <li><a href="http://www.phpmyadmin.net/documentation/#faq">Frequently Asked Questions</a></li>
    <li><a href="http://www.phpmyadmin.net/documentation/changelog.php">ChangeLog</a></li>
    <li><a href="${base_url}translations.${file_ext}">Translations overview</a></li>
</ul>
</div>

<div class="floatbox">
<h3>Localized Documentation</h3>

<p>Please note that these translations are not always complete, but you can <a
href="${base_url}improve.${file_ext}#translate">help</a>.</p>

<ul>
    <li><a href="http://www.phpmyadmin.net/localized_docs/cs">Czech</a></li>
    <li><a href="http://www.phpmyadmin.net/localized_docs/en_GB">English (United Kingdom)</a></li>
    <li><a href="http://www.phpmyadmin.net/localized_docs/es">Spanish</a></li>
    <li><a href="http://www.phpmyadmin.net/localized_docs/fr">French</a></li>
    <li><a href="http://www.phpmyadmin.net/localized_docs/it">Italian</a></li>
    <li><a href="http://www.phpmyadmin.net/localized_docs/ja">Japanese</a></li>
    <li><a href="http://www.phpmyadmin.net/localized_docs/pl">Polish</a></li>
    <li><a href="http://www.phpmyadmin.net/localized_docs/pt_BR">Brazilian Portuguese</a></li>
    <li><a href="http://www.phpmyadmin.net/localized_docs/tr">Turkish</a></li>
    <li><a href="http://www.phpmyadmin.net/localized_docs/zh_CN">Simplified Chinese</a></li>
</ul>
</div>

<div class="floatbox">
<h3>Third Party Tutorials and Articles</h3>
<ul>
    <li><a href="http://dev.mysql.com/tech-resources/articles/mysql_intro.html">Getting Started with MySQL</a></li>
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
    <li><a href="http://phpmyadmin.cz">phpmyadmin.cz: Czech site dedicated to phpMyAdmin</a>
    <ul>
    <li py:for="item in short_news_cz">
        <a href="${item.link}" lang="cs" xml:lang="cs">${item.title}</a>
    </li>
    </ul>
    </li>
</ul>
</div>

<div class="clearer"></div>

<h2><a id="books"></a>Books</h2>

<div class="floatbox book">

<h3>Mastering phpMyAdmin 3.4 for Effective MySQL Management</h3>

<a href="http://www.packtpub.com/mastering-phpmyadmin-3-4-for-effective-mysql-management/book"><img src="${base_url}images/books/pma_en_3.4_125x151.png" alt="Book cover" width="125" height="151" style="border: 0px;" /></a>

<p>
I am pleased to announce an update of my book. It is now up to date with phpMyAdmin 3.4. A percentage of the book's sales is <a href="http://www.packtpub.com/article/open_source_receives_royalties_boost">donated</a> to help phpMyAdmin.
</p>

<p>For more information, please visit <a href="http://www.packtpub.com/mastering-phpmyadmin-3-4-for-effective-mysql-management/book">the book's site</a>.</p>
<p class="signature">Marc Delisle</p>
</div>

<div class="floatbox book">

<h3>phpMyAdmin Starter</h3>

<a href="#" title="In the eBook..." onclick="window.open('https://www.packtpub.com/sites/default/files/pmastarter/pmastarterpreview.html','help','scrollbars=yes,resizable=yes,width=680,height=720,left=180,top=20'); return false;">
    <img width="135" height="170" style="border: 0px;" src="${base_url}images/packt/pmastarter_cover.png" alt="cover image"/>
</a>
<p>
Get started with this quick introduction to phpMyAdmin, its features, and the community. A percentage of each sale goes direct to the phpMyAdmin project.
</p>

<a href="https://www.e-junkie.com/ecom/gb.php?c=cart&amp;i=984362&amp;cl=174893&amp;ejc=2" target="ej_ejc" class="ec_ejc_thkbx" onclick="javascript:return EJEJC_lc(this);">
	<img src="${base_url}images/packt/addtocart.gif" style="border: 0px;" alt="Add to Cart"/></a>
<p class="signature">Marc Delisle</p>
</div>

<div class="floatbox book">

<h3>Mastering phpMyAdmin 2.11 for Effective MySQL Management</h3>

<a href="http://www.packtpub.com/phpmyadmin-3rd-edition/book"><img src="${base_url}images/books/pma_en_100x123.png" alt="Book cover" width="100" height="123" /></a>

<p>
This version of the book is up to date with the 2.11.x series. A percentage of the book's sales is <a href="http://www.packtpub.com/article/open_source_receives_royalties_boost">donated</a> to help phpMyAdmin.
</p>

<p>For more information, please visit <a href="http://www.packtpub.com/phpmyadmin-3rd-edition/book">the book's site</a>.</p>
<p class="signature">Marc Delisle</p>
</div>


<div class="floatbox book">

<h3>phpMyAdmin - efektivní správa MySQL</h3>

<a href="http://www.zonerpress.cz/kniha-phpmyadmin-efektivni-sprava-mysql.html"><img src="${base_url}images/books/pma_cz_90x122.jpg" alt="Book cover" width="90" height="122" /></a>

<p xml:lang="cs">
V edici encyklopedie webdesignera vychází tentokrát ryze praktická kniha – kompletní a podrobná příručka pro uživatele phpMyAdmin, grafického rozhraní pro efektivní správu serveru a databází MySQL. Kniha popisuje v době vydání aktuální českou verzi phpMyAdmin 2.6.0, která obsahuje celou řadu novinek, rozšíření a vylepšení oproti verzi předchozí.
</p>

<p xml:lang="cs">
phpMyAdmin nabízí uživatelům ucelený systém pro komplexní manipulaci s databázemi a tabulkami MySQL. Systémovým administrátorům poskytuje nástroje pro správu uživatelů a jejich oprávnění. Kniha pokrývá oba úhly pohledu, obsahuje navíc i poznámky o používání SQL v rámci MySQL, předvádí některé nedokumentované možnosti a vlastnosti.
</p>

<p xml:lang="cs">
Pro více informací navštivte stránku věnovanou
<a href="http://www.zonerpress.cz/kniha-phpmyadmin-efektivni-sprava-mysql.html">českému vydání knihy</a>.
</p>

</div>
                
<div class="floatbox book">
<h3>Dominar phpMyAdmin para una administraci&oacute;n efectiva de MySQL</h3>

<a href="http://www.packtpub.com/dominary-phpMyAdmin-es"><img src="${base_url}images/books/pma_es_100x123.png" alt="Book cover" width="100" height="123" /></a>

<p xml:lang="es">
Este libro es una gu&iacute;a completa que le ayuda a sacar partido del potencial de phpMyAdmin. Ya sea un programador experimentado, un administrador de sistemas, un dise&ntilde;ador Web o nuevo a las tecnolog&iacute;as de MySQL y phpMyAdmin, este libro le mostrar&aacute; como aumentar su productividad y control cuando trabaje con MySQL. Por ello se ha traducido, de modo que esta gu&iacute;a completa sea m&aacute;s accesible al lector espa&ntilde;ol.
</p>

<p>
<a href="http://www.packtpub.com/dominary-phpMyAdmin-es">Packt Publishing</a>
</p>

</div>

<div class="clearer"></div>

</div>

<xi:include href="_page.tpl" />
</html>
