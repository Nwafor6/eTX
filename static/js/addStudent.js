let AddStudentBtn= document.querySelector("#addStudentbtn")

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

let AddStudentNotification=document.querySelector("#addstudentnotification")

	$("form#addStudentForm").submit(function(e){
		e.preventDefault()
		var formData=new FormData(this)
	// })
	$.ajax({
		type:"POST",
		url:`${domain}/v1/upload/student/`,
		data:formData,
		dataType:'json',
		processData:false,
		contentType:false,
		cache:false,
		headers: {'X-CSRFToken': getCookie('csrftoken')},
		success:function(response){
			// alert(response)
			AddStudentNotification.innerHTML=`<div class="alert alert-warning alert-dismissible fade show" role="alert">
            <small>${response}</small>
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button></div>`
		},
		error:function(error){
			console.log(error)
		}
	})
})
