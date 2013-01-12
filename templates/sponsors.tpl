<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Sponsors</py:def>

<div py:match="content" id="body">

<h2>Sponsors</h2>

<p>
The phpMyAdmin project extends a special thanks to the companies who wish to support us in a recurring way.
</p>

<h3>Silver sponsors</h3>
<a href="http://www.navicat.com"><img src="${server}${base_url}images/navicat_200x68.jpg" alt="Navicat" /></a>
&nbsp;
<a href="http://www.scriptcase.net"><img src="${server}${base_url}images/scriptcase_200x68.png" alt="ScriptCase" /></a>

<h3>Bronze sponsors</h3>
<a href="http://www.aoemedia.de"><img src="${server}${base_url}images/aoemedia_200x68.jpg" alt="AOE media" /></a>
&nbsp;
<a href="http://www.cyberday-gmbh.de"><img src="${server}${base_url}images/cyberday_200x40.png" alt="AOE media" /></a>
<a href="http://phplinkdirectory.com"><img src="${server}${base_url}images/phplinkdirectory_267x48.png" alt="PHP Link Directory" /></a>

<h3>Sponsorship conditions and advantages</h3>

<ul>
 <li>A sponsor has to commit to a 100 USD minimum monthly amount (or 1000 USD yearly amount as a discount for paying in advance)</li>
 <li>The donation is made via Paypal (see the Subscribe form below)</li>
 <li>Sponsors are mentioned on this page, with the two highest sponsors (or 
the two sponsors who were there first, in case of a tie) listed on our <a href="http://phpmyadmin.net">home page</a> as well</li>
</ul>

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
