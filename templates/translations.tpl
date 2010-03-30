<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Translations</py:def>

<div py:match="content" id="body">
<h2>Translations</h2>

<p>
Translations of phpMyAdmin are handled using Gettext. It is used for both
translating phpMyAdmin as well as the documentation (where Po4a is being
used).
</p>

<p>
You are welcome to contribute to any translations, you can follow instructions
on <a href="${base_url}improve.${file_ext}#translate">how to improve page</a>.
Or simply go to the <a href="https://l10n.cihar.com/">translation server</a>
and translate there projects <a
href="https://l10n.cihar.com/projects/phpmyadmin/">phpMyAdmin</a> or <a
href="https://l10n.cihar.com/projects/pmadoc/">phpMyAdmin documentation</a>.
The translation server also provides you overview of translation status.
</p>

<table class="graph sortable" id="sorttable">
<thead>
<tr>
    <th class="forward_sort">Translation</th>
    <th>Strings</th>
    <th colspan="2">Translated strings percent</th>
    <th>Last modification</th>
    <th>Translators</th>
</tr>
</thead>

<tbody>
<tr py:for="item in translations">
<td class="name">
<a href="http://wiki.phpmyadmin.net/pma/Language/${item.short}">${item.name}</a>
</td>
<td class="size">${item.translated}</td>
<td class="size">${item.percent}%</td>
<td class="bar${item.css}">
<div class="bar" style="width: ${round(float(item.percent))}%;"></div>
</td>
<td class="date">${item.updated}</td>
<td>${item.translator}</td>
</tr>
</tbody>
</table>

</div>

<xi:include href="_page.tpl" />
</html>
