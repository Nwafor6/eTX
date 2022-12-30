let registerForm=document.querySelector("#registerForm")
registerForm.addEventListener('submit',p=>{
	p.preventDefault()
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
				let form_parent=document.querySelector("#form_parent")
				form_parent.style.display="none";
				let login_success=document.querySelector("#login-success")
				login_success.style.display="block"
				setTimeout(()=>{
				},1000)
				window.location.replace("etx.pythonanywhere.com/login/")
			},
			error:function(error){
				console.log(error)
				//var err = JSON.parse(xhr.responseText);
			       _successReg.innerHTML=` <div class="alert alert-danger" role="alert" id="login-success">
                  		Error ! This user seems to exist </div>`
			}
		}

		)

})
