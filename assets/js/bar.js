var bar1 = $('._bar._ba1');
var bar2 = $('._bar._ba2');
var bar3 = $('._bar._ba3');
var bar1_htmlFrag = '<img src ="assets/img/info.svg" width="60" height="25" >'
var bar2_htmlFrag = '<img src ="assets/img/work.svg" width="60" height="25" >'
var bar3_htmlFrag = '<img src ="assets/img/contact.svg" width="60" height="25" >'
bar1.html(bar1_htmlFrag);
bar2.html(bar2_htmlFrag);
bar3.html(bar3_htmlFrag);


$('._747451-toolItem._intro').click(function(){
    document.location.href="https://www.facebook.com/garnix.ju";
});

$('._747451-toolItem._work').click(function(){
    document.location.href="http://nlp-ultron.cs.nthu.edu.tw:9596/#present";
});

$('._747451-toolItem._contact').click(function(){
    document.location.href="http://www.nlplab.cc/";
});