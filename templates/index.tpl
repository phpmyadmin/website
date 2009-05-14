<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_rss">${rss_news}</py:def>
<py:def function="page_rss_title">phpMyAdmin project news</py:def>

<div py:match="content" id="body">

<xi:include href="_littleboxes.tpl" />

<h2>About</h2>

<p>
phpMyAdmin is a free software tool written in <a href="http://php.net">PHP</a>
intended to handle the administration of <a href="http://mysql.com">MySQL</a>
over the World Wide Web. phpMyAdmin supports a wide range of operations with 
MySQL. The most frequently used operations are supported by the user interface
 (managing databases, tables, fields, relations, indexes, users, permissions, 
etc), while you still have the ability to directly execute any SQL statement.  
</p>

<div class="bookbanner">
<a href="${base_url}docs.${file_ext}#books" id="fader">
<img src="images/books/pma_en_3.1_100x123.png" alt="phpMyAdmin book" />
<img src="images/books/pma_en_100x123.png" alt="phpMyAdmin book" />
<img src="images/books/pma_cz_90x122.jpg" alt="phpMyAdmin book" />
<img src="images/books/pma_de_90x122.jpg" alt="phpMyAdmin book" />
<img src="images/books/pma_es_100x123.png" alt="phpMyAdmin book" />
</a>
</div>

<p>
phpMyAdmin comes with a wide range of <a
href="${base_url}docs.${file_ext}">documentation</a> and users are welcome to
update <a href="http://wiki.phpmyadmin.net/">our wiki pages</a> to share ideas and
howtos for various operations. The <a
href="${base_url}team.${file_ext}">phpMyAdmin team</a> will try to help you if
you face any problem, you can use <a
href="${base_url}support.${file_ext}">variety of support channels</a> to get
help.
</p>

<p>
phpMyAdmin is also very deeply documented in a book written by one of developers
&ndash; <a href="${base_url}docs.${file_ext}#books">Mastering phpMyAdmin for
Effective MySQL Management</a>, which is available in English, Czech, German
and Spanish.
</p>

<p>
To ease usage to a wide range of people, phpMyAdmin is translated into <a
href="${base_url}translations.${file_ext}">55 languages</a> and supports both LTR
and RTL languages.
</p>

<p>
Since version 3.0.0, phpMyAdmin joined the <a
href="${base_url}gophp5.${file_ext}">GoPHP5 initiative</a> and dropped
compatibility code for older PHP and MySQL versions; version 3 and later requires
at least PHP 5.2 and MySQL 5. To use with older PHP or MySQL versions, use
the older (but still maintained) branch of 2.x releases, which you can find on the <a
href="${base_url}downloads.${file_ext}">download page</a>.
</p>

<p>
phpMyAdmin has won several <a href="${base_url}awards.${file_ext}">awards</a>.
Among others, it was chosen as the best PHP application in various awards and
every year wins the SourceForge.net Community Choice Awards as &quot;Best Tool or
Utility for SysAdmins&quot;.
</p>

<p>
phpMyAdmin is a more than ten years old project with stable and flexible code
base, to find out more about the project and its history see <a
href="${base_url}about.${file_ext}">separate page</a>.
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
            <abbr title="Microsoft Excel 2000">Excel</abbr>, L<sup>A</sup>T<sub><big>E</big></sub>X 
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
    <h2 class="entry-title">Latest News</h2>
    <ul>
    <li py:for="item in short_news">
        <a href="${base_url}news.${file_ext}#${item.anchor}">${item.title}</a> (${item.date})
    </li>
    </ul>
    <p class="signature"><a href="${base_url}news.${file_ext}">...more news.</a></p>
</div>

<div class="floatbox hslice" id="latest-blogs">
    <h2 class="entry-title">Latest Blogs</h2>
    <ul>
    <li py:for="item in short_blogs">
        <a href="${item.link}">${item.title}</a> (${item.date})
    </li>
    </ul>
    <p class="signature"><a href="http://pmaplanet.cihar.com/">...more blogs.</a></p>
</div>

<div class="clearer"></div>

</div>

<xi:include href="_page.tpl" />
</html>
