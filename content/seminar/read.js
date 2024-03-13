async function read() {
    const str = await readFile();
    console.log(str);
}

function readFile() {
    var fso = new ActiveXObject("Scripting.FileSystemObject");
    if (fso.FileExists("./content.html")) {
        var file = fso.OpenTextFile("C./content.html", 1);
        var str = f.ReadAll();
        f.Close();
        return str;
    }
}