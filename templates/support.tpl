<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Support</py:def>

<div py:match="content" id="body">

<div class="floatbox">
<h2>Getting support</h2>

<p>
In an effort to consolidate the support options into just one, the
phpMyAdmin team announces that, effective September 1st, 2013, support has moved to <a href="http://stackoverflow.com/tags/phpmyadmin/info">stackoverflow</a>.
All prior support mechanisms (the phpmyadmin-users mailing list, the help forums, IRC channel, support-request tracker) have been deprecated.
<br />
<br />
The way of reporting (security) bugs and adding feature requests will be unaffected.
</p>
</div>

<div class="floatbox">
<h2>Version 3.5.x being phased out</h2>

<p>
This older version is only supported for security fixes, until Jan 1, 2014.
</p>
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
    <li>For developers: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-devel">phpmyadmin-devel@lists.sourceforge.net</a></li>
    <li>For translators: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-translators">phpmyadmin-translators@lists.sourceforge.net</a></li>
    <li>Git commit notifications: <a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-git">phpmyadmin-git@lists.sourceforge.net</a></li>
    <li><a href="http://sourceforge.net/p/phpmyadmin/mailman/">Mailing lists overview</a></li>
</ul>
</div>

<div class="floatbox">
<h2>Commercial Support</h2>

<p>
If you want to receive commercial support for phpMyAdmin, either as help with
installation or implementing custom features, do not hesitate to contact the 
<a href="https://lists.sourceforge.net/mailman/listinfo/phpmyadmin-devel">development mailing list</a>. 
Please note that these services are not in any way connected with the phpMyAdmin team and we can not guarantee accurate information or quality of service for them. 
</p>

</div>

<div class="clearer"></div>
</div>

<xi:include href="_page.tpl" />
</html>
