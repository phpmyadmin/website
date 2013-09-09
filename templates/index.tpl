<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_rss">${rss_news}</py:def>
<py:def function="page_rss_title">phpMyAdmin project news</py:def>

<div py:match="content" id="body">

<div class="hitbuttons">
<xi:include href="_littleboxes.tpl" />
</div>

<xi:include href="_sponsors.tpl" />

<h2>phpMyAdmin turns 15!</h2>
Read our <a href="${base_url}15-years.${file_ext}">celebration page</a>.

<h2>About</h2>

<p>
phpMyAdmin is a free software tool written in <a href="http://php.net">PHP</a>,
intended to handle the administration of <a href="http://mysql.com">MySQL</a>
over the Web. phpMyAdmin supports a wide range of operations on MySQL, 
MariaDB and Drizzle. Frequently used operations (managing databases, tables, 
columns, relations, indexes, users, permissions, etc) can be performed via the 
user interface, while you still have the ability to directly execute any SQL statement.  
</p>

<div class="bookbanner">
<a href="${base_url}docs.${file_ext}#books" id="fader">
<img src="images/books/pma_en_3.4_150x185.png" alt="phpMyAdmin book" />
<img src="images/books/pma_starter_150x184.jpg" alt="phpMyAdmin Starter" />
</a>
</div>

<p>
phpMyAdmin comes with a wide range of <a
href="${base_url}docs.${file_ext}">documentation</a> and users are welcome to
update <a href="http://wiki.phpmyadmin.net/">our wiki pages</a> to share ideas and
howtos for various operations. The <a
href="${base_url}team.${file_ext}">phpMyAdmin team</a> will try to help you if
you face any problem; you can use a <a
href="${base_url}support.${file_ext}">variety of support channels</a> to get
help.
</p>

<p>
phpMyAdmin is also very deeply documented in a book written by one of the developers
&ndash; <a href="http://link.packtpub.com/XJdqZr">Mastering phpMyAdmin for
Effective MySQL Management</a>, which is available in English and <a href="${base_url}docs.${file_ext}#books">Spanish</a>.
</p>

<p>
To ease usage to a wide range of people, phpMyAdmin is being translated into <a
href="${base_url}translations.${file_ext}">72 languages</a> and supports both LTR
and RTL languages.
</p>

<p>
phpMyAdmin has won several <a href="${base_url}awards.${file_ext}">awards</a>.
Among others, it was chosen as the best PHP application in various awards and
has won every year the SourceForge.net Community Choice Awards as &quot;Best Tool or Utility for SysAdmins&quot;.
</p>

<p>
phpMyAdmin is a fourteen-year-old project with a stable and flexible code
base; you can find out more about the <a href="${base_url}about.${file_ext}">project and its history</a>.
</p>

<div class="floatbox">
    <h2>Features</h2>
    <ul>
        <li>Intuitive web interface</li>
        <li>Support for most MySQL features:
        <ul>
            <li>browse and drop databases, tables, views, fields and indexes</li>
            <li>create, copy, drop, rename and alter databases, tables, fields and
                indexes</li>
            <li>maintenance server, databases and tables, with proposals on server
                configuration</li>
            <li>execute, edit and bookmark any
                <abbr title="structured query language">SQL</abbr>-statement, even
                batch-queries</li>
            <li>manage MySQL users and privileges</li>
            <li>manage stored procedures and triggers</li>
        </ul>
        </li>
        <li>Import data from 
            <abbr title="comma separated values">CSV</abbr> and
            <abbr title="structured query language">SQL</abbr>
            </li>
        <li>Export data to various formats:
            <abbr title="comma separated values">CSV</abbr>,
            <abbr title="structured query language">SQL</abbr>,
            <abbr title="Extensible Markup Language">XML</abbr>,
            <abbr title="Portable Document Format">PDF</abbr>,
            <abbr title="International Organization for Standards">ISO</abbr>/<abbr
            title="International Electrotechnical Commission">IEC</abbr> 26300 -
            OpenDocument Text and Spreadsheet,
            <abbr title="Microsoft Word 2000">Word</abbr>,
            L<sup>A</sup>T<sub><em class="big">E</em></sub>X
            and others
            </li>
        <li>Administering multiple servers</li>
        <li>Creating <abbr title="Portable Document Format">PDF</abbr> graphics of
            your database layout</li>
        <li>Creating complex queries using Query-by-example (QBE)</li>
        <li>Searching globally in a database or a subset of it</li>
        <li>Transforming stored data into any format using a set of predefined
            functions, like displaying BLOB-data as image or download-link
            </li>
        <li>And much more...</li>
    </ul>
</div>

<div class="floatbox hslice" id="latest-news">
    <h2 class="entry-title"><a href="${base_url}news.${file_ext}">Latest News</a></h2>
    <ul>
    <li py:for="item in short_news">
        <a href="${base_url}news.${file_ext}#${item.anchor}">${item.title}</a> (${item.date})
    </li>
    </ul>
    <p class="signature"><a href="${base_url}news.${file_ext}">...more news.</a></p>
</div>

<div class="floatbox hslice" id="latest-blogs">
    <h2 class="entry-title"><a href="http://planet.phpmyadmin.net/">Latest Posts in Developers Blogs</a></h2>
    <ul>
    <li py:for="item in short_blogs">
        <a href="${item.link}">${item.title}</a> (${item.date})
    </li>
    </ul>
    <p class="signature"><a href="http://planet.phpmyadmin.net/">...more blogs.</a></p>
</div>

<div class="clearer"></div>

</div>

<xi:include href="_page.tpl" />
</html>
