<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Download</py:def>
<py:def function="page_rss">${rss_files}</py:def>
<py:def function="page_rss_title">phpMyAdmin file releases</py:def>

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
    href="#distributions">further down on this page</a>. If you just want to
    try phpMyAdmin in virtual machine, you might want to check <a
    href="#appliances">available software appliances which provide
    phpMyAdmin</a>.
    </p>
    <p>
    If you do not have a package available or desire to install your own phpMyAdmin,
    you can download one of following
    source packages. Please note that phpMyAdmin requires at least PHP 5.2
    and MySQL 5.
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
    <xi:include href="_gitdl.tpl" />

    <p>
    Below are listed Git snapshots for trunk branch, more daily snapshots of the
    code are available on <a
    href="http://cihar.com/software/phpmyadmin/">external server</a>.
    </p>

    <table class="dllist">
    <thead>
        <tr>
            <th>File</th>
            <th>Size</th>
            <th>MD5 checksum</th>
        </tr>
    </thead>
    <tbody>
        <tr py:for="file in release_vcs">
            <td><a href="${file.url}#!md5!${file.md5}">${file.name}</a></td>
            <td class="size">${file.humansize}</td>
            <td>${file.md5}</td>
        </tr>
    </tbody>
    </table> 

    <p>
    More information about using Git is available on <a
    href="${base_url}devel.${file_ext}">development page</a>.
    </p>

    <h2>Older Releases</h2>
    <p>
    You can find older releases on <a
    href="https://sourceforge.net/projects/phpmyadmin/files/">SourceForge
    files page</a>. You can also get them 
    from our Git repository (check <a href="${base_url}devel.${file_ext}">developer information</a> for instructions).
    </p>

    <h2><a id="distributions"></a>Distributions</h2>
    <h3>Debian</h3>
    <p>
        Debian's package repositories include a phpMyAdmin package, but be
        aware that the configuration file is maintained in
        <code>/etc/phpmyadmin</code> and may differ in some ways from the
        official phpMyAdmin documentation. The package maintainer often visits
        the official IRC channel (#phpmyadmin on irc.freenode.net).
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
        href="https://launchpad.net/~nijel/+archive/phpmyadmin">PPA for Michal
        Čihař</a>.
    </p>
    <h3>Gentoo</h3>
    <p>
        Gentoo ships the phpMyAdmin package, both in a near stock configuration
        as well as in a <code>webapp-config</code> configuration.  <code>emerge
        dev-db/phpmyadmin</code> to install.
    </p>
    <h3>Mandriva</h3>
    <p>
        Mandriva ships the phpMyAdmin package in their <code>contrib</code> branch
        and can be installed via the usual Control Center. 
    </p>

    <h3>Fedora</h3>
    <p>
        Fedora ships the phpMyAdmin package, but be aware that the
        configuration file is maintained in <code>/etc/phpMyAdmin/</code> and
        may differ in some ways from the official phpMyAdmin documentation.
    </p>

    <h3>Red Hat Enterprise Linux</h3>
    <p>
        Red Hat Enterprise Linux itself and thus derivates like CentOS don't
        ship phpMyAdmin, but the Fedora-driven repository <a
        href="http://fedoraproject.org/wiki/EPEL">Extra Packages for Enterprise
        Linux</a> (EPEL) is doing so, if it's <a
        href="http://fedoraproject.org/wiki/EPEL/FAQ#howtouse">enabled</a>.
        But be aware that the configuration file is maintained in
        <code>/etc/phpMyAdmin/</code> and may differ in some ways from the
        official phpMyAdmin documentation.
    </p>

    <h3>Amahi Linux Home Server</h3>
    <p>
        phpMyAdmin is available as a one-click install on the <a href="http://www.amahi.org/apps">Amahi Home Server</a>. 
    </p>

    <h2><a id="appliances"></a>Appliances</h2>
    <p>
        <a href="http://en.wikipedia.org/wiki/Software_appliance">Software appliances</a>
        are more and more popular way of distributing software. They are
        distributed as an image, which can be directly used by system (be it
        ISO image for bootable CD or virtual disks for some type of
        virtualization).
    </p>
    <h3>Turnkey</h3>
    <p>
        <a href="http://www.turnkeylinux.org/appliances/lamp">LAMP
        Appliance</a> from TurnKey Linux includes all you need to run LAMP
        (Linux, Apache, MySQL, PHP/Python/Perl) together with phpMyAdmin to
        manage MySQL.
    </p>
    <h3>SUSE Studio</h3>
    <p>
        <a href="http://susestudio.com/">SUSE Studio</a> is an online service
        to build software appliances. Jordi Massaguer has built a <a
        href="http://jordimassaguerpla.blogspot.com/2009/02/phpmyadmin-appliance.html">phpMyAdmin
        appliance</a> using this service.
    </p>

</div>

<xi:include href="_page.tpl" />
</html>
