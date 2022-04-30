function send_api()
{

var input_text = document.getElementById("input_text").value


    try {     
        const response = fetch('http://localhost:5000/', {
        method: 'post',
        body: JSON.stringify(
            {
                "inputText": input_text
            }
            ),
        headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        }
        )
        .then(response => response.json())
        .then(data => {
            document.getElementById("output_text").value = data.payload.correctedText;
            document.getElementById("text_edits").value = data.payload.edits;
        }
        );
    } 

    catch(err) {
        console.error(`Error: ${err}`);
    }
}

function reset()
{
    try {
            document.getElementById("input_text").value = ""
            document.getElementById("output_text").value = ""
            document.getElementById("text_edits").value = ""
        }
    catch(err) {
        console.error(`Error: ${err}`);
    }
}

function hide_edit_text_area() {
    try {
        var edit_text_box = document.getElementById("text_edits");
        var edit_button = document.getElementById("view-edit-btn");
        
        if (edit_text_box.style.display === "none") {
            edit_text_box.style.display = "block";
            edit_button.classList.add('active')
        } 
        else {
            edit_text_box.style.display = "none";
            edit_button.classList.add('active')
        }
    }
    catch(err) {
        console.error(`Error: ${err}`);
    }
}