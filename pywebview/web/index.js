async function onClickSubmit() {
    const path = document.getElementById('text_input').value;
    const status = await pywebview.api.convertToPDF(path);
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
    let res = await pywebview.api.choseFile();
    console.log(res);
    document.getElementById('text_input').value = res;
}