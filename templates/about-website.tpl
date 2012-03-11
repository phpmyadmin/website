<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">About Website</py:def>

<div py:match="content" id="body">

<h2>About Website</h2>

<p>
This website is implemented in <a href="http://python.org/">Python</a>, uses
<a href="http://code.google.com/p/feedparser/">FeedParser</a> and 
<a href="http://gitorious.org/projects/git-python/">GitPython</a> to grab 
external data and <a href="http://genshi.edgewall.org/">Genshi</a> to generate 
web pages. Source code of it is available in the Github repository 
<code><a href="https://github.com/phpmyadmin/website">phpmyadmin/website</a></code> 
 (see <a href="${base_url}devel.${file_ext}">developer information</a> 
for information how to access it).
</p>

<p>
Site design and logic has been created by <a href="${base_url}team.${file_ext}#michal">Michal
Čihař</a> and it is hosted on 
<a href="http://sourceforge.net">SourceForge.net</a>.
</p>

<p>
Site should be valid XHTML and CSS, where it makes sense, we try to use 
<a href="http://microformats.org/">Microformats</a>. We also try to make
website <a href="http://www.w3.org/WAI/WCAG1AAA-Conformance">accessible</a>.
</p>

<h2>About phpMyAdmin</h2>

<p>
There is a dedicated page to <a
href="${base_url}about.${file_ext}">information about phpMyAdmin and it's
history</a>.
</p>

<h2 id="syndicate">Syndication</h2>

<p>Following RSS feeds are available for syndication:</p>

<ul>
<li><a href="${rss_news}">phpMyAdmin project news</a></li>
<li><a href="${rss_summary}">phpMyAdmin project summary</a></li>
<li><a href="${rss_files}">phpMyAdmin file releases</a></li>
<li><a href="${rss_security}">phpMyAdmin security issues</a></li>
<li><a href="${rss_donations}">phpMyAdmin donations</a></li>
<li><a href="${rss_vcs}">phpMyAdmin commits</a></li>
</ul>

<p>phpMyAdmin software information is available in following machine readable formats:</p>

<ul>
<li><a href="http://www.asp-shareware.org/pad/">PAD</a>: <a href="http://www.phpmyadmin.net/home_page/phpmyadmin.xml">http://www.phpmyadmin.net/home_page/phpmyadmin.xml</a></li>
<li><a href="http://trac.usefulinc.com/doap">DOAP</a>: <a href="http://www.phpmyadmin.net/home_page/phpmyadmin-doap.xml">http://www.phpmyadmin.net/home_page/phpmyadmin-doap.xml</a></li>
</ul>

</div>

<xi:include href="_page.tpl" />
</html>
