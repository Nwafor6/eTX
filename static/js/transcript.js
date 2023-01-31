let StudentId=document.querySelector("#student_id").value
let SessionId=document.querySelector("#session_id").value
let StdRegNum=document.querySelector("#std_reg_num")
let Semester_=document.querySelector("#semester_")
let Session_=document.querySelector("#session_")
let TranscriptTable=document.querySelector("#transcript_body")
let FirstTranscriptTotal=document.querySelector("#total_body")
let SecondTranscriptTotal=document.querySelector("#total_seon_body")
let SecondSemesterTranscript=document.querySelector("#Second_transcript_body")
let StdName=document.querySelector("#std_name")
let ExcelFirstSemesterResult=document.querySelector("#excel-first-transcript_body")
let ExcelSecondSemesterResult=document.querySelector("#excel-Second_transcript_body")
let Excel_First_Semester_Total=document.getElementById("#excel_first_semester_total_body")
let Excel_Second_Semester_Total=document.getElementById("#excel_second_semester_total_body")
$.ajax({
  type:"GET",
  cache:false,
  url:`/v1/student/${StudentId}/session/${SessionId}/semester/1/`,
  success:function(res){
    console.log(res)
    // Get the value for first and second semester 
    // quality points and total points respectively and CGPA
    FtotalQpt=res.FtotalQpt
    Ftotalpt=res.Ftotalpt
    stotalQpt=res.stotalQpt
    stotalpt=res.stotalpt
    results=res.serializer
    YearOfAdmission=res.student_addmitted_seesion
    cgpa=res.CGPA
    // end  getting of values
    //  Assign the cgpa value to the html holder
    $("#cgpaHtmlHoder").text(`${cgpa}`)
    index=1
    index2=1
    results.forEach(result=>{
      // Major pdf output data
      StdName.innerText = result.student.name
      TranscriptName=result.student.name
      StdRegNum.innerText=result.student.reg_number
      // Semester_.innerText=result.semester.title
      Session_.innerText=result.session.session_title
      // End major PDF output data

      // Major excel output data
      document.getElementById("excel-std-name").innerText=result.student.name;
      document.getElementById("excel-std-reg-no").innerText=result.student.reg_number
      // End major excel ouput data
      if(result.semester.title=="First Semester"){


        TranscriptTable.innerHTML +=`
           <tr>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${index}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.course_code}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.course_title}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.credit_load}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.grade}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.quality_point}
              </td>
            </tr>

        `
        index +=1;

        // compute same first semster result for to the excel sheet
        ExcelFirstSemesterResult.innerHTML +=`
           <tr>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.course_code}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.course_title}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.credit_load}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.grade}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.quality_point}
              </td>
            </tr>

        `
         // for the total and other stuffs
         FirstTranscriptTotal.innerHTML =`
               <tr>
                  <td style="padding: 0.25rem  0.9375rem !important">
                    
                  </td>
                  <td style="padding: 0.25rem  0.9375rem !important">
                  
                  </td>
                  <td style="padding: 0.25rem  0.9375rem !important">
                    
                  </td>
                  <td style="padding: 0.25rem  0.9375rem !important">
                    <strong>Total: ${Ftotalpt}</strong>
                  </td>
                  <td style="padding: 0.25rem  0.9375rem !important">
                    
                  </td>
                  <td style="padding: 0.25rem  0.9375rem !important">
                    <strong>Total: ${FtotalQpt}</strong>
                  </td>
                </tr>

            `
            // end for total and other stuffs
      };
    })
   
    // Seoond semester computation
    results.forEach(result=>{
      if(result.semester.title=="Second Semester"){


        SecondSemesterTranscript.innerHTML +=`
           <tr>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${index2}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.course_code}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.course_title}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.credit_load}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.grade}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.quality_point}
              </td>
            </tr>

        `
        index2 +=1

        // compute same second semster result for to the excel sheet
        ExcelSecondSemesterResult.innerHTML +=`
           <tr>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.course_code}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.course_title}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.credit_load}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.grade}
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                ${result.quality_point}
              </td>
            </tr>

        `

        // for the second semster point total
         SecondTranscriptTotal.innerHTML =`
           <tr>
              <td style="padding: 0.25rem  0.9375rem !important">
                
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
              
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                <strong>Total: ${stotalpt}</strong>
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                
              </td>
              <td style="padding: 0.25rem  0.9375rem !important">
                <strong>Total: ${stotalQpt}</strong>
              </td>
            </tr>

        `
        // populate the excel sheet's brought forward second semester result
        document.getElementById("b-foward-grade-total-point").innerText=FtotalQpt
        document.getElementById("b-foward-total-credit-load").innerText=Ftotalpt
        document.getElementById("excel-second-total-credit-load").innerText=stotalpt
        document.getElementById("excel-second-grade-total-point").innerText=stotalQpt
        document.getElementById("year_of_admission").innerText=YearOfAdmission
        document.getElementById("cgpa_excel").innerText=`(${FtotalQpt} + ${stotalQpt})/ (${Ftotalpt} + ${stotalpt}) = ${cgpa}`
        // end point
      };
    })


  },
  error:function(err){
    console.log(err)
  }
})


let PdfButton=document.querySelector("#pdfButton")
let CourseHolder=document.querySelector("#courseholder")
let DownloadNotification=document.querySelector("#download_notification")
let ExcelDownloadNotification=$("#excel_download_notification")


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


$("#excelButton").click(function(){
  $("#excel_download_notification").html(`<button class="btn btn-primary" type="button" disabled>
    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
    Loading...
  </button>`)
  console.log("just clicked and working now")
  let excel= document.getElementById("excel-transcripts-table");
  table=$(".table")
  let wb = XLSX.utils.table_to_book(excel)
  XLSX.writeFile(wb, `${TranscriptName}.xlsx`);
  setTimeout(()=>{
    $("#excel_download_notification").html(`<button type="button" class="btn btn-primary btn-icon-text text-white" id="excelButton"data-toggle="modal" data-target="#__exampleModal"><i class="ti-download btn-icon-prepend text-white"></i>Excel</button>`)
  }

    , 6000)
});



