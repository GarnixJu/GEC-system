var bar1 = $('._bar._ba1');
var bar2 = $('._bar._ba2');
var bar3 = $('._bar._ba3');
var bar4 = $('._bar._ba4');
var bar5 = $('._bar._ba5');

var bar1_htmlFrag = '<img src ="assets/img/info.svg" width="60" height="25" >'
var bar2_htmlFrag = '<img src ="assets/img/work.svg" width="60" height="25" >'
var bar3_htmlFrag = '<img src ="assets/img/contact.svg" width="60" height="25" >'
var bar4_htmlFrag = '<img src ="assets/img/Linggle.svg" width="60" height="25" >'
var bar5_htmlFrag = '<img src ="assets/img/Writeahead.svg" width="60" height="25" >'

bar1.html(bar1_htmlFrag);
bar2.html(bar2_htmlFrag);
bar3.html(bar3_htmlFrag);
bar4.html(bar4_htmlFrag);
bar5.html(bar5_htmlFrag);


$('._747451-toolItem._intro').click(function(){
    document.location.href="https://www.facebook.com/garnix.ju";
});

$('._747451-toolItem._work').click(function(){
    document.location.href="http://nlp-ultron.cs.nthu.edu.tw:9596/#present";
});

$('._747451-toolItem._contact').click(function(){
    document.location.href="http://www.nlplab.cc/";
});

$('._747451-toolItem._Linggle').click(function(){
    document.location.href="http://linggle.com/";
});

$('._747451-toolItem._WriteAhead').click(function(){
    document.location.href="http://writeahead.nlpweb.org/more";
});