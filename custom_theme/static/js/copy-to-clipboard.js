/*
    Adds to element with class .scalar-input possibility
    for click copy innerText
    Additionally tooltip element is appended as a child to this element
    for showing info when clicked
*/

function copyElementText(element) {
    var textToCopy = element.innerText.split('\n')[0];
    var myTemporaryInputElement = document.createElement("input");
    myTemporaryInputElement.type = "text";
    myTemporaryInputElement.value = textToCopy;
    document.body.appendChild(myTemporaryInputElement);
    myTemporaryInputElement.select();
    document.execCommand("Copy");
    document.body.removeChild(myTemporaryInputElement);
    console.log(textToCopy)
    return textToCopy
}

$(function(){
    $copyItems = $('.scalar-input')
    $copyItems.each(function(index,ele) {
        $(ele).on('click', ()=>{
            $(ele).find('.copy-tooltiptext').text('Copied '+ copyElementText(ele) )
            ele.setAttribute('active','true')
        });
        $(ele).on('mouseout', ()=>{
            $(ele).find('.copy-tooltiptext').text('Copy Input')
            ele.setAttribute('active','false')
        })
    });

    $copyItems.addClass('copy-tooltip')
    $copyItems.append('<span class="copy-tooltiptext">Copy Input</span>')
});