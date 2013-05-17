<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Awards</py:def>

<div py:match="content" id="body">
    <div class="award" py:for="award in awards">
        <a href="${award.link}" class="awardlink"><img src="${base_url}images/awards/${award.image}" alt="${award.title}" /></a>
        ${Markup(award.text)}
        <p py:if="award.photos">Photos:
        <span py:for="photo in award.photos">
        <a href="${base_url}images/awards/${photo[0]}" rel="lightbox[awards]" title="${photo[2]}">${photo[1]}</a>
        </span>
        </p>
        <div class="clearer"></div>
    </div>
    <div class="clearer"></div>
</div>

<xi:include href="_page.tpl" />
</html>
