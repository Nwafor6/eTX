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
			url:"http://127.0.0.1:8000/account/login/",
			data:{
				'email': email,
				'password':password,
			},
			dataType:'json',
			success: function(response){
				login_btn.style.display="none"
				login_success.style.display="block"
				setTimeout(()=>{
				},1000)
				window.location.href="http://127.0.0.1:8000"
			},
			error:function(error){
				console.log(error)
			}
		}

		)

})


