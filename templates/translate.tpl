<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Translating phpMyAdmin</py:def>

<div py:match="content" id="body">

<h2>Translating phpMyAdmin</h2>

<p>
For localization, phpMyAdmin uses Gettext, you can find po files for each
translation in <code>po</code> directory in phpMyAdmin sources. You can
translate them using usual tools for handling Gettext translations or use our
<a href="https://l10n.cihar.com/projects/phpmyadmin/">translation server</a>.
More information about translating can be found in
<a href="http://www.phpmyadmin.net/documentation/#faq7_2">FAQ 7.2</a>. The more
detailed documentation can be found on our <a href="http://wiki.phpmyadmin.net/pma/Translating">wiki</a>.
</p>

<p>
Documentation is being translated using po4a and gettext (see <a
href="${base_url}docs.${file_ext}">documentation</a> for existing
translations). To start, checkout <code><a
href="http://github.com/phpmyadmin/localized_docs/tree/master/po">localized_docs/po</a></code> from Git, or
just go to <a href="https://l10n.cihar.com/projects/pmadoc/">translation
server</a> and translate it online. If your language is missing, just contact
<a href="mailto:michal@cihar.com">Michal Čihař</a>, he will add it.  If you
prefer to translate directly the po files, please put updated ones into our <a
href="https://sourceforge.net/tracker/?group_id=23067&amp;atid=387645">translation
tracker</a>.
</p>

</div>

<xi:include href="_page.tpl" />
</html>


