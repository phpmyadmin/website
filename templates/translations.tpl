<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Translations</py:def>

<div py:match="content" id="body">
<h2>Translations</h2>

<table class="graph">
<tr>
    <th>Translation</th>
    <th>Strings</th>
    <th colspan="2">Translated strings percent</th>
    <th>Last modification</th>
</tr>

<tr py:for="item in translations">
<th class="name">
<a href="http://wiki.cihar.com/pma/Language/${item.short}">${item.name}</a>
</th>
<td class="size">
${item.translated}
</td>
<td class="size">
${item.percent}%
</td>
<td class="bar"><div style="width: ${round(float(item.percent))}%;"></div></td>
<td class="date">
${item.updated}
</td>
</tr>
</table>

</div>

<xi:include href="_page.tpl" />
</html>
