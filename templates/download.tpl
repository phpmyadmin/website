<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Download</py:def>
<py:def function="page_rss">${rss_files}</py:def>

<div py:match="content" id="body">
    <h2>Download</h2>
    <p>
    Many operating systems already include a phpMyAdmin package and will
    automatically keep it updated, however these versions are sometimes
    slightly outdated and therefore may be missing the latest features.
    Additionally, the configuration process varies widely by package and
    may not adhere to the official phpMyAdmin documentation. That being said,
    it is usually the quickest way to an updated installation. Please contact your OS
    vendor for more information. Some additional information is also available <a
    href="#distributions">further down on this page</a>.
    </p>
    <p>
    If you do not have a package available or desire to install your own phpMyAdmin,
    you can download one of following
    source packages. Please note that 3.x versions require at least PHP 5.2
    and MySQL 5 to use them. If you are using older versions, please choose
    the 2.x branch, which is still supported for security fixes.
    </p>

    <py:for each="release in releases">
    <h2>${release.fullname}</h2>
    <xi:include href="_release.tpl" />
    </py:for>

    <py:for each="release in releases_beta">
    <h2>Testing: ${release.fullname}</h2>
    <xi:include href="_release.tpl" />
    </py:for>

    <h2>Development Versions</h2>
    <xi:include href="_svndl.tpl" />
    <p>
    More information about using subversion is available on <a
    href="${base_url}improve.${file_ext}#devel">development page</a>.
    </p>

    <h2>Older Releases</h2>
    <p>
    You can find older releases on <a
    href="https://sourceforge.net/project/showfiles.php?group_id=23067">SourceForge
    files page</a>. 
    </p>
    <py:for each="release in releases_older">
    <h3>${release.fullname}</h3>
    <xi:include href="_release.tpl" />
    </py:for>

    <h2><a name="distributions"></a>Distributions</h2>
    <h3>Debian</h3>
    <p>
        Debian's package repositories include a phpMyAdmin package, but be aware
        that the configuration file is maintained in /etc/phpmyadmin and may
        differ in some ways from the official phpMyAdmin documentation. The
	package maintainer often visits the official IRC channel (#phpmyadmin on
	irc.freenode.net).
    </p>
    <h3>OpenSUSE</h3>
    <p>
        OpenSUSE already comes with phpMyAdmin package, however if you want to
        use recent version, you can use packages from <a
        href="http://software.opensuse.org/search?q=phpmyadmin">openSUSE Build
        Service</a>.
    </p>
    <h3>Ubuntu</h3>
    <p>
        Ubuntu ships phpMyAdmin package, however if you want to use recent
        version, you can use packages from <a
        href="https://launchpad.net/~nijel/+archive/">PPA for Michal
        Čihař</a>.
    </p>


</div>

<xi:include href="_page.tpl" />
</html>
