<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Contribute</py:def>

<div py:match="content" id="body">

<h2>Contribute to phpMyAdmin</h2>

<p>
As a free software project, phpMyAdmin is very open to your contributions. You don't
need developer skills to help, there are several non-coding ways to get involved
in a project (code is welcome too, of course!).
</p>

<h3>Helping users</h3>

<p>
Interested in helping other users to use phpMyAdmin? You can join any of
<a href="${base_url}support.${file_ext}">support</a> we provide and help users 
there - IRC, mailing lists and web forums, where you can share your experience.
</p>

<h3 id="translate">Localization</h3>

<p>
phpMyAdmin is being translated to many languages, but maybe your language is not 
really up to date? You can easily contribute on our
<a href="https://l10n.cihar.com/projects/phpmyadmin/">translation server</a>.
You can find out more on <a href="${base_url}translate.${file_ext}">translation
page</a>.
</p>

<h3>Testing and quality assurance</h3>

<p>
One of important things is to avoid problems in user interface. You can really help
us here to provide feedback on releases and especially by testing pre-releases 
(alpha/beta/rc) we provide for testing. Just download them and <a href="http://sourceforge.net/tracker/?atid=377408&amp;group_id=23067">report any issues</a>
you face with them.
</p>

<h3>Documentation writer/tutorial creator</h3>

<p>
Do you 
feel our documentation misses some points? We welcome additions, just 
let us know how you think the documentation can be improved. You can 
open a <a href="http://sourceforge.net/tracker/?group_id=23067&amp;atid=377410">patch tracker</a> item with your suggestions. Should 
you know git, you can directly submit patches, but this is not necessary.
</p>

<p>
Also documentation does not have to be text only, we would welcome to have some
video tutorials giving users hints how to do specific tasks inside phpMyAdmin.
</p>

<h3 id="devel">Developing</h3>

<p>
Coding contributions are very welcome, the easiest way is to fork our code on github 
and submit a merge request. We really welcome bug fixes or new features. 
You can find out more on <a href="${base_url}devel.${file_ext}">developers
page</a>.
</p>

<h3>Bug/features screening/squashing</h3>

<p>
Our trackers, especially
<a href="https://sourceforge.net/tracker/?group_id=23067&amp;atid=377411&amp;status=1">feature tracker</a>
contain dozens of entries which might already implemented or don't make much sense after years.
You can go through reported issues, verify if they still apply to latest version and 
check whether they would be still useful. Also checking incoming reports for all required
information or whether they were already not reported is welcome help.
</p>

<h3>Fund our project</h3>

<p>
We need money to allow our presence on conferences, buy new hardware or provide various 
useful services to our users and developers. By <a href="${base_url}donate.${file_ext}">donating</a>
you help us in this area and possibly increase our presence on conferences.
</p>

</div>

<xi:include href="_page.tpl" />
</html>
