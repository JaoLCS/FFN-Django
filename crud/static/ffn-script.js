function form_edit(){
    var campo = document.getElementById("id_tema")
    campo.classList.add("form-control")
    campo.style.fontFamily("Libre Franklin")
}

document.onload = form_edit()

function form_edit_noticia(){
    var inputs = document.getElementsByTagName("input")

    inputs[1].classList.add("form-control")
    inputs[1].style.fontFamily("Libre Franklin")
}

document.onload = form_edit_noticia()