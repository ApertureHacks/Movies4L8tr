function validateForm() {
	var name = document.forms["mainform"]["_user"].value;
	if(name==null || name=="") {
		alert("Name must be filled out");
		return false;
	}
	var phone = document.forms["mainform"]["_phone"].value;
	console.log(phone);
	var email = document.forms["mainform"]["_email"].value;
	if((phone==null && email==null) || (phone=="" && email=="") || (phone==null && email=="") || (phone=="" && email==null)) {
		alert("Either email or phone must be filled out");
		return false;
	}
	var movie = document.forms["mainform"]["_movie"].value;
	var release = document.forms["mainform"]["_release"].value;
	$.ajax(
		{
			type : 'POST',
			url : '/ajax',
			data : { name : name,
					 phone : phone,
					 email : email,
					 movie : movie,
					 release : release
					}
		}
	  ).done(function( returnData ){
		$("#gobutton").addClass("btn-success");
	  });

}
