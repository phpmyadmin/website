<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_rss">${rss_news}</py:def>

<div py:match="content" id="body">

<py:for each="release in releases">
    <div class="downloadbutton">
    <span class="dlname">Download <a href="${release.notes}">${release.version}</a>:</span>
    <ul class="dllist">
    <py:for each="file in release.files"><py:if test="file.featured">
        <li><a href="${file.url}">${file.ext}</a></li>
    </py:if></py:for>
    </ul> 
    </div>
</py:for>


    <h2>About</h2>
   <p>
   phpMyAdmin is a tool written in PHP intended to handle the administration
   of MySQL over the Web. Currently it can create and drop databases,
   create/drop/alter tables, delete/edit/add fields, execute any SQL statement,
   manage keys on fields, manage privileges,export data into various formats
   and is available in 55 languages.</p>

   <h2>Features</h2>
   <ul>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>Intuitive web interface</li>
    <li>And much more...</li>
   </ul>

   <h2>Mailing lists</h2>
   <ul>
     <li>For users: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-users">phpmyadmin-users@lists.sourceforge.net</a></li>
     <li>For developers: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-devel">phpmyadmin-devel@lists.sourceforge.net</a></li>
     <li>SVN commit notifications: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-svn">phpmyadmin-svn@lists.sourceforge.net</a></li>
   </ul>
</div>

<xi:include href="_page.tpl" />
</html>
