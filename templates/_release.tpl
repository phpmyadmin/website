<html xmlns:py="http://genshi.edgewall.org/" xmlns:xi="http://www.w3.org/2001/XInclude" py:strip="">
        <p>Released ${release.date}, see <a href="${release.notes}">release notes</a> for details.</p>
        <p>${release.info}</p>
	<table class="dllist">
	  <tr>
	  <th>File</th>
	  <th>Size</th>
	  <th>MD5 checksum</th>
	  <th>Downloads</th>
          </tr>
            <py:for each="file in release.files">
	      <tr>
	       <td><a href="${file.url}#!md5!${file.md5}">${file.name}</a></td>
	       <td>${file.humansize}</td>
	       <td>${file.md5}</td>
	       <td align="right">${file.dlcount}</td>
	      </tr>
            </py:for>
        </table> 
</html>
