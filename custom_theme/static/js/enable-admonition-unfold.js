$(function(){
    var admSeclector = 'div.admonition',
        keywordSelector = '.admonition .admonition-title'
        $admonitions = $(admSeclector),
        $keywords = $(keywordSelector);

    $keywords.each(function(index,ele) {
        $(ele).on('click', ()=>{
            var p = ele.parentElement
            if( p.hasAttribute('active') ){
                p.removeAttribute('active');
            }
            else {
                p.setAttribute('active', 'true');
            }
         });
    });

//    $admonitions.each(function(index, ele) {
//        $(ele).on('click', ()=>{
//            if( ! ele.hasAttribute('active')) {
//                ele.setAttribute('active', 'true')
//            }
//        });
//    });

});