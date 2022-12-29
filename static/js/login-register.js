let login_form=document.querySelector("#login-form")
let login_success=document.querySelector("#login-success")
let LoginResponse=document.querySelector("#login_response")
let login_btn=document.querySelector("#login-btn")
console.log("login")
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
<<<<<<< HEAD
=======

>>>>>>> d461b623e576dd5ea82f8b7a0969667ebfc58007
				LoginResponse.innerHTML=`<div class="alert alert-success" role="alert" id="login-success" >
                    ${response}
                  </div>`
<<<<<<< HEAD
=======

>>>>>>> d461b623e576dd5ea82f8b7a0969667ebfc58007
				login_btn.style.display="none"
				login_success.style.display="block"
				console.log(response)
				setTimeout(()=>{
					LoginResponse.innerHTML=`<button type="submit" class="btn btn-block btn-facebook auth-form-btn" id="login-btn">
                    Sign In
                  </button>`
				},1000)
<<<<<<< HEAD
				window.location.replace("etx.pythonanywhere.com")
=======
				window.location.reload()
>>>>>>> d461b623e576dd5ea82f8b7a0969667ebfc58007
				console.log("got here")
			},
			error:function(error){
				console.log(error)
				// LoginResponse.innerHTML=``
			}
		}

		)

})



