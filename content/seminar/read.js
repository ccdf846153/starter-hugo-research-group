async function read() {
    const fileResult = await waitReader("content.html");
    console.log(fileResult)
}

function waitReader(file) {
    return new Promise((resolve, reject) => {
        var reader = new FileReader();
        reader.onload = function (e) {
            resolve(e.target.result);
        };
        reader.readAsText(file);
    });
}