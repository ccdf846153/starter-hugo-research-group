function read() {
    var request = new XMLHttpRequest();
    // request.setHeader("Access-Control-Allow-Origin", "*");
    // request.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
    // request.setHeader("Access-Control-Allow-Headers", "Content-Type, X-Requested-With");
    request.open(
        'GET', 
        'https://gitee.com/ccdf846153/unic_resources/tree/master/content.html', 
        true
    );
    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            if (request.status === 200 || request.status === 0) {
                var content = request.responseText;
                console.log(content);
            }
        }
    };
    request.send(null);
}