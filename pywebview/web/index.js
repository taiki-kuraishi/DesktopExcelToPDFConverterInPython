let path_array = [];

async function onClickSubmit() {
    const paths = document.getElementById('text_input').value;
    const path_array = await pywebview.api.submitPath(paths);
    console.log(path_array)
    if (path_array[0] == 1) {
        alert("File not found");
    }
    else {
        console.log(path_array);
        //pathの個数を表示
        const p = document.getElementById("path_length");
        p.textContent = path_array.length;

        // pathをリストで表示
        const ul = document.getElementById("file_list");
        for (let i = 0; i < path_array.length; i++) {
            const li = document.createElement("li");
            li.textContent = path_array[i];
            ul.appendChild(li);
        }
    }
}
async function onClickChoseFile() {
    let res = await pywebview.api.showFileDialog();
    document.getElementById('text_input').value = res;
}
async function onClickChoseFolder() {
    let res = await pywebview.api.showFolderDialog();
    document.getElementById('text_input').value = res;
}