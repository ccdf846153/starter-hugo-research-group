function read() {
    var script = document.createElement('script');
    script.type = 'text/javascript';

    // 传参并指定回调执行函数为onBack
    script.src = 'https://gitee.com/ccdf846153/unic_resources/tree/master/content.html&callback=onBack';
    document.head.appendChild(script);

    // 回调执行函数
    function onBack(res) {
        console.log(JSON.stringify(res));
    }
}