var global_CurrentImage1;
var global_CurrentImage2;
var globalRetAddrArr;

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

			function showImage1(imgName) {
				var curImage = document.getElementById("Image1");				
				curImage.src = imgName;	
				curImage.alt = imgName;
				curImage.title = imgName;
				global_CurrentImage1 = imgName;				
			}			

			function showImage2(imgName) {
				var curImage = document.getElementById("Image2");				
				curImage.src = imgName;	
				curImage.alt = imgName;
				curImage.title = imgName;
				global_CurrentImage2 = imgName;				
			}	

			function displayImage(img1,img2){
				showImage1(img1);
				showImage2(img2);

			}

			function goHome(){
				var home = "index.html"
				document.getElementById("home").href= home;
			}

			function radPrevMonth(idname, curMth){
				var prevMth;
				if (curMth == "jul"){
					prevMth = "june";
				}
				else if (curMth =="aug"){
					prevMth = "july";
				}
				else if (curMth =="sep"){
					prevMth = "august";
				}
				document.getElementById(idname).href="radiometer_"+prevMth+".html";

			}

			function radNextMonth(idname, curMth){
				var nextMth;
				if (curMth == "jun"){
					nextMth = "july";
				}
				else if (curMth =="jul"){
					nextMth = "august";
				}
				else if (curMth =="aug"){
					nextMth = "september";
				}
				document.getElementById(idname).href="radiometer_"+nextMth+".html";
			}
			
