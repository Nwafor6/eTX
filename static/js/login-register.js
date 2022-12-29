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
				window.location.href="etx.pythonanywhere.com"
				console.log("got here")
			},
			error:function(error){
				console.log(error)
			}
		}

		)

})


