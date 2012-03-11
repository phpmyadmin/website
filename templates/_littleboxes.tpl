<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
<!--! Little boxes with downloads and other quick links -->

<div class="rightbuttons">
<div class="rightbutton downloadbutton" py:for="release in releases_featured">
    <xi:include href="_dlbox.tpl" />
</div>

<div class="rightbutton downloadbutton" py:for="release in releases_beta">
    <xi:include href="_dlbox.tpl" />
</div>

<div class="rightbutton">
    <span class="dlname"><a href="${base_url}contest.${file_ext}" >Contest: win books!</a></span>
</div>

<div class="rightbutton">
    <span class="dlname"><a href="http://demo.phpmyadmin.net/trunk-config/" title="Go to demo server">Try phpMyAdmin</a></span>
</div>

<div class="rightbutton">
    <span class="dlname"><a href="${base_url}donate.${file_ext}" rel="payment">Donate to phpMyAdmin</a></span>
</div>

<div class="rightbutton">
<a href="#" title="In the eBook..." onclick="window.open('https://www.packtpub.com/sites/default/files/pmastarter/pmastarterpreview.html','help','scrollbars=yes,resizable=yes,width=680,height=720,left=180,top=20'); return false;">
    <img width="135" height="170" alt="eBook cover" src="${base_url}images/packt/pmastarter_cover.png" />
</a>
    <a href="https://www.e-junkie.com/ecom/gb.php?c=cart&amp;i=984362&amp;cl=174893&amp;ejc=2" target="ej_ejc" class="ec_ejc_thkbx" onclick="return EJEJC_lc(this)">
    <img src="${base_url}images/packt/addtocart.gif" width="132" height="60" alt="Add to Cart"/></a>
    <p style="font-size: smaller">A percentage of each sale goes direct to the phpMyAdmin project.</p>
</div>

</div>

</html>
