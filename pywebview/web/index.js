async function onClickSubmit() {
    const paths = document.getElementById('text_input').value;
    const status = await pywebview.api.submitPath(paths);
    if (status == 0) {
        // do nothing
    }
    else if(status == 1) {
        alert("File not found");
    }
    else{
        alert("Error");
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