let sessions_holder=document.querySelector("#sessions_holder")
let domain= document.querySelector("#domain").value
let response_length=0;

// let clicked_session=document.querySelector(`#session${response[i].id}`)

// GET ALL SESSION 
$.ajax({
	type:"GET",
	url:`${domain}/v1/departments/`,
	success:function(response){
		console.log(response)
		for (i in response){
			sessions_holder.innerHTML +=`

			<tr class="table-info" id="session_del_table${response[i].id}">
              <td>
                ${response[i].id}
              </td>
              <td>
                ${response[i].title}
              </td>
               <td>
                <button type="button" data-id="${domain}/v1/departments/${response[i].id}/" class="btn btn-primary border-0 text-white sessionsbtn" data-toggle="modal" data-target="#updatesession">Edit <i class="ti-file btn-icon-append"></i></button>
              </td>
              <td>
                <a href="${domain}/sessions/${response[i].id}/" class="btn btn-primary border-0 text-white">View</a>
              </td>
              <td data-id="${response[i].id}">
                <form id="sessiondelform"  method="DELETE" data-id="${response[i].id}">
                <input type="hidden">
                <button type="submit" class="btn btn-danger border-0 text-white" data-id="${response[i].id}" id="ssessiondelbtn">Delete</button>
                </form>
              </td
            </tr>

			`
			
		}
		response_length=response.length
	},
	error:function(error){
		console.log('erro',error)
	}
})


// CREATE SESSION VIEW
let addSessionForm=document.querySelector("#addSessionForm")
addSessionForm.addEventListener('submit',e=>{
e.preventDefault()
let title=document.querySelector("#exampleInputUsername1").value
	$.ajax({
		type:"POST",
		url:`${domain}/v1/departments/`,
		data:{
			"title":title,
			'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
		},
		dataType: 'json',
		success:function(response){

				sessions_holder.innerHTML +=`

				<tr class="table-info">
          <td>
            ${response.id}
          </td>
          <td>
            ${response.title}
          </td>
           <td>
                <a href="${domain}/v1/departments/${response.id}/" class="btn btn-primary border-0 text-white">Edit</a>
              </td>
              <td>
                <a href="" class="btn btn-primary border-0 text-white">View</a>
              </td>
              <td>
                <a href="" class="btn btn-danger border-0 text-white">Delete</a>
              </td>
        </tr>

				`
				addSessionForm.reset()
		},
		error:function(error){
			console.log('erro',error)
		}
	})
})

// Update SESSIONS
// Allow the DOM to load first
document.addEventListener("DOMContentLoaded", function(e) {

		let sessionsbtn=document.querySelectorAll(".sessionsbtn");
		console.log(sessionsbtn);
		let sessionbtn_id="";
		console.log(sessionsbtn.length)
		for (let i=0; i<sessionsbtn.length; i++){
				console.log('BhjgVHG')
				sessionsbtn[i].addEventListener('click',function(){
						sessionbtn_id = this.dataset.id
						console.log(sessionbtn_id)
						$.ajax({
								type:"GET",
								url:`${sessionbtn_id}`,
								success:function(res){
									console.log(res)
									document.querySelector("#exampleInputUsername").value=res.title
								}
						})
				})
		}
		// sumbit form for updating
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

		let updateSessionForm=document.querySelector("#updateSessionForm")
		// console.log(updateSessionForm.innerHTML)
		updateSessionForm.addEventListener("submit",e=>{
			e.preventDefault()
			let exampleInputUsername=document.querySelector("#exampleInputUsername").value
			console.log(exampleInputUsername)
			// let csrf_token=$("input[name=csrfmiddlewaretoken]").val()
			$.ajax({
					type:"PUT",
					url:`${sessionbtn_id}`,
					data:{
						'title':exampleInputUsername,
					},
					headers: {'X-CSRFToken': getCookie('csrftoken')},
					dataType:'json',
					success:function(response){
						console.log(response)
						updateSessionForm.reset()
						document.querySelector(`#session_del_table${response.id}`).innerHTML=`

						<tr class="table-info" id="session_del_table${response.id}">
              <td>
                ${response.id}
              </td>
              <td>
                ${response.title}
              </td>
               <td>
                <button type="button" data-id="${domain}/v1/departments/${response.id}/" class="btn btn-primary border-0 text-white sessionsbtn" data-toggle="modal" data-target="#updatesession">Edit <i class="ti-file btn-icon-append"></i></button>
              </td>
              <td>
                <a href="${domain}/session/${response.id}/students/" class="btn btn-primary border-0 text-white">View</a>
              </td>
              <td data-id="${response.id}">
                <form id="sessiondelform" action="${domain}/v1/delete_admittedsession/${response.id}/" method="DELETE" data-id="${response.id}">
                <input type="hidden">
                <button type="submit" class="btn btn-danger border-0 text-white" data-id="${response.id}" id="ssessiondelbtn">Delete</button>
                </form>
              </td
            </tr>

						`

					},
					error:function(err){
						console.log(err)
					}
			})
		})

})


// Delete section
// Allow the DOM to load first
document.addEventListener("DOMContentLoaded", function(e) {


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

	let ssessiondelbtn=document.querySelectorAll("#ssessiondelbtn")
	let Alert=document.querySelector("._alert")
	Alert.style.display="none"
	console.log(ssessiondelbtn)
	for (let i=0; i<ssessiondelbtn.length; i++){
		ssessiondelbtn[i].addEventListener('click',function(){
			ssessiondelbtn_id = this.dataset.id
			session_del_table= ssessiondelbtn_id
			console.log(ssessiondelbtn_id)
			let sessiondelform=document.querySelectorAll("#sessiondelform")
			console.log(sessiondelform)

	// Confirm if the user wants to delete the department
		if(confirm('Sure want to delete this session?')){
					for (let i=0; i<sessiondelform.length; i++){
							sessiondelform[i].addEventListener("submit",e=>{
							e.preventDefault()
							

									$.ajax({
									type:"DELETE",
									url:`${domain}/v1/departments/${ssessiondelbtn_id}/`,
									headers: {'X-CSRFToken': getCookie('csrftoken')},
									success:function(response){
										let session_del_table= document.querySelector(`#session_del_table${ssessiondelbtn_id}`)
										console.log(response)
										session_del_table.style.display="none"
										Alert.style.display="block"
									},
									error:function(error){
										console.log(error)

									}
								})			
					})

					}
				
		}
		})
	}
})







