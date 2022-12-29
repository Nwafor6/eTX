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
			url:"http://127.0.0.1:8000/account/register/",
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
				window.location.href="http://127.0.0.1:8000/login/"
			},
			error:function(error){
				console.log(error)
			}
		}

		)

})