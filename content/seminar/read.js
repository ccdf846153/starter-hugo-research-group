function read() {
    var request = new XMLHttpRequest();
    request.open(
        'GET', 
        'https://gitee.com/ccdf846153/unic_resources/tree/master/content.txt', 
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