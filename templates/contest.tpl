<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">

<py:def function="page_title">Contest</py:def>

<div py:match="content" id="body">
<h2>Contest: win books!</h2>
<p>
Packt Publishing sponsors this programming contest, offering six copies of the <a href="http://www.packtpub.com/mastering-phpmyadmin-3-4-for-effective-mysql-management/book">Mastering phpMyAdmin 3.4</a> book (two print copies and four e-books).
</p>
<h3>Rules</h3>
<ul>
 <li>For each item in the list of acceptable tickets below, the first person to submit a correct patch (refer to &ldquo;how to submit your patch&rdquo; below) wins a book</li>
 <li>The patch must be accepted by the phpMyAdmin team</li>
 <li>Winners will get the choice of printed or e-book based on the time of their submission</li>
 <li>The winner's name for each ticket will appear on this page</li>
 <li>Members of the phpMyAdmin team are not eligible to the contest</li>
 <li>The contest runs from February 24 to March 24, 2013 at 23:59 UTC</li>
 <li>Maximum of one prize per person</li>
</ul>

<h3>Acceptable tickets</h3>
<ol>
 <li><a href="https://sourceforge.net/p/phpmyadmin/bugs/3813/">Grid editing UTF8 SET/ENUM value</a></li>
 <li><a href="https://sourceforge.net/p/phpmyadmin/bugs/3818/">After "Rename table ... to ..." left menu doesn't reflect changes</a> (winner: Ayush Chaudhary, ebook)</li>
 <li><a href="https://sourceforge.net/p/phpmyadmin/feature-requests/879/">Reserved word warning </a></li>
 <li><a href="https://sourceforge.net/p/phpmyadmin/feature-requests/1319/">Automatically create index when creating foreign key</a></li>
 <li><a href="https://sourceforge.net/p/phpmyadmin/feature-requests/1333/">Name foreign key constraints</a></li>
 <li><a href="http://sourceforge.net/p/phpmyadmin/feature-requests/1399/">No hard-coded icons in css files</a></li>
</ol>

<h3>How to submit your patch</h3>
<ul>
 <li>Be familiar with our <a href="${base_url}devel.${file_ext}">developers page</a></li>
 <li>Prepare your patch against the master branch</li>
 <li>Submit it on <a href="http://github.com">github.com</a> as a pull request with a title such as &ldquo;Contest-X&rdquo;, where X is the number from the above list</li>
 <li>In your git environment, ensure that you have configured your email address; therefore your commit will show your address and we'll be able to communicate with you; as an example, refer to <a href="http://wiki.phpmyadmin.net/pma/Git#Before_starting">our wiki</a></li>
</ul>

<h3>Discount codes</h3>
<p>Anyone seeing this page can use one of the following discount codes (valid until March 24, 2013) to obtain a 20% discount when ordering a <a href="http://www.packtpub.com/mastering-phpmyadmin-3-4-for-effective-mysql-management/book">Mastering phpMyAdmin 3.4</a> book copy.</p>
<ul>
 <li>Print : <strong>MREPHB</strong></li>
 <li>E-book: <strong>MREPHE</strong></li>
</ul>
<a href="http://link.packtpub.com/XJdqZr"><img src="${base_url}images/books/pma_en_3.4_150x185.png" alt="Book cover" width="150" height="185" style="border: 0px;" /></a>
</div>

<xi:include href="_page.tpl" />
</html>
