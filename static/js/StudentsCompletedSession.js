let Session=document.querySelector("#students_holder")
let Stud_id= document.querySelector("#stud_id").value

// GET ALL STUDENTS THE SESSION
$.ajax({
	type:"GET",
  cache:false,
	url:`/v1/student/${Stud_id}/session/`,
	success:function(response){
    let SessionResponse=response
    index=1;
    SessionResponse.forEach(session=>{
      Session.innerHTML +=`

            <tr class="" id="session_del_table">
                    <td>
                      ${index}
                    </td>
                    <td>
                      ${session.session_title}
                    </td>
                    <td>
                      <a href="javascripts:void(0)" class="btn btn-primary border-0 text-white" style="pointer-events:none" >First Semester</a>
                    </td>
                    <td>
                      <a href="javascripts:void(0)" class="btn btn-primary border-0 text-white" style="pointer-events:none" >Second Semester</a>
                    </td>
                    <td>
                      <a href="/transcript/student/${Stud_id}/session/${session.id}/allsemesters/" class="btn btn-danger border-0 text-white">Download</a>
                    </td>
                  </tr>

            `
            index +=1;
  
    })


	},
	error:function(error){
		console.log(error)
	}
})


