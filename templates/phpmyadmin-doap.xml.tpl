<?xml version="1.0" encoding="UTF-8" ?>
<Project rdf:about="#Project" xmlns="http://usefulinc.com/ns/doap#" xmlns:foaf="http://xmlns.com/foaf/0.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:py="http://genshi.edgewall.org/">
  <name>Wammu</name>
  <shortdesc xml:lang="en">Administration of MySQL over the Web.</shortdesc>
  <description xml:lang="en">phpMyAdmin is a free software tool written in PHP intended to handle the administration of MySQL over the World Wide Web. phpMyAdmin supports a wide range of operations with MySQL. The most frequently used operations are supported by the user interface (managing databases, tables, fields, relations, indexes, users, permissions, etc), while you still have the ability to directly execute any SQL statement. To ease usage to a wide range of people, phpMyAdmin is translated into 55 languages and supports both LTR and RTL languages.</description>
  <bug-database rdf:resource="https://sourceforge.net/p/phpmyadmin/bugs/" />
  <programming-language>PHP</programming-language>
  <download-page rdf:resource="http://www.phpmyadmin.net/home_page/downloads.php" />
  <homepage rdf:resource="http://www.phpmyadmin.net/" />
  <license rdf:resource="http://usefulinc.com/doap/licenses/gpl" />
  <wiki rdf:resource="http://wiki.phpmyadmin.net/" />
  <screenshots rdf:resource="http://www.phpmyadmin.net/home_page/try.php" />
  <old-homepage rdf:resource="http://phpmyadmin.sourceforge.net/" />
  <old-homepage rdf:resource="http://phpmyadmin.sf.net/" />
  <category rdf:resource="http://freshmeat.net/browse/253/"/>
  <category rdf:resource="http://freshmeat.net/browse/68/"/>
  <maintainer>
    <foaf:Person>
      <foaf:name>Marc Delisle</foaf:name>
      <foaf:mbox_sha1sum>0350baf1c3a9a0e31ee5c010f7b69021bec24e85</foaf:mbox_sha1sum>
    </foaf:Person>
  </maintainer>
  <developer>
    <foaf:Person>
      <foaf:name>Michal Čihař</foaf:name>
      <foaf:homepage rdf:resource="http://cihar.com/" />
      <foaf:mbox rdf:resource="mailto:michal@cihar.com" />
      <foaf:mbox_sha1sum>6dd3e0747f1392564764e15a7dde1e27d4b978d0</foaf:mbox_sha1sum>
    </foaf:Person>
  </developer>
<repository>
    <GitRepository>
      <location rdf:resource="git://github.com/phpmyadmin/phpmyadmin.git" />
      <browse rdf:resource="http://github.com/phpmyadmin/" />
    </GitRepository>
  </repository>
<py:for each="release in releases_featured">
<release py:for="file in release.files">
    <Version>
      <name>${file.name}</name>
      <created>${release.date}</created>
      <revision>${release.version}</revision>
      <file-release rdf:resource="${file.url}" />
    </Version>
  </release>
  </py:for>
</Project>

