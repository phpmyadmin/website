<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE rdf:RDF
[
<!ENTITY % HTMLlat1 PUBLIC
 "-//W3C//ENTITIES Latin 1 for XHTML//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml-lat1.ent">
]>
<rdf:RDF xmlns="http://purl.org/rss/1.0/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:admin="http://webns.net/mvcb/" xmlns:py="http://genshi.edgewall.org/">
<channel rdf:about="http://www.phpmyadmin.net/security/">
<title>phpMyAdmin security announcements</title>
<link>http://www.phpmyadmin.net/security/</link>
<description>phpMyAdmin security announcements</description>
<dc:language>en-us</dc:language>
<dc:creator>phpMyAdmin devel team</dc:creator>
<dc:date>${generated.w3cdtf()}</dc:date>
<admin:generatorAgent rdf:resource="${server}" />
<items>
<rdf:Seq>
    <rdf:li py:for="issue in topissues" rdf:resource="${issue.fulllink}" />
</rdf:Seq>
</items>
</channel>

<item  py:for="issue in topissues" rdf:about="${issue.fulllink}">
<link>${issue.fulllink}</link>
<title>${issue.name}</title>
<dc:date>${issue.date.w3cdtf()}</dc:date>
<dc:creator>phpMyAdmin devel team</dc:creator>
<dc:subject>phpMyAdmin security</dc:subject>
<description>
<![CDATA[
<p>${issue.summary}</p>

<p><a href="http://cve.mitre.org/cgi-bin/cvename.cgi?name=${issue.cve}">${issue.cve}</a></p>
]]>
</description>
</item>

</rdf:RDF>
