let sessions_holder=document.querySelector("#sessions_holder")
let domain= document.querySelector("#domain").value
let DepartmentId=document.querySelector("#department_id").value
let response_length=0;

// let clicked_session=document.querySelector(`#session${response[i].id}`)

// GET ALL SESSION
$.ajax({
	type:"GET",
	url:`/v1/departments/${DepartmentId}/add_admittedsession/`,
	success:function(response){
		for (i in response){
			sessions_holder.innerHTML +=`

			<tr class="table-info" id="session_del_table${response[i].id}">
              <td>
                ${response[i].id}
              </td>
              <td>
                ${response[i].session_title}
              </td>
              <td>
                ${response[i].created}
              </td>
               <td>
                <button type="button" data-id="/v1/update_admittedsession/${response[i].id}/" class="btn btn-primary border-0 text-white sessionsbtn" data-toggle="modal" data-target="#updatesession">Edit <i class="ti-file btn-icon-append"></i></button>
              </td>
              <td>
                <a href="/dept/${DepartmentId}/session/${response[i].id}/students/" class="btn btn-primary border-0 text-white">View</a>
              </td>
              <td data-id="${response[i].id}">
                <form id="sessiondelform" action="/v1/delete_admittedsession/${response[i].id}/" method="DELETE" data-id="${response[i].id}">
                <input type="hidden">
                <button type="submit" class="btn btn-danger border-0 text-white" data-id="${response[i].id}" id="ssessiondelbtn">Delete</button>
                </form>
              </td
            </tr>

			`

		}
		response_length=response.length
		// console.log(response_length)
	},
	error:function(error){
		console.log('erro',error)
	}
})