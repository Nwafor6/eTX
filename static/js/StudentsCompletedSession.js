let Session=document.querySelector("#students_holder")
let Stud_id= document.querySelector("#stud_id").value
let TranscriptTable=document.querySelector("#transcript_body")
let SecondSemesterTranscript=document.querySelector("#Second_transcript_body")
let StdName=document.querySelector("#std_name")



let StdRegNum=document.querySelector("#std_reg_num")
let Semester_=document.querySelector("#semester_")
let Session_=document.querySelector("#session_")
let domain= document.querySelector("#domain").value
let TranscriptName=""

// GET ALL STUDENTS THE SESSION
$.ajax({
	type:"GET",
	url:`${domain}/v1/student/${Stud_id}/session/`,
	success:function(response){
    let SessionResponse=response
    index=1;
    SessionResponse.forEach(session=>{
      let SessionSemester=session.semester
      SessionSemester.forEach(semester=>{

          Session.innerHTML +=`

            <tr class="" id="session_del_table">
                    <td>
                      ${index} 
                    </td>
                    <td>
                      ${semester.session.session_title}
                    </td>
                    <td>
                      <a href="javascripts:void(0)" class="btn btn-primary border-0 text-white" style="pointer-events:none" >${semester.title}</a>
                    </td>
                    <td>
                      <button data-sems_id="${semester.id}" data-sess_id="${semester.session.id}" type="button" class="btn btn-danger btn-icon-text" data-toggle="modal" data-target="#exampleModal" id="semester_btn" ><i class="ti-download btn-icon-prepend"></i>View</button>
                    </td>
                  </tr>

            `
            index +=1;

      })
    })
    
	
	},
	error:function(error){
		console.log(error)
	}
})

// Allow the DOM to load
document.addEventListener("DOMContentLoaded", function(e) {
  Sems_id=""
  Sess_id=""
  let SemesterBtn=document.querySelectorAll("#semester_btn")
  SemesterBtn.forEach(btn=>{
    btn.addEventListener("click",function(){
      TranscriptTable.innerHTML =""
      SecondSemesterTranscript.innerHTML =""
      Sems_id=this.dataset.sems_id
      Sess_id=this.dataset.sess_id
      $.ajax({
        type:"GET",
        url:`${domain}/v1/student/${Stud_id}/session/${Sess_id}/semester/${Sems_id}/`,
        success:function(res){
          console.log(res)
          results=res
          index=1
          index2=1
          results.forEach(result=>{
            StdName.innerText = result.student.name
            TranscriptName=result.student.name
            StdRegNum.innerText=result.student.reg_number
            // Semester_.innerText=result.semester.title
            Session_.innerText=result.session.session_title
            if(result.semester.title=="First Semester"){

            
              TranscriptTable.innerHTML +=`
                 <tr>
                    <td>
                      ${index}
                    </td>
                    <td>
                      ${result.course_code}
                    </td>
                    <td>
                      ${result.course_title}
                    </td>
                    <td>
                      ${result.credit_load}
                    </td>
                    <td>
                      ${result.grade}
                    </td>
                    <td>
                      ${result.quality_point}
                    </td>
                  </tr>  

              `
              index +=1
            };
          })
          // Seoond semester computation
          results.forEach(result=>{
            if(result.semester.title=="Second Semester"){

            
              SecondSemesterTranscript.innerHTML +=`
                 <tr>
                    <td>
                      ${index2}
                    </td>
                    <td>
                      ${result.course_code}
                    </td>
                    <td>
                      ${result.course_title}
                    </td>
                    <td>
                      ${result.credit_load}
                    </td>
                    <td>
                      ${result.grade}
                    </td>
                    <td>
                      ${result.quality_point}
                    </td>
                  </tr> 

              `
              index2 +=1
            };
          })

        },
        error:function(err){
          console.log(err)
        }
      })
    })
  })
})

let PdfButton=document.querySelector("#pdfButton")
let CourseHolder=document.querySelector("#courseholder")
let DownloadNotification=document.querySelector("#download_notification")



PdfButton.addEventListener("click",function(){

        DownloadNotification.innerHTML=`<button class="btn btn-primary" type="button" disabled>
          <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
          Loading...
        </button>`
        // Choose the element id which you want to export.
        var element = document.getElementById('courseholder');
        element.style.width = '700px';
        element.style.height = '900px';
        var opt = {
            margin:       0.5,
            filename:     `${TranscriptName}.pdf`,
            image:        { type: 'jpeg', quality: 1 },
            html2canvas:  { scale: 1 },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait',precision: '12' }
          };
        
        // choose the element and pass it to html2pdf() function and call the save() on it to save as pdf.
        html2pdf().set(opt).from(element).save();
        setTimeout(()=>{
          DownloadNotification.innerHTML=`<button type="button" class="btn btn-danger btn-icon-text" id="pdfButton"><i class="ti-download btn-icon-prepend"></i>Download</button>`
        }

          , 6000)
      })




