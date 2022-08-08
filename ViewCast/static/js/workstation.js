function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev, text) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data).cloneNode(true));
    let new_id_img = data + "-img";
    let new_id_in_hide = data + "-in-hide";
    let new_id_in_txt = data + "-in-txt";
    let new_img = document.getElementById("next-img");
    let new_in_hide = document.getElementById("next-in-hide");
    let new_in_txt = document.getElementById("next-in-txt");
    new_img.id = new_id_img;
    new_img.removeAttribute("ondragover");
    new_img.removeAttribute("ondrop");
    new_in_hide.id = new_id_in_hide;
    new_in_hide.name = new_id_in_hide;
    new_in_hide.value = data;
    new_in_txt.id = new_id_in_txt;
    new_in_txt.name = new_id_in_txt;

    var row_img = document.getElementById("time-line-img");
    var row_input = document.getElementById("time-line-input");
    var new_cell_img = row_img.insertCell(-1);
    new_cell_img.setAttribute("id", "next-img");
    new_cell_img.setAttribute("ondragover", "allowDrop(event)");
    new_cell_img.setAttribute("ondrop", "drop(event)");

    var new_cell_input = row_input.insertCell(-1);
    new_cell_input.setAttribute("class", "time-line-input")
    let new_cell_in_hide = document.createElement("input")
    new_cell_in_hide.setAttribute("type", "hidden")
    new_cell_in_hide.setAttribute("id", "next-in-hide")
    new_cell_in_hide.setAttribute("name", "next-in-hide")
    new_cell_in_hide.setAttribute("value", "")
    let new_cell_in_txt = document.createElement("input")
    new_cell_in_txt.setAttribute("type", "number")
    new_cell_in_txt.setAttribute("id", "next-in-txt")
    new_cell_in_txt.setAttribute("name", "next-in-txt")
    new_cell_input.appendChild(new_cell_in_hide)
    new_cell_input.appendChild(new_cell_in_txt)
}