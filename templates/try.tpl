<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Try</py:def>

<div py:match="content" id="body">

<h2>Try</h2>


<h2>Screenshots</h2>

<div class="screenshot">
    <div class="screenshotimgborder">
    <div class="screenshotimg">
        <a href="${base_url}images/screenshots/main_page.png" target="pmadocs">
            <img src="${base_url}images/screenshots/main_page-small.png"
            alt="Main page screenshot" />
        </a>
    </div>
    </div>
</div>
</div>

<xi:include href="_page.tpl" />
</html>
