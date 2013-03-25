<html xmlns:py="http://genshi.edgewall.org/" py:strip="">

<!--! Main menu bar -->
   <nav>
   <ul>
   <py:for each="item in menu">
     <li py:attrs="item['class']"><a href="${item.link}">${item.title}</a></li>
   </py:for>
   </ul>
   <div class="clearer"></div>
   </nav>
</html>
