<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Team</py:def>

<div py:match="content" id="body">

<h2>Team</h2>

<p>
The phpMyAdmin development team has been organized on <a
href="http://sourceforge.net/projects/phpmyadmin/">SourceForge.net</a> since
it's start in 2001. They are responsible for the development of phpMyAdmin and represents
it at various conferences.
</p>

<div class="floatbox">
<h3>Marc Delisle</h3>
<img class="head" src="${base_url}images/heads/marc.png" alt="Marc Delisle" />
<p>
Marc took over the phpMyAdmin project from founder Tobias Ratschiller and
started a new era of phpMyAdmin together with Olivier Müller and Loïc Chapeaux
in 2001. 
</p>
<p>
He is currently the project administrator and he has contributed the largest amount of
code to the project. He lives in Québec, Canada.
</p>
</div>

<div class="floatbox">
<h3>Michal Čihař</h3>
<img class="head" src="${base_url}images/heads/nijel.png" alt="Michal Čihař" />
<p>
Michal made his first contribution to phpMyAdmin in 2001 by updating the Czech
translation. Later he contributed charset conversion code and improved export
and import handling to support plugins.
</p>
<p>
He currently maintains the project web site, demo server, wiki and other useful
services. He lives in Prague, Czech Republic.
</p>
</div>

<div class="floatbox">
<h3>Sebastian Mendel</h3>
<img class="head" src="${base_url}images/heads/sebastian.png" alt="Sebastian Mendel" />
<p>
Sebastian has been a member of the phpMyAdmin development team since 2005. He did major
work on improving user interface and introduced the use of classes in the phpMyAdmin
code.
</p>
<p>
He lives in Leipzig, Germany.
</p>
</div>

<div class="clearer"></div>

<h2>Team meetings</h2>

<p>
We would like to meet other members of the team more often, but so far only a
single team meeting in real life has happened. It was at big party in Karlsruhe,
Germany for the 10th anniversary of PHP and MySQL at the 
<a href="http://www.linuxtag.org/2005">LinuxTag</a>
<a href="http://www.lamparea.org/">LAMP Area</a>, with some special
guests.
</p>

<div class="screenshot">
    <a href="${base_url}images/linuxtag/IMG_4187.JPG"
    rel="lightbox[meeting]" title="phpMyAdmin team with Rasmus (PHP) - Marc Delisle, Olivier Müller, Alexander M. Turek, Rasmus Lerdorf, Garvin Hicking, Michal Čihař, Robin Johnson">
        <img src="${base_url}images/linuxtag/IMG_4187_tn.JPG"
        alt="phpMyAdmin team with Rasmus (PHP)" />
    </a>
</div>

<div class="screenshot">
    <a href="${base_url}images/linuxtag/IMG_4189.JPG"
    rel="lightbox[meeting]" title="phpMyAdmin team with Monty (MySQL) - Michal Čihař, Marc Delisle, Olivier Müller, Garvin Hicking, Michael Widenius (Monty), Alexander M. Turek, Robin Johnson">
        <img src="${base_url}images/linuxtag/IMG_4189_tn.JPG"
        alt="phpMyAdmin team with Rasmus (PHP)" />
    </a>
</div>

<div class="clearer"></div>

<h2>Contributors</h2>

<p>
We'd like to thank all the former developers and contributors,
whom over the years have contributed to the success of phpMyAdmin.
A full list is maintained in the <a
href="http://www.phpmyadmin.net/documentation/#credits">documentation</a>.
</p>
    
</div>

<xi:include href="_page.tpl" />
</html>
