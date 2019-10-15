$(function(){
    var admSeclector = '.admonition',
        keywordSelector = '.admonition .admonition-title'
        $admonitions = $(admSeclector),
        $keywords = $(keywordSelector);

    $keywords.each(function(index,ele) {
        $(ele).on('click', ()=>{
            if( ele.parentElement.hasAttribute('active') ){
                ele.parentElement.removeAttribute('active');
            }
            else {
                ele.parentElement.setAttribute('active', 'true');
            }
         });
    });
});