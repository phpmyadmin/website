<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Sponsors</py:def>

<div py:match="content" id="body">

<h2>Sponsors</h2>

<p>
The phpMyAdmin project extends a special thanks to the companies who wish to support us in a recurring way.
</p>

<h3>Gold sponsor</h3>
<a href="https://www.certs4less.com"><img src="${server}${base_url}images/certs4less_240x65.jpg" alt="Certs4Less" /></a>

<h3>Silver sponsors</h3>
<a href="http://www.navicat.com"><img src="${server}${base_url}images/navicat_200x68.jpg" alt="Navicat" /></a>
&nbsp;
<a href="http://www.scriptcase.net"><img src="${server}${base_url}images/scriptcase_200x68.png" alt="ScriptCase" /></a>

<h3>Bronze sponsors</h3>
<a href="http://www.aoemedia.de"><img src="${server}${base_url}images/aoemedia_200x68.jpg" alt="AOE media" /></a>
&nbsp;
<a href="http://www.cyberday-gmbh.de"><img src="${server}${base_url}images/cyberday_200x40.png" alt="AOE media" /></a>
<a href="http://phplinkdirectory.com"><img src="${server}${base_url}images/phplinkdirectory_267x48.png" alt="PHP Link Directory" /></a>
<a href="http://vds64.com"><img src="${server}${base_url}images/vds64_200x68.png" alt="VDS64" /></a>

<h3>Sponsorship conditions and advantages</h3>

<ul>
 <li>A sponsor has to commit to a monthly or yearly amount depending on sponsorship level</li>
 <li>The donation is made via Paypal (see the Subscribe form below)</li>
 <li>Sponsors logo with link is placed on this page</li>
 <li>Silver and higher sponsors are on our <a href="http://phpmyadmin.net">home page</a> as well in order of levels</li>
 <li>Logo size is limited depending on sponsorship level</li>
 <li>Number of sponsors for levels higher than brozne is limited</li>
 <li>We reserve right to change sponsorship levels in future</li>
</ul>

<p>Sponsorship levels in overview:</p>

<table class="nice">
<thead>
<tr><th>Level</th><th>Possible sponsors</th><th>Monthly amount</th><th>Yearly amount</th><th>Additional logo placement</th><th>Logo size</th></tr>
</thead>
<tbody>
<tr><td class="name">Platinum</td><td class="size">1</td><td class="size">$1,000</td><td class="size">$10,000</td><td>Top section on home page</td><td>250x250</td></tr>
<tr><td class="name">Gold</td><td class="size">2</td><td class="size">$500</td><td class="size">$5,000</td><td>Second section on home page</td><td>250x130</td></tr>
<tr><td class="name">Silver</td><td class="size">4</td><td class="size">$250</td><td class="size">$2,500</td><td>Third section on home page</td><td>250x70</td></tr>
<tr><td class="name">Bronze</td><td class="size">unlimited</td><td class="size">$100</td><td class="size">$1,000</td><td>None</td><td>250x70</td></tr>
</tbody>
</table>

<h3>New sponsors</h3>

<p>
If you use phpMyAdmin or offer it to your customers, please consider 
sponsoring the project with a monthly donation. The money will be used to 
improve phpMyAdmin, bring phpMyAdmin developers to conferences and to cover 
costs for services required to run the project.
</p>

<p>
To get listed on this page, please contact us at 
<a href="mailto:donate@phpmyadmin.net?subject=Sponsorship">donate@phpmyadmin.net</a> after
subscribing here. Please note that we might refuse to link to some sites which
we consider unethical or inappropriate.
</p>

<p>
Thank you for your support!
</p>

<div class="subscribe">

<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_s-xclick" />
<input type="hidden" name="hosted_button_id" value="QXKQ4SM8MDTL4" />
<p><input type="hidden" name="on0" value="Sponsorship level" />Sponsorship options</p>
<p>
<select name="os0">
	<option value="Bronze">Bronze: $100 USD - monthly</option>
	<option value="Silver">Silver: $250 USD - monthly</option>
	<option value="Gold">Gold: $500 USD - monthly</option>
	<option value="Platinum">Platinum: $1,000 USD - monthly</option>
	<option value="Bronze (year)">Bronze (year): $1,000 USD - yearly</option>
	<option value="Silver (year)">Silver (year): $2,500 USD - yearly</option>
	<option value="Gold (year)">Gold (year): $5,000 USD - yearly</option>
	<option value="Platinum (year)">Platinum (year): $10,000 USD - yearly</option>
</select>
</p>
<p>
<input type="hidden" name="currency_code" value="USD" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_subscribe_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!" />
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</p>
</form>

</div>


<h2>Technology partners</h2>

<p>
The phpMyAdmin project is grateful to <a href="http://sourceforge.net/projects/phpmyadmin">SourceForge</a> and <a href="https://github.com/phpmyadmin">GitHub</a> for their services.</p>

</div>

<xi:include href="_page.tpl" />
</html>
