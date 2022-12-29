// Javascript for uploading result on the hoome page
console.log("no more working")
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

let UploadResultNotification=document.querySelector("#uploadresultnotification")

    $("form#uploadresultForm").submit(function(e){
        e.preventDefault();
        var formData=new FormData(this);
        onetime.innerHTML=`<button class="btn btn-primary" type="button" disabled>
          <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
          Loading...
        </button>`

    // })
    $.ajax({
        type:"POST",
        url:`/v1/upload/`,
        data:formData,
        dataType:'json',
        processData:false,
        contentType:false,
        cache:false,
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        success:function(response){
            UploadResultNotification.innerHTML=`<div class="alert alert-warning alert-dismissible fade show" role="alert">
            <small>${response}</small>
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button></div>`
            onetime.innerHTML=`<button id="uploadresulttbn" type="submit" class="btn btn-primary me-2">Upload</button>`
            document.querySelector("#uploadresultForm").reset()
        },
        error:function(error){
            console.log(error)
            UploadResultNotification.innerHTML=`<div class="alert alert-warning alert-dismissible fade show" role="alert">
            <small>${error}</small>
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button></div>`
            onetime.innerHTML=`<button id="uploadresulttbn" type="submit" class="btn btn-primary me-2">Upload</button>`

        }
    })
})
// End of javascript for uploading reuslt on the home page

// ###################################################
// JavsScript for adding a new session to from the home page

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
// const csrftoken = getCookie('csrftoken');
// end the csrf_token function

// CREATE SESSION VIEW
let IndexAddSessionForm=document.querySelector("#indexaddSessionForm")
IndexAddSessionForm.addEventListener('submit',e=>{
e.preventDefault()
let session_title=document.querySelector("#session_title").value
    $.ajax({
        type:"POST",
        url:`/v1/departments/1/add_admittedsession/`,
        data:{
            "session_title":session_title,
        },
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        dataType: 'json',
        success:function(response){
            IndexAddSessionForm.reset()
            document.querySelector("#addsessionnotification").innerHTML=`<div class="alert alert-success alert-dismissible fade show" role="alert">
            <small>${response.session_title} session created successfully </small>
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button></div>`
        },
        error:function(error){
            console.log(error)
            document.querySelector("#addsessionnotification").innerHTML=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
            <small>An Error occured. This session seems to exist already. </small>
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button></div>`
        }
    })
})


// #########################################################
// Javascript for adding a students via the front page
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
// const csrftoken = getCookie('csrftoken');
// end the csrf_token function
console.log("now goodw")
let AddStudentNotification=document.querySelector("#addstudentnotification")

    $("form#addStudentForm").submit(function(e){
        e.preventDefault()
        var formData=new FormData(this)
    // })
    $.ajax({
        type:"POST",
        url:`/v1/upload/student/`,
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
             document.querySelector("#addStudentForm").reset()
        },
        error:function(error){
            console.log(error)
        }
    })
})
