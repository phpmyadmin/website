<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Contest</py:def>

<div py:match="content" id="body">
<h2>Contest: win books and a yearly PacktLib subscription!</h2>
<p>
Packt Publishing (publisher of <a href="http://www.packtpub.com/mastering-phpmyadmin-3-4-for-effective-mysql-management/book">Mastering phpMyAdmin 3.4</a>) sponsors this programming contest, offering five e-books of your choice from their entire collection, plus a special prize of a yearly subscription to <a href="http://packtlib.packtpub.com">PacktLib</a>.
</p>
<h3>Rules</h3>
<ul>
 <li>For each item in the list of acceptable tickets below, the first person to submit<br /> a correct patch (refer to &ldquo;how to submit your patch&rdquo; below) wins an e-book</li>
 <li>The patch must be accepted by the phpMyAdmin team</li>
 <li>The phpMyAdmin team will pick one of the e-book winners at random<br /> to receive the special prize</li>
 <li>The names of all winners will appear on this page</li>
 <li>Members of the phpMyAdmin team are not eligible to the contest</li>
 <li>The contest runs from February 8 to March 8, 2014 at 23:59 UTC</li>
 <li>Maximum of one prize per person, except for the lucky one<br /> who gets also the special prize</li>
</ul>

<h3>Acceptable tickets</h3>
<ol>
<li><a href="https://sourceforge.net/p/phpmyadmin/bugs/4053">List of procedures is not displayed after executing with Enter</a></li>
<li><a href="https://sourceforge.net/p/phpmyadmin/bugs/4081">Setup page content shifted to the right edge of its tabs</a></li>
<li><a href="https://sourceforge.net/p/phpmyadmin/bugs/4271">Query by example and the second criteria line</a></li>
<li><a href="https://sourceforge.net/p/phpmyadmin/bugs/4272">Incorrect tabindex</a> (winner: Viduranga Wijesooriya)</li>
<li><a href="https://sourceforge.net/p/phpmyadmin/bugs/4276">Login loop on session expiry</a></li>
</ol>

<h3>How to submit your patch</h3>
<ul>
 <li>Be familiar with our <a href="${base_url}devel.${file_ext}">developers page</a></li>
 <li>In your git environment, ensure that you have configured your email address; therefore your commit will show your address and we'll be able to communicate with you; as an example, refer to <a href="http://wiki.phpmyadmin.net/pma/Git#Before_starting">our wiki</a></li>
 <li>Prepare your patch against the QA_4_1 branch</li>
 <li>Read our <a href="https://github.com/phpmyadmin/phpmyadmin/blob/master/DCO">DCO file</a> to ensure you accept our license and sign your commit (git -s)</li>
 <li>Submit it on <a href="http://github.com">github.com</a> as a pull request with a title such as &ldquo;Contest-X&rdquo;, where X is the number from the above list</li>
</ul>

<h3>Discount codes</h3>
<p>Anyone seeing this page can use one of the following discount codes (expire on March 31, 2014) to obtain a 25% discount for the entire Packt collection. Packt <a href="http://www.packtpub.com/article/open_source_receives_royalties_boost"> donates</a> a percentage from the sales of the phpMyAdmin-related books to the phpMyAdmin project.</p>
<ul>
 <li>Book : <strong>mRvKXazB</strong></li>
 <li>E-book: <strong>eB3Nu2yG</strong></li>
</ul>
<a href="http://link.packtpub.com/XJdqZr"><img src="${base_url}images/books/pma_en_3.4_150x185.png" alt="Book cover" width="150" height="185" style="border: 0px;" /></a>
</div>

<xi:include href="_page.tpl" />
</html>
