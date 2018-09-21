/*
	Dimension by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// const csrftoken = getCookie('csrftoken');
const csrftoken = $("input[name=csrfmiddlewaretoken]").val();

(function($) {
	API_URL = 'translate/';
	document.cookie = `csrftoken=${csrftoken}; path=/ `;

    // set up ajax csrf-token 
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
    // HEADERS = {'Content-Type': 'application/json; charset=UTF-8', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': '*'}

	// $( "#show-text:empty" )
	// 	.text( "Was empty!" )
	// 	.css( "background", "rgb(255,220,200)" );
	
	$( "#enterValue" ).on('input',function(e){
		var v = $('textarea#enterValue').val();
		if(v == "") {
			$( "#show-box" ).css( "border", "none" );
			document.getElementById("show-text").textContent = "";
			$( "#show-box" ).css( 'border', 'none' );
		}
	});

	skel.breakpoints({
		xlarge:		'(max-width: 1680px)',
		large:		'(max-width: 1280px)',
		medium:		'(max-width: 980px)',
		small:		'(max-width: 736px)',
		xsmall:		'(max-width: 480px)',
		xxsmall:	'(max-width: 360px)'
	});
})(jQuery);
