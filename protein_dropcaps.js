var head = document.head || document.getElementsByTagName('head')[0]
var style = document.createElement('style');
style.type = 'text/css';
var css=".drop-LETTER{float: left;\
         font-size: .1px;\
         background: url('Alphabet_ray/LETTER.png') no-repeat;\
         background-size: 45px;\
         padding: 40px 0 0 40px;\
         margin-right: 9px;}";

var c=document.body.children;
var drop=true;
for (var i=0; i<c.length; i++) {
    if (document.body.children[i].nodeName == 'H1') drop=true;
    if (document.body.children[i].nodeName == 'P' && drop) {
        var letter=document.body.children[i].innerText[0].toUpperCase();
        document.body.children[i].innerHTML='<span class=drop-{L}></span>'.replace('{L}',letter)+document.body.children[i].innerHTML.slice(1);
        console.log(css.replace(/LETTER/g,letter));
        style.appendChild(document.createTextNode(css.replace(/LETTER/g,letter)));
        document.body.children[i].classList.add("dropcap-"+letter);
        drop=false;
        }
}
head.appendChild(style);