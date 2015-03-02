<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" xmlns:gcse="uri:google-did-not-provide-a-real-ns" py:strip="">

<py:def function="page_rss">${rss_news}</py:def>
<py:def function="page_rss_title">phpMyAdmin project summary</py:def>

<py:def function="page_title">About</py:def>

<div py:match="content" id="body">

<h2>Search</h2>

<p>
This page uses Google Custom Search to give you best results related to
phpMyAdmin. You can also use it <a
href="http://www.google.com/coop/cse?cx=008688692096734274889:2un4bs4yxjm">directly
on Google</a>.
</p>

<script>
  (function() {
    var cx = '008688692096734274889:2un4bs4yxjm';
    var gcse = document.createElement('script');
    gcse.type = 'text/javascript';
    gcse.async = true;
    gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
        '//www.google.com/cse/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(gcse, s);
  })();
</script>
<gcse:search></gcse:search>
    
</div>

<xi:include href="_page.tpl" />
</html>
