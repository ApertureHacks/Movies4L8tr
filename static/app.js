function validateForm() {
	var name = document.forms["mainform"]["_user"].value;
	if(name==null || name=="") {
		alert("Name must be filled out");
		return false;
	}
	var phone = document.forms["mainform"]["_phone"].value;
	var email = document.forms["mainform"]["_email"].value;
	if((phone==null && email==null) || (phone=="" && email=="") || (phone==null && email=="") || (phone=="" && email==null)) {
		alert("Either email or phone must be filled out");
		return false;
	}
	//use the jquery ajax helpers
	$.ajax(
	{
		type: "POST",
		url: "ajax",
		data: { name : name,
				email : email,
				phone: phone}
	}
	).done(function( returnData ) {

		$("#gobutton").addClass("btn-success");
}
