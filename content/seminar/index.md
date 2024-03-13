---
title: Seminar | UNIC Group
type: landing

sections:
  - block: markdown
    content:
      title: 组会分享
      subtitle: ''
      text: <div id="mask"><div>访问密码：</div><div><form><input type="text" id="submitText" name="pwdBox"><input type="button" value="确认" onclick="submitPwd();"></form></div></div><div id="content"></div><script type="text/javascript" src="./sha256.js"></script><script type="text/javascript" src="./read.js"></script><script type="text/javascript"> async function submitPwd() { if (SHA256(document.getElementById('submitText').value) == "ef271b641bd639249d33fad6401aa5f4ddad6c99bf0ae4ac8f40facae58dc9c0") { console.log("Welcome!"); document.getElementById('mask').remove(); var content = await read(); document.getElementById('content').innerHTML = content; var eContainerPublications = document.getElementById('container-publications'); var eTableContent = document.getElementById('table-content'); var eChildrenNum = eTableContent.children.length; eContainerPublications.style.height = eChildrenNum * (61.6) + 'px'; console.log(eChildrenNum); }}</script>

    design:
      columns: '1'

---
