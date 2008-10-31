<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<div id="left">
<ul py:for="item in issues">
    <li><a href="${item.link}">${item.name}</a></li>
</ul>
</div>

</html>
