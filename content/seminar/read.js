async function read() {
    var fileInput = document.getElementById("content");
    const fileResult = await readFile("content.html");
    console.log(fileResult)
}