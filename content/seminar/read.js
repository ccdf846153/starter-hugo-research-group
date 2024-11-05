async function read() {
    try {
        let response = await fetch('https://unicxidian.netlify.app/seminar_list/content.txt');
        let fileContent = await response.text();

        const parser = new DOMParser();
        const doc = parser.parseFromString(fileContent, 'text/html');
        return doc.body.innerHTML;
    } catch (error) {
        console.error(error);
    }
}