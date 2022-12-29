let Session=document.querySelector("#students_holder")
let SessionId=document.querySelector("#students_session").value
let Dept_id= document.querySelector("#dept_id").value
let Notify=document.querySelector("#notify")
let domain= document.querySelector("#domain").value

// GET ALL STUDENTS THE SESSION
$.ajax({
	type:"GET",
	url:`/v1/department/${Dept_id}/session/${SessionId}/students/`,
	success:function(response){
    for(i in response){

      Session.innerHTML +=`

      <tr class="table-info" id="session_del_table${response[i].id}">
              <td>
                ${response[i].name}
              </td>
              <td>
                ${response[i].department.title}
              </td>
              <td>
                ${response[i].reg_number}
              </td>
              <td>
                ${response[i].admitted_session.session_title}
              </td>
              <td>
                <a href="/student/${response[i].id}/completed-session/" class="btn btn-primary border-0 text-white">View</a>
              </td>
            </tr>

      `

    }
    if (response.length ===0){
      Notify.innerHTML =`
          <strong>No Students Admitted in this Session Yet</strong>
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
      `
      Notify.style.display="block";

    }


	},
	error:function(error){
		console.log(error)
	}
})



let onetime=document.querySelector("#onetime")
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



// Search and filter student by registration number
let StudentRegNum=document.querySelector("#search_student")
let SearchForm=document.querySelector("#search_form")
$("#search_form").submit(function(e){
  e.preventDefault();
  $.ajax({
    type:"POST",
    url:`/v1/department/${Dept_id}/session/${SessionId}/students/`,
    data:{
      "reg_num":StudentRegNum.value
    },
    headers: {'X-CSRFToken': getCookie('csrftoken')},
    success:function(response){
      SearchForm.reset();
       for(i in response){

      Session.innerHTML =`

      <tr class="table-info" id="session_del_table${response[i].id}">
              <td>
                ${response[i].name}
              </td>
              <td>
                ${response[i].department.title}
              </td>
              <td>
                ${response[i].reg_number}
              </td>
              <td>
                ${response[i].admitted_session.session_title}
              </td>
              <td>
                <a href="/student/${response[i].id}/completed-session/" class="btn btn-primary border-0 text-white">View</a>
              </td>
            </tr>

      `

    }
    if (response.length ===0){
      Notify.innerHTML =`
          <strong>Student with this registration number does not exist</strong>
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
      `
      Notify.style.display="block";

    }

    },
    error:function(error){
      console.log(error)
    }
  })
})