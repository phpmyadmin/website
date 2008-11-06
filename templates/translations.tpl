<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Translations</py:def>

<div py:match="content" id="body">
<h2>Translations</h2>

<p>
Translations inside phpMyAdmin are in different shape. The ones that have less
than 80% translated strings are shown in dark red, the ones bellow 50% in more
intensive red (those are considered  orphaned and the phpMyAdmin project would
appreciate any help in updating them).
</p>
<p>
If you want to help improving translation, please follow intructions in <a
href="http://wiki.cihar.com/pma/FAQ_7.2">FAQ 7.2</a> in documentation.
</p>


<table class="graph sortable" id="sorttable">
<thead>
<tr>
    <th class="forward_sort">Translation</th>
    <th>Strings</th>
    <th colspan="2">Translated strings percent</th>
    <th>Last modification</th>
</tr>
</thead>

<tbody>
<tr py:for="item in translations">
<td class="name">
<a href="http://wiki.cihar.com/pma/Language/${item.short}">${item.name}</a>
</td>
<td class="size">${item.translated}</td>
<td class="size">${item.percent}%</td>
<td class="bar${item.css}">
<div class="bar" style="width: ${round(float(item.percent))}%;"></div>
</td>
<td class="date">${item.updated}</td>
</tr>
</tbody>
</table>

</div>

<xi:include href="_page.tpl" />
</html>
