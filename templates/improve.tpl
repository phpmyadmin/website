<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Contribute</py:def>

<div py:match="content" id="body">

<h2>Contribute to phpMyAdmin</h2>

<p>
As a free software project, phpMyAdmin is very open to your contributions. You don't
need developer skills to help, there are several non-coding ways to get involved
in a project (code is welcome too, of course!).
</p>

<h3>An invitation to students</h3>
<p>
To gain practical experience in open-source development, you are welcome to contribute to phpMyAdmin. Usually, this is volunteer work, but since 2008, our project has been part of <a href="http://code.google.com/soc">Google Summer of Code</a>. This program "offers post-secondary student developers ages 18 and older stipends to write code for various open source software projects". So, <a href="http://wiki.phpmyadmin.net/pma/Category:Google_Summer_of_Code">join us</a> soon and get ready for the next GSoC!
</p>

<h3>Helping users</h3>

<p>
Interested in helping other users to use phpMyAdmin? You can join any of the
<a href="${base_url}support.${file_ext}">support</a> options we provide and help users
there - IRC, mailing lists and web forums, where you can share your experience.
</p>

<h3 id="translate">Localization</h3>

<p>
phpMyAdmin is being translated to many languages, but maybe your language is not 
really up to date? You can easily contribute on our
<a href="https://l10n.cihar.com/engage/phpmyadmin/">translation server</a>.
You can find out more on the <a href="${base_url}translate.${file_ext}">translation
page</a>.
</p>

<h3>Testing and quality assurance</h3>

<p>
One important thing for us is to avoid problems in the user interface. You can really help
us here by providing feedback on releases and especially by testing the pre-releases
(alpha/beta/rc) we provide for testing. Just download them and <a href="https://sourceforge.net/p/phpmyadmin/bugs/">report any issues</a>
you face with them.
</p>

<h3>Documentation writer/tutorial creator</h3>

<p>
Do you 
feel our documentation misses some points? We welcome additions; just
let us know how you think the documentation can be improved. 
The best way is to <a href="http://wiki.phpmyadmin.net/pma/Pull_request">submit a pull request</a>
against our <a href="https://github.com/phpmyadmin/">GitHub repository</a>.
If you don't know how to make these changes, we still want to hear your input.
You can submit a <a href="https://sourceforge.net/p/phpmyadmin/feature-requests/">feature request</a>
explaining your suggested improvements.
</p>

<p>
Also documentation does not have to be text only, we would welcome to have some
video tutorials giving users hints how to do specific tasks inside phpMyAdmin.
</p>

<h3 id="devel">Developing</h3>

<p>
Coding contributions are very welcome, the easiest way is to fork our code on github 
and submit a pull request. We really welcome bug fixes or new features. 
You can find out more on the <a href="${base_url}devel.${file_ext}">developers
page</a>.
</p>

<h3>Bug/features screening/squashing</h3>

<p>
Our trackers, especially the
<a href="http://sourceforge.net/p/phpmyadmin/feature-requests/">feature tracker</a>,
contain dozens of entries which might already be implemented or don't make much sense after years.
You can go through reported issues, verify if they still apply to latest version and 
check whether they would be still useful. Also checking incoming reports for all required
information or whether they were already reported is welcome help.
</p>

<h3>Fund our project</h3>

<p>
We need money to allow our presence at conferences, buy new hardware or provide various
useful services to our users and developers. By <a href="${base_url}donate.${file_ext}">donating</a>
you help us in this area and possibly increase our presence at conferences.
</p>

</div>

<xi:include href="_page.tpl" />
</html>
