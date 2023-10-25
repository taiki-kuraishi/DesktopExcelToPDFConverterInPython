async function onClickSubmit() {
    const paths = document.getElementById('text_input').value;
    const status = await pywebview.api.main(paths);
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
    // console.log(typeof res)
    // console.log(res[0]);
    // console.log(res.length)
    document.getElementById('text_input').value = res;
}