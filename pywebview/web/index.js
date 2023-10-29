let path_array = [];

function addListItem(full_path, file_name) {
    // ul要素を取得
    var ul = document.getElementById("path-list-ol");

    // 新しいli要素を作成
    var li = document.createElement("li");
    li.setAttribute("id", "path-list-li");
    li.setAttribute("class", "list-group-item d-flex justify-content-between align-items-start");

    // 新しいdiv要素を作成
    var div = document.createElement("div");
    div.setAttribute("id", "full-path");
    div.setAttribute("class", "ms-2 me-auto");

    // 新しいdiv要素の子要素として、新しいdiv要素を作成
    var fileNameDiv = document.createElement("div");
    fileNameDiv.setAttribute("id", "file-name");
    fileNameDiv.setAttribute("class", "fw-bold");
    fileNameDiv.appendChild(document.createTextNode(file_name));
    div.appendChild(fileNameDiv);

    // 新しいdiv要素の子要素として、新しいテキストノードを作成
    var content = document.createTextNode(full_path);
    div.appendChild(content);

    // li要素の子要素として、新しいdiv要素を追加
    li.appendChild(div);

    // li要素の子要素として、新しいspan要素を追加
    // var span = document.createElement("span");
    // span.setAttribute("class", "badge bg-primary rounded-pill");
    // span.appendChild(document.createTextNode("14"));
    // li.appendChild(span);

    // ul要素の子要素として、新しいli要素を追加
    ul.appendChild(li);
}

//windowが読み込まれたら
//start-menuのみ表示
window.addEventListener('DOMContentLoaded', () => {
    onClickShowOnlyStartMenu();
});

//start-menuのみ表示
function onClickShowOnlyStartMenu() {
    document.getElementById('start-menu').style.display = 'block';
    document.getElementById('select-path').style.display = 'none';
    document.getElementById('show-path-list').style.display = 'none';
    document.getElementById('save-file').style.display = 'none';
    document.getElementById('convert').style.display = 'none';
}

//select-pathのみ表示
function onClickShowOnlySelectPathMenu() {
    document.getElementById('start-menu').style.display = 'none';
    document.getElementById('select-path').style.display = 'block';
    document.getElementById('show-path-list').style.display = 'none';
    document.getElementById('save-file').style.display = 'none';
    document.getElementById('convert').style.display = 'none';

    //select-path-nextにdispatchEvent changeを発火させる
    input = document.getElementById('path-input');
    var event = new Event("change");
    input.dispatchEvent(event);
}

//show-path-listのみ表示
function onClickShowOnlyShowPathListMenu() {
    document.getElementById('start-menu').style.display = 'none';
    document.getElementById('select-path').style.display = 'none';
    document.getElementById('show-path-list').style.display = 'block';
    document.getElementById('save-file').style.display = 'none';
    document.getElementById('convert').style.display = 'none';
}

//save-fileのみ表示
function onClickShowOnlySaveFileMenu() {
    document.getElementById('start-menu').style.display = 'none';
    document.getElementById('select-path').style.display = 'none';
    document.getElementById('show-path-list').style.display = 'none';
    document.getElementById('save-file').style.display = 'block';
    document.getElementById('convert').style.display = 'none';

    //path-outputにdispatchEvent changeを発火させる
    input = document.getElementById('path-output');
    var event = new Event("change");
    input.dispatchEvent(event);
}

//convertのみ表示
function onClickShowOnlyConvertMenu() {
    document.getElementById('start-menu').style.display = 'none';
    document.getElementById('select-path').style.display = 'none';
    document.getElementById('show-path-list').style.display = 'none';
    document.getElementById('save-file').style.display = 'none';
    document.getElementById('convert').style.display = 'block';
}

//miIdのinputが空ならtargetIdのbuttonをdisabledにする
function onChangeInput(myId, targetId) {
    const path = document.getElementById(myId).value;
    if (path == "") {
        document.getElementById(targetId).disabled = true;
    }
    else {
        document.getElementById(targetId).disabled = false;
    }
}

async function onClickPathSubmit() {
    const paths = document.getElementById('path-input').value;
    const path_array = await pywebview.api.submitPath(paths);
    console.log(path_array)
    if (path_array[0] == 1) {
        alert("File not found");
    }
    else {
        //show-path-listのみ表示
        onClickShowOnlyShowPathListMenu();

        //pathの個数を表示
        const p = document.getElementById("path_length");
        p.textContent = "fileの個数は : " + path_array.length;

        //ol path-list-olの中身を削除
        const ol = document.getElementById("path-list-ol");
        while (ol.firstChild) {
            ol.removeChild(ol.firstChild);
        }

        // pathをリストで表示
        for (let i = 0; i < path_array.length; i++) {
            addListItem(path_array[i], path_array[i].split('/').pop())
        }
    }
}
async function onClickChoseFile() {
    let res = await pywebview.api.showFileDialog();
    input = document.getElementById('path-input');
    input.value = res;

    // changeイベントを手動でトリガー
    var event = new Event("change");
    input.dispatchEvent(event);
}
async function onClickChoseFolder() {
    let res = await pywebview.api.showFolderDialog();
    input = document.getElementById('path-input');
    input.value = res;

    // changeイベントを手動でトリガー
    var event = new Event("change");
    input.dispatchEvent(event);
}

async function onClickChoseSaveFolder() {
    let res = await pywebview.api.showFolderDialog();
    input = document.getElementById('path-output');
    input.value = res;

    // changeイベントを手動でトリガー
    var event = new Event("change");
    input.dispatchEvent(event);
}

async function onClickSave() {
    const path = document.getElementById('path-output').value;
    console.log(path);
    let res = await pywebview.api.saveFile(path);
    console.log(res);
    if (res == 1) {
        alert("Folder not found");
    }
    else {
        onClickShowOnlyConvertMenu();
    }
}