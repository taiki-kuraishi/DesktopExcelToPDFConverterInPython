async function onClickSubmit() {
    const path = document.getElementById('text_input').value;
    await pywebview.api.printPath(path);
}
async function onClickChoseFile() {
    let res = await pywebview.api.choseFile();
    console.log(res);
    document.getElementById('text_input').value = res;
}