let domain= document.querySelector("#domain").value

let logout_btn=document.querySelector("#logout_btn")
logout_btn.addEventListener('click',()=>{
	$.ajax({
		type:'GET',
		url:`/account/logout/`,
		success:function(response){
			window.location.href="/login/"
		},
		error:function(error){
			console.log(error)
		}
	})
})