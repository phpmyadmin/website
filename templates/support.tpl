<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Support</py:def>

<div py:match="content" id="body">

<div class="floatbox">
<h2>Forum / IRC</h2>
<ul>
   <li><strong><a href="http://sourceforge.net/forum/forum.php?forum_id=72909">Help Forum</a></strong></li>
   <li><a href="http://sourceforge.net/forum/forum.php?forum_id=296543">Forum d'aide (en français)</a></li>
   <li><a href="http://sourceforge.net/forum/forum.php?forum_id=297172">Anwenderforum (auf Deutsch)</a></li>
   <li>IRC: #phpmyadmin on <a href="http://freenode.net/">irc.freenode.net</a></li>
</ul>
</div>

<div class="floatbox">
<h2>Trackers</h2>
<ul>
    <li py:for="tracker in trackers"><a href="${tracker.link}">${tracker.name}</a> - ${tracker.description}</li>
</ul>
</div>

<div class="floatbox">
<h2>Mailing Lists</h2>
<ul>
    <li>For users: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-users">phpmyadmin-users@lists.sourceforge.net</a></li>
    <li>For developers: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-devel">phpmyadmin-devel@lists.sourceforge.net</a></li>
    <li>SVN commit notifications: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-svn">phpmyadmin-svn@lists.sourceforge.net</a></li>
    <li><a href="http://sourceforge.net/mail/?group_id=23067">Mailing lists overview</a></li>
</ul>
</div>

<div class="floatbox">
<h2>Commercial Support</h2>

<p>
If you want to receive commercial support for phpMyAdmin, either as help with
installation or implementing custom features, do not hesitate to contact us on
<a
href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-devel">development
mailing list</a>. There are also third party service providers listed on
<a
href="https://sourceforge.net/services/project_services.php?project_id=23067&amp;showListings=true">SourceForge.net
Marketplace</a>. Please note that these services are not in any connection
with phpMyAdmin team and we can not guarantee accurate information or quality
of service for them.
</p>

</div>

<div class="floatbox">
<h2>Security Issues</h2>

<xi:include href="_security_contact.tpl" />

</div>

<div class="clearer"></div>
</div>

<xi:include href="_page.tpl" />
</html>
