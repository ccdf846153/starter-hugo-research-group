async function read() {
    try {
        var response = await fetch('https://unicxidian.netlify.app/seminar_list/content.txt');
        var fileContent = await response.text();

        if (fileContent == undefined) {
            response = await fetch('https://unicxidian.org/seminar_list/content.txt');
            fileContent = await response.text();
        }

        const parser = new DOMParser();
        const doc = parser.parseFromString(fileContent, 'text/html');
        return doc.body.innerHTML;
    } catch (error) {
        console.error(error);
    }
}