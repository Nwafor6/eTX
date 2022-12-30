let registerForm=document.querySelector("#registerForm")
registerForm.addEventListener('submit',p=>{
	p.preventDefault()
	let ShowSuccesNotify=document.querySelector("#_successReg")
	ShowSuccesNotify.style.display="block"
	let email=document.querySelector("#exampleInputEmail1").value
	let first_name=document.querySelector("#exampleInputUsername1").value
	let last_name=document.querySelector("#exampleInputLatName").value
	let password=document.querySelector("#exampleInputPasswordll").value
	$.ajax(
		{
			type:'POST',
			url:"/account/register/",
			data:{
				'email': email,
				"first_name":first_name,
				"last_name":last_name,
				'password':password,
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
			},
			dataType:'json',
			success: function(response){
				console.log(response)
				let form_parent=document.querySelector("#form_parent")
				registerForm.reset()
				// let login_success=document.querySelector("#login-success")
				// login_success.style.display="block"
				_successReg.innerHTML=` <div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>Account created successfully now click 'login'</strong>
            </div>`
				setTimeout(()=>{document.querySelector("#login-btn")
				},1000)
				// window.location.replace("etx.pythonanywhere.com/login/")
			},
			error:function(error){
				console.log(error)
				//var err = JSON.parse(xhr.responseText);
			       _successReg.innerHTML=` <div class="alert alert-danger alert-dismissible fade show" role="alert">
            <strong>Error !! A user with this details already exist </strong>
            </div>`
            setTimeout(()=>{
            	_successReg.style.display="none"
            }, 3000)
			}
		}

		)

})
