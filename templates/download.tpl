<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Download</py:def>
<py:def function="page_rss">${rss_files}</py:def>

<div py:match="content" id="body">
    <h2>Download</h2>
    <p>
    Many operating systems already include a phpMyAdmin package and some of
    them offer a way to upgrade to the latest version. Please contact your OS
    vendor for more information. Some informations are also available <a
    href="#distributions">bellow on this page</a>.
    </p>
    <p>
    If you do not have the possibility, you can download one of following
    source packages. Please note that 3.x versions require at least PHP 5.2
    and MySQL 5 to use them. If you are using older versions, please choose
    2.x brach, which is still supported by development team.
    </p>

    <py:for each="release in releases">
    <h2>${release.fullname}</h2>
    <xi:include href="_release.tpl" />
    </py:for>

    <h2>Development versions</h2>
    <xi:include href="_svndl.tpl" />
    <p>
    More information about using subversion is available on <a
    href="${base_url}improve.${file_ext}#devel">development page</a>.
    </p>

    <h2>Older releases</h2>
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
