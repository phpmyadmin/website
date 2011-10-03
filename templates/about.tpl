<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_rss">${rss_summary}</py:def>
<py:def function="page_rss_title">phpMyAdmin project summary</py:def>

<py:def function="page_title">About</py:def>

<div py:match="content" id="body">

<h2>History</h2>

<p>
Tobias Ratschiller, then an IT consultant and later founder of the software
company Maguma, started to work on a PHP-based web front-end to MySQL in 1998,
inspired by Peter Kuppelwieser's MySQL-Webadmin. He gave up the project (and
phpAdsNew, of which he was also the original author) in 2000 because of lack
of time.
</p>

<p>
By that time, phpMyAdmin had already become one of the most popular PHP
applications and MySQL administration tools, with a large community of users
and contributors. In order to coordinate the growing number of patches, a
group of three developers, Olivier Müller, Marc Delisle and Loïc Chapeaux,
registered the phpMyAdmin project at <a
href="http://sourceforge.net/">SourceForge.net</a> and took over the
development in 2001.
</p>


<h2>Milestone releases</h2>

<ul>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_0.9.0">0.9.0</a> (September 9, 1998): First internal release.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_1.1.0">1.1.0</a> (November 3, 1998): Added first confirmations for DROP commands.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_1.2.0">1.2.0</a> (November 29, 1998): Added possibility to import from text files.</li>

<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_1.3.0">1.3.0</a> (December 16, 1998): Added query by example functionality.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_1.3.1">1.3.1</a> (December 27, 1998): First multi-lingual version.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_1.4.0">1.4.0</a> (January 16, 1999): Added support for renaming and copying tables.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.0.0">2.0.0</a> (April 11, 1999): Major layout changes.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.1.0">2.1.0</a> (June 8, 2000): Last release by the original developer Tobias Ratschiller.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.2.0">2.2.0</a> (August 31, 2001): First stable release made by the phpMyAdmin project.</li>

<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.3.0">2.3.0</a> (November 8, 2001): Database and table views were split into smaller sections.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.5.0">2.5.0</a> (November 5, 2003): Introduction of the MIME-based transformation system.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.6.0">2.6.0</a> (September 27, 2004): Improved character set handling and support for MySQL 4.</li>

<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.7.0">2.7.0</a> (December 4, 2005): Improved importing capabilities, simplified configuration and interface cleanup.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.8.0">2.8.0</a> (March 6, 2006): Compatibility updates, hiding databases, configurable memory limits, web-based setup.</li>

<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.9.0">2.9.0</a> (September 20, 2006): Added export to OpenDocument Text and Spreadsheet.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.10.0">2.10.0</a> (February 27, 2007): GUI for relations, called Database Designer.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_2.11.0">2.11.0</a> (August 22, 2007): Supports creating VIEWS from query results, manages triggers, procedures and functions. Improved interface for servers handling large number of databases/tables.</li>

<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_3.0.0">3.0.0</a> (September 27, 2008): Requires PHP 5.2 and MySQL 5+. Supports EVENT and TRIGGER.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_3.1.0">3.1.0</a> (November 28, 2008): Added support for BLOBStreaming, Swekey hardware authentication and rewritten setup script.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_3.2">3.2.0</a> (June 9, 2009): Added many small features.</li>
<li><a href="http://wiki.phpmyadmin.net/pma/phpMyAdmin_3.3">3.3.0</a> (March 7, 2010): Added new import and export modules, changes tracking, synchronization and support for replication configuration.</li>
<li>3.4.0 (May 11, 2011): AJAXification of some parts, charts, visual query builder, user preferences, ENUM/SET editor.</li>
</ul>


<h2>Name</h2>

<p>
phpMyAdmin name is obviously mixture of PHP as a language it uses, MySQL as a
database it manages and administration as the activity it handles. Even thought
the name seems to be quite simple, many people mix it up and they refer to
phpMyAdmin under different names, such as myphpadmin, phpadmin, phpmysqladmin
(these are three most frequent Google searches going to this website besides
correctly spelled variant).
</p>

<h2>Factoids</h2>

<p>
phpMyAdmin project currently has <a
href="${links.developers}">${info.developers} developers</a>. Over the life of
project on SourceForge.net, users have downloaded ${info.downloads} copies of
phpMyAdmin, wrote ${info.forumposts} posts into <a
href="${links.forums}">${info.forums} forums</a> and discussed various topics
in <a href="${links.mailinglists}">${info.mailinglists} mailing lists</a>.
</p>

<h2>Tracker Statistics</h2>

<table class="graph sortable" id="sorttable">
<thead>
<tr>
    <th class="forward_sort">Tracker</th>
    <th>Description</th>
    <th>Open issues</th>
    <th>Total issues</th>
</tr>
</thead>

<tbody>
<tr py:for="tracker in trackers">
<td class="name"><a href="${tracker.link}">${tracker.name}</a></td>
<td class="name">${tracker.description}</td>
<td class="size">${tracker.open}</td>
<td class="size">${tracker.total}</td>
</tr>
</tbody>
</table>

</div>

<xi:include href="_page.tpl" />
</html>
