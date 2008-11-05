<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Awards</py:def>

<div py:match="content" id="body">
    <div class="award" py:for="award in awards">
        <a href="${award.link}" class="awardlink"><img src="${base_url}images/awards/${award.image}" alt="${award.title}" /></a>
        ${Markup(award.text)}
        <p py:if="award.photo">Here is a 
            <a href="${base_url}images/awards/${award.photo}"
            rel="lightbox[awards]" title="${award.phototext}">
            photo</a> from the Awards ceremony.</p>
        <div class="clearer"></div>
    </div>
    <div class="clearer"></div>
</div>

<xi:include href="_page.tpl" />
</html>
