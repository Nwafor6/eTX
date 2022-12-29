let domain= document.querySelector("#domain").value

let logout_btn=document.querySelector("#logout_btn")
logout_btn.addEventListener('click',()=>{
	$.ajax({
		type:'GET',
		url:`${domain}/account/logout/`,
		success:function(response){
			window.location.href="http://127.0.0.1:8000/login/"
		},
		error:function(error){
			console.log(error)
		}
	})
})