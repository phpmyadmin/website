<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Improve</py:def>

<div py:match="content" id="body">

<h2>Improve phpMyAdmin</h2>

<p>
As a free software project, phpMyAdmin is very open to your contributions. You don't
need developer skills to help, there are several non-coding ways to get involved
in a project (code is welcome too, of course!).
</p>

<p>Ways in which you can contribute:</p>
<ul>
  <li><a href="#devel">program</a> new features,</li>
  <li>report <a href="http://sourceforge.net/tracker/?atid=377408&amp;group_id=23067">bugs</a> (errors in the program),</li>
  <li>debug existing features,</li>

  <li>improve documentation or the <a href="http://wiki.phpmyadmin.net/">wiki</a>,</li>
  <li><a href="#translate">translate phpMyAdmin</a> to your own language,</li>
  <li><a href="#translate">translate the documentation</a>,</li>
  <li>help other users on <a href="https://sourceforge.net/forum/?group_id=23067">forums</a>,</li>

  <li>distribute phpMyAdmin,</li>
  <li><a href="${base_url}donate.${file_ext}">donate money</a> to the project,</li>
</ul>

<p>As you can see, everyone can help.</p>

<h2><a id="devel"></a>Developing</h2>

<p>
phpMyAdmin is (as the name says) written in PHP and uses MySQL. Besides this,
we also need people skilled in HTML, JavaScript and CSS, as these are parts
which make our user interface. You don't have to be expert in all these areas
- even knowing only one of them, you can still provide substantial help in
creating or debugging some features.
</p>

<p>
For storing our code we use <a href="http://subversion.tigris.org/">Subversion</a>.
If you don't know it, you can get some basic facts in <a
href="http://en.wikipedia.org/wiki/Subversion_(software)">Wikipedia</a> or
reference in the comprehensive book <a href="http://svnbook.red-bean.com/">Version Control with
Subversion</a>.
</p>

<p>
If you are looking for some simple task where you can start, check out
our wiki page with <a href="http://wiki.phpmyadmin.net/pma/Dev:Junior">junior 
jobs</a> where you can find some tips where to look.
</p>

<h3>Source Code Repository</h3>
<xi:include href="_svndl.tpl" />

<p>
To start development you want to start with <code>trunk/phpMyAdmin</code>,
where the current development version of phpMyAdmin is stored. Other interesting
parts of repository include:
</p>

<dl class="cvslist">
<dt>trunk/</dt><dd>Current development version of all code.</dd>
<dt>trunk/phpMyAdmin</dt><dd>phpMyAdmin code.</dd>
<dt>trunk/website</dt><dd>Website code.</dd>
<dt>trunk/themes</dt><dd>Themes.</dd>
<dt>trunk/data</dt><dd>Various project related data (such as logos, T-shirt graphics, etc.).</dd>
<dt>trunk/history</dt><dd>Some historical documents (old changelogs or website).</dd>
<dt>trunk/planet</dt><dd><a href="http://planet.phpmyadmin.net/">Planet phpMyAdmin</a> configuration.</dd>
<dt>trunk/localized_docs</dt><dd>Not used anymore, see Git section bellow.</dd>
<dt>tags/</dt><dd>Tags for all released versions (as <code>RELEASE_X_Y_Z</code>)</dd>
<dt>tags/STABLE</dt><dd>Special moving tag which always contains latest
released stable version</dd>
<dt>tags/TESTING</dt><dd>Special moving tag which always contains latest
released testing version</dd>
<dt>branches/</dt><dd>Maintenance branches for older versions (as <code>QA_X_Y</code>)</dd>
</dl>

<p>
Examples of how to checkout phpMyAdmin code:
</p>

<pre>
#  Latest development version:
svn checkout https://phpmyadmin.svn.sourceforge.net/svnroot/phpmyadmin/trunk/phpMyAdmin phpMyAdmin-dev
# Latest stable version:
svn checkout https://phpmyadmin.svn.sourceforge.net/svnroot/phpmyadmin/tags/STABLE/phpMyAdmin phpMyAdmin-stable
</pre>

<h3>Git Repository</h3>

<p>
phpMyAdmin is currently considering to switch development to Git. These 
repositories do not yet contain current code are used mostly for testing.
</p>

<p>
Git repository are located at
<code>git://phpmyadmin.git.sourceforge.net/gitroot/phpmyadmin/</code> and you
can browse it online using <a
href="http://phpmyadmin.git.sourceforge.net/git/gitweb-index.cgi">Gitweb</a>.
</p>

<p>
Following repositories are already used for development:
</p>

<dl class="cvslist">
<dt>trunk/localized_docs</dt><dd>Localized documentation.</dd>
</dl>

<h3>Repository Statistics</h3>
<p>Several analyses of the repository are available:</p>
<ul>
<li><a href="http://www.phpmyadmin.net/svnstats/">mpy-svn-stats</a></li>
<li><a href="http://cia.vc/stats/project/phpmyadmin/">CIA.vc</a></li>
<li><a href="http://www.ohloh.net/projects/phpmyadmin">Ohloh</a></li>
<li><a href="https://sourceforge.net/project/stats/detail.php?group_id=23067&amp;ugn=phpmyadmin&amp;type=svn">SourceForge.net</a></li>
</ul>

<h3>Coding Standards</h3>
<p>
Standards should be obeyed in all cases when possible. Generated content
should be valid XHTML 1.0 and CSS. PHP code should match <a
href="http://pear.php.net/manual/en/standards.php">PEAR Coding Standards</a>
and documented using <a href="http://www.phpdoc.org/">phpDocumentator</a>.
</p>

<h3>Developer Documentation</h3>

<p>More documentation can be found in the following places:</p>
<ul>
<li><a href="http://wiki.phpmyadmin.net/pma/Devel:Main">Developers wiki</a></li>
<li><a href="http://www.phpmyadmin.net/phpdoc/">Documentation of phpMyAdmin
(autogenerated)</a></li>
</ul>

<h2><a id="translate"></a>Translating</h2>

<p>
For localization, phpMyAdmin uses its own simple localization system - each
translation has its own PHP file with all texts. All these files are encoded in
UTF-8 (if you see another encoding, you're using an old version). To translate,
you have to follow steps described in <a
href="http://wiki.phpmyadmin.net/pma/FAQ_7.2">FAQ 7.2</a>.
</p>

<p>
Documentation is being translated using po4a and gettext (see <a
href="${base_url}docs.${file_ext}">documentation</a> for existing
translations). To start, checkout <code><a
href="http://phpmyadmin.svn.sourceforge.net/viewvc/phpmyadmin/trunk/localized_docs/po/">localized_docs/po</a></code> from SVN, or
just go to <a href="https://l10n.cihar.com/projects/pmadoc/">translation
server</a> and translate it online. If your language is missing, just contact
<a href="mailto:michal@cihar.com">Michal Čihař</a>, he will add it.  If you
prefer to translate directly the po files, please put updated ones into our <a
href="https://sourceforge.net/tracker/?group_id=23067&amp;atid=387645">translation
tracker</a>.
</p>

</div>

<xi:include href="_page.tpl" />
</html>
