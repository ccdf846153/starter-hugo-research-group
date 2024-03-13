function read() {
    var request = new XMLHttpRequest();
    const parser = new DOMParser();

    request.open(
        'GET', 
        'https://www.unicxidian.org/seminar_list/content.html', 
        true
    );
    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            if (request.status === 200 || request.status === 0) {
                var content = request.responseText;
                const doc = parser.parseFromString(content, 'text/html');
                return doc.body.innerHTML;
            }
        }
    };
    request.send(null);
}