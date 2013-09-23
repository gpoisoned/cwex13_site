
// This is the global current image displayed
var global_CurrentImage;


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

			function createRadLinkImgName(idname){
				var returnAddr = window.location.toString()+"/"+imgAttr()+;

				var elem = document.getElementById(idname);
				elem.href = "radiometer_"+getMonth()+".html"+"?"+radImgPath()+"&"+returnAddr;

			}

			function mthToNum(x){
				var toReturn = new Array();
				if (x =="june"){
					toReturn[0] ="06";
					toReturn[1] = "Rad_jun";
				}
				else if(x =="july")
				{
					toReturn[0] ="07";
					toReturn[1] = "Rad_jul";
				}
				else if (x =="august"){
					toReturn[0] ="08";
					toReturn[1] = "Rad_aug";
				}
				else if (x =="september"){
					toReturn[0] ="09";
					toReturn[1] = "Rad_sep";
				}
				return toReturn;
			}

			function radImgPath(){
				var rtn_val = getCurImgDay();
				var mth = mthToNum(getMonth());
				return mth[1]+"/"+"2013-"+mth[0]+"-"+rtn_val;			
		 	}	

		 	function getImgFilePath(){
				var curUrl = window.location.toString().split('/');
		 		var getFile = curUrl[curUrl.length-1].split('.')[0];
		 		return getFile;
		 	}

		 	function getSiteName(){
		 		var getFile = getImgFilePath();
		 		var siteName = getFile.slice(0,2);
		 		return siteName;
		 	}

		 	function imgAttr(){
		 		var siteName = getSiteName();
		 		var siteNum = siteName.slice(1,siteName.length);
				if (siteNum == "1"){
					var i_attr ="WC49_Img/";
				}
				else if(siteNum == "2"){
					var i_attr ="WC61_Img/";
				}
				else if (siteNum == "3"){
					var i_attr = "WC68_Img/";
				}
				return i_attr;
		 	}	

		 	function getMonth(){
		 		var getFile = getImgFilePath();
		 		return getFile.slice(2,getFile.length);

		 	}	

			function showImage(imgName) {
				var curImage = document.getElementById("Image");				
				curImage.src = imgName;	
				curImage.alt = imgName;
				curImage.title = imgName;
				global_CurrentImage = imgName;				
			}			

			function preLoadImages() {
				var tmp = new Array();
				for(var i = 0; i < arguments.length; i++) {
					tmp[i] = new Image();
					tmp[i].src = arguments[i];						
				}			
			}

			function goHome(){
				var home = "index.html"
				document.getElementById("home").href= home;
			}

			function getCurImgDay(){
				var m_d = global_CurrentImage.split('-')[1].split('.')[0];
				return m_d.slice(m_d.length-2,m_d.length);
			}

			function nextMonth(idname){	
				var getFile = getImgFilePath();
		 		var siteName= getFile.slice(2,getFile.length);	
				var curMonth = getMonth();
				alert(curMonth);
				var day = getCurImgDay();
				var siteNum = siteName.slice(1,siteName.length);
				if (siteNum == "1"){
					var i_attr ="WC49_Img/";
				}
				else if(siteNum == "2"){
					var i_attr ="WC61_Img/";
				}
				else if (siteNum == "3"){
					var i_attr = "WC68_Img/";
				}

				if (curMonth == "june"){
					var nextMonth = "july";
					var m_attr = "Jul";
				}
				else if (curMonth == "july"){
					var nextMonth = "august";
					var m_attr = "Aug";
				}
				else if (curMonth == "august"){
					var nextMonth = "september";
					var m_attr = "Sept";
				}
				
		     //document.getElementById(idname).href = siteName+nextMonth+".html?"+i_attr+siteName.toUpperCase()+'-'+m_attr+day+'.jpg';
		     document.getElementById(idname).href = siteName+nextMonth+".html";
		    }

			function prevMonth(idname){;
				var curMonth = getMonth();
				var day = getCurImgDay();
				var siteName = getSiteName();

				var day = getCurImgDay();
				var siteNum = siteName.slice(1,siteName.length);
				if (siteNum == "1"){
					var i_attr ="WC49_Img/";
				}
				else if(siteNum == "2"){
					var i_attr ="WC61_Img/";
				}
				else if (siteNum == "3"){
					var i_attr = "WC68_Img/";
				}

				if (curMonth == "july"){
					var prevMonth = "june";
					var m_attr = "Jun";
				}
				else if (curMonth == "august"){
					var prevMonth = "july";
					var m_attr = "Jul";
				}
				else if (curMonth == "september"){
					var prevMonth = "august";
					var m_attr = "Aug";
				}
				//document.getElementById(idname).href = siteName+prevMonth+".html?"+i_attr+siteName.toUpperCase()+'-'+m_attr+day+'.jpg';
				document.getElementById(idname).href=siteName+prevMonth+".html";
			}


			