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