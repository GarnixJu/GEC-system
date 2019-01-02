//var bar1 = $('._bar._ba1');
var bar2 = $('._bar._ba2');
var bar3 = $('._bar._ba3');
var bar4 = $('._bar._ba4');
var bar5 = $('._bar._ba5');


const submitBtn = $(".submit-btn");
submitBtn.on('click', submitQuery);

//var bar1_htmlFrag = '<img src ="static/img/info.svg" width="60" height="25" >';
var bar2_htmlFrag = '<img src ="static/img/work.svg" width="60" height="25" >';
var bar3_htmlFrag = '<img src ="static/img/contact.svg" width="60" height="25" >';
var bar4_htmlFrag = '<img src ="static/img/Linggle.svg" width="60" height="25" >';
var bar5_htmlFrag = '<img src ="static/img/Writeahead.svg" width="60" height="25" >';

//bar1.html(bar1_htmlFrag);
bar2.html(bar2_htmlFrag);
bar3.html(bar3_htmlFrag);
bar4.html(bar4_htmlFrag);
bar5.html(bar5_htmlFrag);


function submitQuery(){
    var text = $('#textarea').val();
    // console.log(text);
    // send to server and process response
    document.getElementById("bar2_colr").style.background = "#323439";

    gec_it_post(text);
    // score_it_post(text);
    $( "#show-box" ).css( 'border', 'solid 0.01em rgb(204, 230, 245)');
}


var delay = (function(){
    var timer = 0;
    return function(callback, ms){
      clearTimeout (timer);
      timer = setTimeout(callback, ms);
    };
  })();


$( "#textarea" ).on("keyup", function(e){
    //var flag = true;
    if(event.keyCode == 13) {
        var flag =true;
        submitBtn.click();
        //submitQuery();
    }
});



$( "#textarea" ).keyup(function(){
    delay(function(){
        document.getElementById("bar2_colr").style.background="#790b1c";        
      }, 4000);
});


function gec_it_post(query){
    $("#suggestion-area").html('<span class="small">批改中...</span>');
    $.ajax({
        type: "POST",
        url: API_URL,
        data: JSON.stringify({text: query}),
        dataType: 'json',
        success: function (data) {
            // console.log("success")
            
            var content = data.word_diff
                .replace(/\[-(.*?)-\]/g, '<span class="deletion">$1</span>')
                .replace(/\{\+(.+?)\+\}/g, '<span class="correction">$1</span>')
                .replace(/(\r\n|\n)/g, "<br>");
            console.log(content);
            content += '<br><span class="small warning">很抱歉，本系統僅能偵測出部分錯誤 T_T</span>';
                
            document.getElementById("suggestion-area").innerHTML = content;
        }, 
        error: function(XMLHttpRequest, textStatus, errorThrown) { 
            console.log("Status: " + textStatus); 
            console.log("Error: " + errorThrown); 
        }
    });
}


function score_it_post(text){
    // document.getElementById("show-box").textContent = "result:"+query;
    $.ajax({
        type: "POST",
        url: "http://thor.nlplab.cc:7777/aes",
        data: JSON.stringify({courpus: text}),
        dataType: 'text',
        success: function (data) {
            console.log(data);
            $(".score").text(data);
        }, 
        error: function(XMLHttpRequest, textStatus, errorThrown) { 
            console.log("Status: " + textStatus); 
            console.log("Error: " + errorThrown); 
        }
    });
}
