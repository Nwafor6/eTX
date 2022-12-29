let Session=document.querySelector("#students_holder")
// let SessionId=document.querySelector("#students_session").value
let Stud_id= document.querySelector("#stud_id").value
// console.log(SessionId)
let domain= document.querySelector("#domain").value

// GET ALL STUDENTS THE SESSION
$.ajax({
	type:"GET",
	url:`${domain}/v1/student/${Stud_id}/session/`,
	success:function(response){
		console.log(response)
    console.log(response)
    for(i in response){

      Session.innerHTML +=`

      <tr class="table-info" id="session_del_table${response[i].id}">
              <td>
                ${response[i].id} 
              </td>
              <td>
                ${response[i].session_title}
              </td>
              <td>
                <a href="" class="btn btn-primary border-0 text-white" >${response[i].session_title} - First Semester</a>
              </td>
              <td>
                <a href="" class="btn btn-primary border-0 text-white" >${response[i].session_title} - Second Semester</a>
              </td>
              <td>
                <a href="${domain}/session/${response[i].id}/students/" class="btn btn-primary border-0 text-white">View</a>
              </td>
            </tr>

      `

    }
    arr_1=response
    arr_1.forEach(res=>{
      console.log(res.session_title,"session_title")
      arr_2=res.semester
      arr_2.forEach(sems=>{
        console.log(sems.id,sems.title,"semster id", sems.session.session_title)
      })
    })

	
	},
	error:function(error){
		console.log(error)
	}
})
// arr_1=[2,3,[3,4,5,6,7,],5]
// arr_2=[9,8]

// arr_1.forEach(x=>{
//   arr_2.forEach(y=>{
//     console.log(x,y)
//   })
// })


# view all courses for the students has  completed ######
class StudentSemesterCourse(generics.RetrieveAPIView):
  queryset=Student.objects.all()
  serializer_class=StudentSerializer
  permission_classes=[IsAuthenticated]

  def get(self, request, *args, **kwargs):
    queryset=AdmittedSession.objects.get(id=self.kwargs['sess_id'])
    first_semester=Semester.objects.get(session=queryset, title="First Semester")
    second_semester=Semester.objects.get(session=queryset, title="Second Semester")
    # print(first_semester,"first",second_semester,"second")
    first_sems_courses=[courses for courses in first_semester.course_set.filter(student=self.kwargs['pk'], semester=first_semester ) ]
    second_sems_courses=[courses for courses in second_semester.course_set.filter(student=self.kwargs['pk'], semester=second_semester ) ]
    complete_courses=[first_sems_courses,second_sems_courses]
    print(complete_courses)
    # get all sesmester of this session
    # print(queryset.session_title.id)
    print(Student.objects.get(id=self.kwargs['pk']),"student")
    semester_title=Semester.objects.get(id=self.kwargs['sems_id'])
    print(semester_title.title,"jhhuhu")
    semester=Semester.objects.get(title=semester_title.title,session_id=self.kwargs['sess_id'],)
    print(semester)
    courses=semester.course_set.filter(student=self.kwargs['pk'], semester=semester )
    serializer=ModifedCourseSerializer(complete_courses, many=True)
    return Response(serializer.data)












    <script >
        let login_form=document.querySelector("#login-form")
        let login_success=document.querySelector("#login-success")
        let login_btn=document.querySelector("#login-btn")
        login_form.addEventListener('submit',e=>{
          e.preventDefault()
          let email= document.querySelector("#exampleInputEmail1").value
          let password= document.querySelector("#exampleInputPassword1").value

          $.ajax(
            {
              type:'POST',
              url:"/account/login/",
              data:{
                'email': email,
                'password':password,
              },
              dataType:'json',
              success: function(response){
                login_btn.style.display="none"
                login_success.style.display="block"
                console.log(response)
                setTimeout(()=>{
                },1000)
                window.location.replace("etx.pythonanywhere.com")
                console.log("got here")
              },
              error:function(error){
                console.log(error)
              }
            }

            )

        })
    </script>