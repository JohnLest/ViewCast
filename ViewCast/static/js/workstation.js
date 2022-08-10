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
    let data = ev.dataTransfer.getData("text");
    let to_clone = document.getElementById(data).cloneNode(true);
    to_clone.id= `${data}-clone`;
    ev.target.appendChild(to_clone);
    var row_img = document.getElementById("time-line-img");
    var row_input = document.getElementById("time-line-input");
    var new_cell_img = row_img.insertCell(-1);
    var new_cell_input = row_input.insertCell(-1);

    let index = new_cell_input.cellIndex -1;
    let id_img = `${data}-${index}-img`;
    let id_in = `${data}-${index}-txt`;

    let img = document.getElementById("next-img");
    let input = document.getElementById("next-in-txt");
    img.id = id_img;
    img.removeAttribute("ondragover");
    img.removeAttribute("ondrop");
    input.id = id_in;
    input.name = id_in;
    input.setAttribute("required", "")

    new_cell_img.setAttribute("id", "next-img");
    new_cell_img.setAttribute("ondragover", "allowDrop(event)");
    new_cell_img.setAttribute("ondrop", "drop(event)");

    new_cell_input.setAttribute("class", "time-line-input")
    let new_cell_in_txt = document.createElement("input")
    new_cell_in_txt.setAttribute("type", "number")
    new_cell_in_txt.setAttribute("id", "next-in-txt")
    new_cell_in_txt.setAttribute("name", "next-in-txt")
    new_cell_input.appendChild(new_cell_in_txt);
}

function validate_flux(){
    let td = document.getElementsByClassName("time-line-input");
    var error_div = document.getElementById("error");
    if(td.length <= 1){
        error_div.innerHTML = "No media in flux";
        return false;
    }
    let start_date = document.getElementById("start-date");
    let end_date = document.getElementById("end-date");
    let currentDate = new Date();
    if(end_date.value){
        let date= new Date(end_date.value + 'Z');
        if(date < currentDate.getTime()){
            error_div.innerHTML = `The end date ${end_date.value} in in the past`;
            return false;
        }
    }
    if(start_date.value && end_date.value){
        let start = new Date(start_date.value + 'Z');
        let end = new Date(end_date.value + 'Z');
        if(end.getTime() < start.getTime()){
            error_div.innerHTML = `The start date ${start_date.value} start after the end date ${end_date.value}`;
            return false;
        }
    }
    return false;
}