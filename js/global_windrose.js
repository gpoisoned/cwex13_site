var global_CurrentImage;
var currentSite;

	
function removeQueryString(){
	var uri = window.location.toString();
	if (uri.indexOf("?") > 0) {
		var clean_uri = uri.substring(0, uri.indexOf("?"));
	   	window.history.replaceState({}, document.title, clean_uri);
	}
}
		 					
// This funciton is useful for displaying images from the index page based on user's choice
function getQueryString(){		
	var query = window.location.toString();	
	var FinalQuery = query.split("?")[1];
	return FinalQuery;
	//var FinalQuery = query.slice(1,query.length);		
}						

function init(siteName,imgName){
	currentSite = siteName;

	requestedImg = getQueryString();
	if (typeof(requestedImg) == "undefined"){
		showImage(imgName);
	}
	else{
		showImage(requestedImg);
	}

	removeQueryString();
		
}

function goHome(){
	var home = "index.html"
	document.getElementById("home").href= home;
}

function showImage(imgName) {
	var curImage = document.getElementById("Image");				
	curImage.src = imgName;	
	curImage.alt = imgName;
	curImage.title = imgName;
	global_CurrentImage = imgName.split('/')[1];				
}	

function nextSite(idName){
	var e = document.getElementById(idName);
	if(currentSite =="49"){
		var nxt = '61';
		e.href="windrose_a2.html"+"?"+nxt+"_windrose/"+global_CurrentImage;
	}
	else if(currentSite=="61"){
		var nxt ='68';
		e.href="windrose_a3.html"+"?"+nxt+"_windrose/"+global_CurrentImage;
	}

}

function prevSite(idName){
	var e = document.getElementById(idName);
	if(currentSite =="61"){
		var prev = '49';
		e.href="windrose_a1.html"+"?"+prev+"_windrose/"+global_CurrentImage;;
	}
	else if(currentSite=="68"){
		var prev ='61';
		e.href="windrose_a2.html"+"?"+prev+"_windrose/"+global_CurrentImage;
	}

}