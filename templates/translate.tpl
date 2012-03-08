<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Translating phpMyAdmin</py:def>

<div py:match="content" id="body">

<h2>Translating phpMyAdmin</h2>

<p>
For localization, phpMyAdmin uses Gettext, you can find po files for each
translation in <code>po</code> directory in phpMyAdmin sources. You can
translate them using usual tools for handling Gettext translations or use our
<a href="https://l10n.cihar.com/projects/phpmyadmin/">translation server</a>.
</p>

<p>
The phpMyAdmin's documentation is being translated using po4a and gettext (see
<a href="${base_url}docs.${file_ext}">documentation</a> for existing
translations) and the process here is pretty much same as translating
phpMyAdmin itself.
</p>

<p>
It would be a good idea to subscribe to the <a
href="https://lists.sourceforge.net/lists/listinfo/phpmyadmin-translators">phpmyadmin-translators</a>
mailing list, because this is where we ask for translations of new messages.
</p>

<h3>Using translation server</h3>

<p>
Translation server includes various subprojects, you should always focus on
latest stable branch. Once this is complete you might want to continue
translating <code>master</code> and documentation. The changes are
automatically propagated, so you don't have to affraid you will have
to translate same strings several times.
</p>

<h3>Offline translating</h3>

<p>
As phpMyAdmin uses standard Gettext files, you can use your favorite editor to
edit them. There are various editors for translations which you can use for
offline translating.
</p>

<p>
You can download po files either directly from Git (see 
<a href="${base_url}devel.${file_ext}">developer instructions for more
details</a>) or use <a
href="https://l10n.cihar.com/projects/phpmyadmin/">translation server</a>,
which allows you to directly download latest po file for desired version.
</p>

<p>
To submit changes, you can either use <a
href="https://sourceforge.net/tracker/?group_id=23067&amp;atid=387645">translation
tracker on SourceForge.net</a> or <a
href="https://l10n.cihar.com/projects/phpmyadmin/">translation server</a>,
which can merge your changed po file back to existing sources.
</p>

<h3>More information</h3>

<p>
You can find more information on <a href="http://wiki.phpmyadmin.net/pma/Gettext_for_translators">our wiki</a>.
</p>

</div>

<xi:include href="_page.tpl" />
</html>


