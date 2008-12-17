<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Security - ${announcement_id()}</py:def>
<py:def function="page_rss">${base_url}security/index.xml</py:def>
<py:def function="page_rss_title">phpMyAdmin security issues</py:def>

<div py:match="content">

<xi:include href="_list.tpl" />

<div id="body">
    <h2>${announcement_id()}</h2>

    <p><strong>Announcement-ID:</strong> ${announcement_id()}</p>
    <p><strong>Date:</strong> ${announcement_date()}</p>
    <p py:if="defined('announcement_updated')"><strong>Updated:</strong> ${announcement_updated()}</p>

    <h3>Summary</h3>
    <p>${announcement_summary()}</p>

    <h3>Description</h3>
    <p py:if="defined('announcement_description')">${announcement_description()}</p>
    <py:if test="defined('announcement_description_fmt')">${announcement_description_fmt()}</py:if>

    <h3>Severity</h3>
    <p>${announcement_severity()}</p>

    <py:if test="defined('announcement_mitigiation')">
    <h3>Mitigation factor</h3>
    <p>${announcement_mitigiation()}</p>
    </py:if>

    <h3>Affected Versions</h3>
    <p>${announcement_affected()}</p>

    <py:if test="defined('announcement_unaffected')">
    <h3>Unaffected Versions</h3>
    <p>${announcement_unaffected()}</p>
    </py:if>

    <h3>Solution</h3>
    <p>${announcement_solution()}</p>

    <py:if test="defined('announcement_references') or defined('announcement_cve')">
    <h3>References</h3>
    <p py:if="defined('announcement_references')">${announcement_references()}</p>
    <p py:if="defined('announcement_cve')"><a href="http://web.nvd.nist.gov/view/vuln/detail?vulnId=${announcement_cve()}">${announcement_cve()}</a></p>
    </py:if>

    <py:if test="defined('announcement_patches')">
    <h3>Patches</h3>
    <p>${announcement_patches()}</p>
    </py:if>

    <p>
    For further information and in case of questions, please contact the
    phpMyAdmin team. Our website is <a href="http://www.phpmyadmin.net/">
    http://www.phpmyadmin.net</a>.
    </p>

</div>
<div class="clearer"></div>
</div>

<xi:include href="../_page.tpl" />
</html>
