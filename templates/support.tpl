<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Support</py:def>

<div py:match="content" id="body">

<div class="floatbox">
<h2>Getting support</h2>

<p>
The easiest way to get support is to use the <a href="https://sourceforge.net/projects/phpmyadmin/forums/forum/72909">help forum</a>
but we're ready to help on IRC or mailing list as well. Check below for more options.
</p>
</div>


<div class="floatbox">
<h2>Forum / IRC</h2>
<ul>
   <li><strong><a href="https://sourceforge.net/p/phpmyadmin/discussion/Help/">Help Forum</a></strong></li>
   <li><a href="https://sourceforge.net/p/phpmyadmin/discussion/Aide/">Forum d'aide (en français)</a></li>
   <li><a href="https://sourceforge.net/p/phpmyadmin/discussion/Hilfe/">Anwenderforum (auf Deutsch)</a></li>
   <li>IRC: #phpmyadmin on <a href="http://freenode.net/">irc.freenode.net</a></li>
</ul>
</div>

<div class="floatbox">
<h2>Trackers</h2>

<p>
Trackers on SourceForge.net are used to track bug reports, requests for new features or proposed patches.
</p>

<ul>
    <li py:for="tracker in trackers"><a href="${tracker.link}">${tracker.name}</a> - ${tracker.description}</li>
</ul>
</div>

<div class="floatbox">
<h2>Mailing Lists</h2>
<ul>
    <li>For news/announcements: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-news">phpmyadmin-news@lists.sourceforge.net</a></li>
    <li>For users: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-users">phpmyadmin-users@lists.sourceforge.net</a></li>
    <li>For developers: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-devel">phpmyadmin-devel@lists.sourceforge.net</a></li>
    <li>For translators: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-translators">phpmyadmin-translators@lists.sourceforge.net</a></li>
    <li>Git commit notifications: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-git">phpmyadmin-git@lists.sourceforge.net</a></li>
    <li><a href="http://sourceforge.net/mail/?group_id=23067">Mailing lists overview</a></li>
</ul>
</div>

<div class="floatbox">
<h2>Commercial Support</h2>

<p>
If you want to receive commercial support for phpMyAdmin, either as help with
installation or implementing custom features, do not hesitate to contact us on
<a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-devel">development mailing list</a>. 
Please note that these services are not in any connection with phpMyAdmin team and we can not guarantee accurate information or quality of service for them. 
</p>

</div>

<div class="clearer"></div>
</div>

<xi:include href="_page.tpl" />
</html>
