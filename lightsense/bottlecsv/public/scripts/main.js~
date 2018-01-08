//functions to show/hide elements
function show(elementclass) {
    for (var i = 0; i < elementclass.length; i++) {
      elementclass[i].style.display = 'block';
    }
}

function hide(elementclass) {
    for (var i = 0; i < elementclass.length; i++) {
      elementclass[i].style.display = 'none';
    }
}

// *** initalise layout - set all to hidden *** 
var statusclass = document.getElementsByClassName("statustext");
var btnclass = document.getElementsByClassName("btn");
var selectorclass = document.getElementsByClassName("selector");
var initclass = document.getElementsByClassName("init"); 

hide(statusclass);
hide(btnclass);
hide(selectorclass);
show(initclass);

//function to pick value from tlength selector box
function tlength_submit() {
    var x = document.getElementById("tlength_selector").value;

    var hideboxes = document.getElementsByClassName("tlength");
    var showboxes = document.getElementsByClassName("mlvol");

    hide(hideboxes);
    show(showboxes);
                      
    var url = `/get_tlength/${x}`;

    //send url, including parameter, to python function
    var oReq = new XMLHttpRequest();
		oReq.open("GET", url);
		oReq.send();
}

// *** functions to get average voltage from main_program function ***
function voltavgResponse() {
    document.getElementById("voltavg_status").innerHTML = "Average voltage: " + this.responseText + "V";
    
    var showboxes = document.getElementsByClassName("results");
    show(showboxes);
}   

function updatevoltavg() {
    var httpRequest = new XMLHttpRequest();
    httpRequest.addEventListener("load", voltavgResponse);
    httpRequest.open("GET", "/main_program");
    httpRequest.send();
}

// *** main section of javascript ***
function postToChat(value) {
	var url;
	switch(value) {

   //this happens when the go button is clicked
		case 'show_led':

      var hideboxes = document.getElementsByClassName("init");
      var showboxes = document.getElementsByClassName("led");

      hide(hideboxes);
      show(showboxes);

      url = "/led_toggle";
			break;

    //this happens when the LED button 'yes' is clicked
		case 'show_tlength':

      var hideboxes = document.getElementsByClassName("led");
      var showboxes = document.getElementsByClassName("tlength");

      hide(hideboxes);
      show(showboxes);

			break;
			
	  case 'tlength_submit':
	  
	    var x = document.getElementById("tlength_selector").value;

      var hideboxes = document.getElementsByClassName("tlength");
      var showboxes = document.getElementsByClassName("mlvol");

      hide(hideboxes);
      show(showboxes);
                        
      url = `/get_tlength/${x}`;
      break;
	  
	  case 'mlvol_submit':
	  
      var x = document.getElementById("mlvol_selector").value;

      var hideboxes = document.getElementsByClassName("mlvol");
      var showboxes = document.getElementsByClassName("main");

      hide(hideboxes);
      show(showboxes);
                                                   
      url = `/get_mlvol/${x}`;
      break;

    //this happens when the go button is clicked in main_program
    case 'main_program':

      var hideboxes = document.getElementsByClassName("main");
      hide(hideboxes);
     
      updatevoltavg();
      updateTable("mlplot");
      updateTable("vplot");      

      url = "/main_program";
      break;

    //this happens when the button is clicked 'yes' in response to 'are you happy?'
    case 'results':

        var hideboxes = document.getElementsByClassName("results");
        var showboxes = document.getElementsByClassName("proceed");       

        hide(hideboxes);
        show(showboxes);
        
        break;

    //this happens if there is to be another test run
    case 'proceed':

        var hideboxes = document.getElementsByClassName("proceed");
        var showboxes = document.getElementsByClassName("mlvol");

        hide(hideboxes);
        show(showboxes);

        break;

    //this happens when the program ends
		case 'end_program':
      var hideboxes = document.getElementsByClassName("proceed");           

      hide(hideboxes);

      document.getElementById("final_output").style.display = "block";     
      break;

    //this happens when there is some sort of error
		case 'error':

      var hideboxes1 = document.getElementsByClassName("led");
      var hideboxes2 = document.getElementsByClassName("results");
      hide(hideboxes1);
      hide(hideboxes2); 

	    document.getElementById("error_status").style.display = "block";  
			document.getElementById("error_status").innerHTML = "Error. Please check your connections and restart the program! You can do this by refreshing the page."; 

			break;
	}
					
	if (url) {
		var oReq = new XMLHttpRequest();
		oReq.open("GET", url);
		oReq.send();
	}
	
}
