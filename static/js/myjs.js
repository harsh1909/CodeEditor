function submit_request(){
	document.getElementById("id_action").value ="submit_request"
}

function save_request(){
	document.getElementById("id_action").value ="save_request"
}

function clearcode(){
			document.getElementById("id_code_input").value =""
			document.getElementById("id_code_output").value=""
			document.getElementById("id_custom_input").value=""
			

		}

function show_custom(){
	var cur = document.getElementById("id_custom_input").style.display;
	if(cur=="none"){
		document.getElementById("id_custom_input").style.display="block";
	}	
	else{
		document.getElementById("id_custom_input").style.display="none";
	}
}

function readText(that){
	if(that.files && that.files[0])
	{
		var reader = new FileReader();
		reader.onload = function (e) {  
			var output=e.target.result;
			document.getElementById("id_code_input").value= output;
		};
		reader.readAsText(that.files[0]);
	}
}

function saveTextAsFile(textToWrite)
{
	var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'}); 
	var downloadLink = document.createElement("a");
	downloadLink.download = 'download.txt';
	downloadLink.innerHTML = "Download File";
	if (window.webkitURL != null)
	{
		// Chrome allows the link to be clicked
		// without actually adding it to the DOM.
		downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
	}
	else
	{
		// Firefox requires the link to be added to the DOM
		// before it can be clicked.
		downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
		downloadLink.onclick = destroyClickedElement;
		downloadLink.style.display = "none";
		document.body.appendChild(downloadLink);
	}

	downloadLink.click();
}