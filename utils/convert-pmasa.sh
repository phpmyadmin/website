#!/bin/sh

# This sed expression has been used to convert security announcements to new
# format (afterwards manual changes had to be done).

sed -ri '
    s@Date: *([0-9-]*)[^0-9-]*@<py:def function="announcement_date">\n\1\n</py:def>\n@;
    s@Updated: *([0-9-]*)<br />@<py:def function="announcement_updated">\n\1\n</py:def>\n@;
    s@Announcement-ID: *(PMASA-[0-9-]*)[^0-9-]*@<py:def function="announcement_id">\n\1\n</py:def>\n@;
    s@<b>Description</b>: *<br />@<py:def function="announcement_description">@;
    s@<b>Summary</b>: *<br />@<py:def function="announcement_summary">@;
    s@<b>Severity</b>: *<br />@<py:def function="announcement_severity">@;
    s@<b>Affected versions</b>: *<br />@<py:def function="announcement_affected">@;
    s@<b>Unaffected versions</b>: *<br />@<py:def function="announcement_unaffected">@;
    s@<b>Solution:?</b>:?<br />@<py:def function="announcement_solution">@;
    s@<b>References?:?</b>:?<br />@<py:def function="announcement_references">@;
    s@<b>Patches:?</b>:?<br />@<py:def function="announcement_patches">@;
    s@<b>Mitigation factor:?</b>:?<br />@<py:def function="announcement_mitigation">@;
    s@<p>@\n@;
    s@</p>@</py:def>@;
    /For further information and in case of questions, please contact the/D;
    /In case of questions, please contact /D;
    /phpMyAdmin team. Our website i/D;
    /phpMyAdmin security announceme/D;
    /<hr/D;
    $s@.*@<xi:include href="../_page.tpl" />\n</html>@;
    $s@.*@</html>@;
    1i \
<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
    ' PMASA-*

