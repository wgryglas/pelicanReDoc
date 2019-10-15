$(function(){
    var pagePositon = 0,
        sectionsSeclector = '.section h2, .entry-title',
        $scrollItems = $(sectionsSeclector),
        offsetTolorence = 30,
        pageMaxPosition = $scrollItems.length - 1;

    //Map the sections:
    $scrollItems.each(function(index,ele) { $(ele).attr("debog",index).data("pos",index); });

    // Bind to scroll
    $(window).bind('scroll',upPos);

    //Move on click:
    $('button.scrolling').click(function(e){
        console.log('clicked')
        if ($(this).hasClass('next') && pagePositon+1 <= pageMaxPosition) {
            pagePositon++;
            $('html, body').stop().animate({
                  scrollTop: $scrollItems.eq(pagePositon).offset().top
            }, 300);
        }
        if ($(this).hasClass('previous') && pagePositon-1 >= 0) {
            pagePositon--;
            $('html, body').stop().animate({
                  scrollTop: $scrollItems.eq(pagePositon).offset().top
              }, 300);
            return false;
        }
    });

    //Update position func:
    function upPos(){
       var fromTop = $(this).scrollTop();
       var $cur = null;
        $scrollItems.each(function(index,ele){
            if ($(ele).offset().top < fromTop + offsetTolorence) $cur = $(ele);
        });
       if ($cur != null && pagePositon != $cur.data('pos')) {
           pagePositon = $cur.data('pos');
       }
    }

});