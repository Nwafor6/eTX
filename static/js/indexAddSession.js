console.log("hello my people")
// Get csrf_token cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
// end the csrf_token function

// CREATE SESSION VIEW
let IndexAddSessionForm=document.querySelector("#indexaddSessionForm")
IndexAddSessionForm.addEventListener('submit',e=>{
e.preventDefault()
let session_title=document.querySelector("#session_title").value
	$.ajax({
		type:"POST",
		url:`${domain}/v1/departments/1/add_admittedsession/`,
		data:{
			"session_title":session_title,
		},
		headers: {'X-CSRFToken': getCookie('csrftoken')},
		dataType: 'json',
		success:function(response){
			IndexAddSessionForm.reset()
			alert("New Session Added succesful")
		},
		error:function(error){
			alert("Session already exist")
		}
	})
})