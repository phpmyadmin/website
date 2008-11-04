<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_rss">${rss_news}</py:def>

<div py:match="content" id="body">

<xi:include href="_littleboxes.tpl" />

<h2>About</h2>

<p>
phpMyAdmin is a free software tool written in PHP intended to handle the
administration of the MySQL over the World Wide Web. phpMyAdmin supports wide
range of operations with MySQL. Most frequently used operations are supported
by user interface (managing databases, tables, fields, relations, indexes,
users, permissions, etc), while you still have ability to directly execute any
SQL statement.  
</p>

<script type="text/javascript">
//<![CDATA[
var counter = 1;
var banArray = new Array(4);
if(document.images) {
    banArray[0] = new Image(97,123);
    banArray[0].src = "images/books/pma_en_100x123.png";
    banArray[1] = new Image(90,122);
    banArray[1].src = "images/books/pma_cz_90x122.jpg";
    banArray[2] = new Image(90,122);
    banArray[2].src = "images/books/pma_de_90x122.jpg";
    banArray[3] = new Image(100,123);
    banArray[3].src = "images/books/pma_es_100x123.png";
}
function changeBanner() {
    if(counter > 3)
       counter = 0;
    document.bookbanner.src = banArray[counter].src;
    counter++;
}
var timer = window.setInterval("changeBanner()", 10000);
//]]>
</script>


<div class="bookbanner">
<a href="${base_url}docs.${file_ext}#books">
<img src="images/books/pma_en_100x123.png" width="100" height="123" id="bookbanner" alt="phpMyAdmin books" />
</a>
</div>

<p>
To ease usage to wide range of people, phpMyAdmin is translated to <a
href="${base_url}languages.${file_ext}">55 languages</a> and supports both LTR
and RTL languages.
</p>

<p>
phpMyAdmin comes with wide range of <a
href="${base_url}docs.${file_ext}">documentation</a> and users are welcome to
update <a href="http://wiki.cihar.com/">our wiki pages</a> to share ideas and
howtos for various operations.
</p>

<p>
phpMyAdmin is also very deeply documented in book written by one of developers
&ndash; <a href="${base_url}docs.${file_ext}#books">Mastering phpMyAdmin for
Effective MySQL Management</a>, which is available in English, Czech, German
and Spanish.
</p>

<p>
Since version 3.0.0, phpMyAdmin dropped compatibility code for older PHP and
MySQL versions and you require PHP 5.2 and MySQL 5+ to use it. To use with
older PHP or MySQL versions, use older (but still maintained) branch of 2.x
releases.
</p>

<div class="floatbox">
    <h2>Features</h2>
    <ul>
        <li>Intuitive web interface</li>
        <li></li>
        <li>And much more...</li>
    </ul>
</div>

<div class="floatbox">
    <h2>Latest News</h2>
    <ul>
    <li py:for="item in shortnews">
        <a href="${base_url}news.${file_ext}#${item.anchor}">${item.title}</a> (${item.date})
    </li>
    </ul>
    <p class="signature"><a href="${base_url}news.${file_ext}">...more news.</a></p>
</div>

<div class="clearer"></div>

    <h2>Mailing lists</h2>
    <ul>
        <li>For users: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-users">phpmyadmin-users@lists.sourceforge.net</a></li>
        <li>For developers: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-devel">phpmyadmin-devel@lists.sourceforge.net</a></li>
        <li>SVN commit notifications: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-svn">phpmyadmin-svn@lists.sourceforge.net</a></li>
    </ul>

</div>

<xi:include href="_page.tpl" />
</html>
