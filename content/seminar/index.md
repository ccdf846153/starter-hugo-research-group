---
title: Seminar | UNIC Group
type: landing

sections:
  - block: markdown
    content:
      title: 组会分享
      subtitle: ''
      text: <style>@import url(./style.css)</style><div id="mask"><div id="mask-container"><form id="form-container"><div id="password-div"><label id="password-label"><span>密码</span><input type="password" id="pwdBox" name="pwdBox" class="filter-search form-control form-control-sm"></label><input type="button" id="pwd-confirm" value="确认" onclick="submitPwd();"></div><br/><input type="checkbox" id="showPassword"></form></div></div><div id="content"></div><script type="text/javascript" src="./sha256.js"></script><script type="text/javascript" src="./read.js"></script><script type="text/javascript"> window.onload = function() { document.getElementById('pwdBox').style.width = "calc(100%-4rem)"; }; async function submitPwd() { if (SHA256(document.getElementById('pwdBox').value.toUpperCase()) == "ef271b641bd639249d33fad6401aa5f4ddad6c99bf0ae4ac8f40facae58dc9c0") { console.log("Welcome!"); document.getElementById('mask').remove(); var content = await read(); document.getElementById('content').innerHTML = content; var eContainerPublications = document.getElementById('container-publications'); var eItemTableContent = document.getElementById('item-table-content'); var eChildrenNum = eItemTableContent.rows.length; eContainerPublications.style.height = ((eChildrenNum - 1) * 42.59 + 38.19 + 100) + 'px'; console.log(eChildrenNum); } }</script>

    design:
      columns: '1'

---
