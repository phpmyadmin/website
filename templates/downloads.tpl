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
    href="http://docs.phpmyadmin.net/en/latest/setup.html">in our documentation</a>. If you just want to
    try phpMyAdmin in virtual machine, you might want to check the <a
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
    Below are listed Git snapshots for master branch, more daily snapshots of the
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

    <h2><a id="distributions"></a>Installing phpMyAdmin</h2>

    <p>
        The full process of installing phpMyAdmin is described in our <a
        href="http://docs.phpmyadmin.net/en/latest/setup.html">manual</a>.  You
        can find there also information how to install phpMyAdmin on your Linux
        distribution.
    </p>

    <h2><a id="appliances"></a>Appliances</h2>
    <p>
        <a href="http://en.wikipedia.org/wiki/Software_appliance">Software appliances</a>
        are becoming a popular way of distributing software. They are
        distributed as an image, which can be directly used by system (be it
        ISO image for bootable CD or virtual disks for some type of
        virtualization).
    </p>
    <p>
        There are quite many appliances which provide phpMyAdmin as a
        management tool for MySQL. It usually comes as part of LAMP stack
        but there might be other offerings as well. Please check your 
        favorite appliance provider, ISV or app store for it. Some of the
        appliaces are <a href="https://wiki.phpmyadmin.net/pma/Third_party_installers">
        listed on our wiki</a>.
    </p>
</div>

<xi:include href="_page.tpl" />
</html>
