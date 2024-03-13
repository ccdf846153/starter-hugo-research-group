---
title: Seminar | UNIC Group
type: landing

sections:
  - block: markdown
    content:
      title: 组会分享
      subtitle: ''
<<<<<<< HEAD
      text: <div id="mask"><div><form><label for="password" style="margin-right: 1rem;">密码</label><input type="password" id="password" name="password" class="filter-search form-control form-control-sm" style="width: 20%; min-width: 15rem;"><input type="button" value="确认" onclick="submitPwd();" style="border: none; font-size: 8pt;"><br/><input type="checkbox" id="showPassword" onclick="togglePasswordVisibility();"><label for="showPassword">显示密码</label></form></div></div><div id="content"></div><script type="text/javascript" src="./sha256.js"></script><script type="text/javascript" src="./read.js"></script><script type="text/javascript"> function togglePasswordVisibility() { var passwordInput = document.getElementById("password"); var showPasswordInput = document.getElementById("showPassword"); if (showPasswordInput.checked) { passwordInput.type = "text"; } else { passwordInput.type = "password"; } } async function submitPwd() { if (SHA256(document.getElementById('password').value.toUpperCase()) == "ef271b641bd639249d33fad6401aa5f4ddad6c99bf0ae4ac8f40facae58dc9c0") { console.log("Welcome!"); document.getElementById('mask').remove(); var content = await read(); document.getElementById('content').innerHTML = content; var eContainerPublications = document.getElementById('container-publications'); var eItemTableContent = document.getElementById('item-table-content'); var eChildrenNum = eItemTableContent.rows.length; eContainerPublications.style.height = ((eChildrenNum - 1) * 42.59 + 38.19 + 100) + 'px'; console.log(eChildrenNum); } }</script>
=======
      text: <div id="mask"><div>访问密码：</div><div><form><input type="text" id="submitText" name="pwdBox"><input type="button" value="确认" onclick="submitPwd();"></form></div></div><div id="content"></div><script type="text/javascript" src="./sha256.js"></script><script type="text/javascript" src="./read.js"></script><script type="text/javascript"> async function submitPwd() { if (SHA256(document.getElementById('submitText').value.toUpperCase()) == "ef271b641bd639249d33fad6401aa5f4ddad6c99bf0ae4ac8f40facae58dc9c0") { console.log("Welcome!"); document.getElementById('mask').remove(); var content = await read(); document.getElementById('content').innerHTML = content; var eContainerPublications = document.getElementById('container-publications'); var eItemTableContent = document.getElementById('item-table-content'); var eChildrenNum = eItemTableContent.rows.length; eContainerPublications.style.height = ((eChildrenNum - 1) * 42.59 + 38.19 + 100) + 'px'; console.log(eChildrenNum); }}</script>
>>>>>>> parent of a29c65d (asd)

    design:
      columns: '1'

---
