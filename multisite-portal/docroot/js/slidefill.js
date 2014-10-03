jQuery.fn.slideFill = function(arg, dont100) {
    clearTimeout(window._slideFillTimeOut);
    if (this.length === 0) {
        return;
    }
    if (arg == 'show' || arg === undefined) {
        var show = true,
            hide = false;
    } else if (arg === 'hide') {
        var show = false,
            hide = true;
    }
    $(this).each(function(){
        var $obj = $(this);
       // Establish the parent. If it's inside a .slidefill-parent, use that. Otherwise, use first parent
       var $p = $obj.parents('.slidefill-parent');
       if ($p.length === 0) {
           $p = $obj.parent();
       }
       var w = $p.outerWidth(),
           h = $p.outerHeight(),
           origW = $obj.data('original-width') || $obj.width(),
           origH = $obj.data('original-height') || $obj.height();
        if ($p.hasClass('dogear-top')) {
            h += $p.find('.top').height();
        }   
        if ($p.hasClass('dogear-bottom')) {
            h += $p.find('.bottom').height();
        }
        
        if ( show && !$obj.hasClass('showing') && !$obj.hasClass('hiding') ) {
        	if (typeof VideoJS != "undefined") {
        		var video = $p.find('.slidefill-content video');
        		if (video && video.length > 0) {
        			// VideoJS needs to be passed the id of the video:
        			video.attr('id', 'casestudy-slidefill-video');
        			VideoJS.setup('casestudy-slidefill-video');
        		}
        	}
            
            $obj.data('original-width', origW).data('original-height', origH).addClass('showing');
            $obj.addClass('active').width(w).height(h).removeClass('showing');
            // Show the div
            if (dont100 == false || dont100 == undefined) {
              setTimeout(function(){
                  $obj.addClass('full').removeClass('showing');
                  $obj.css({ width: '100%', height: '100%' });
                  
                  // for work page, and any other that uses slidefill (other than home),
                  // animate to the top of the slidefill button:
                  var isHomePage = $('#casestudy-slidefill-video').parents('.home');
                  if ( !isHomePage.length )
                	  $('html, body').animate({ scrollTop: $(".slidefill-close").offset().top });
              }, 400);
            } else {
              $obj.removeClass('showing');
            }
        }
        else if ( hide && !$obj.hasClass('hiding') && !$obj.hasClass('showing') ) {
            $obj.removeClass('full').height(h).width(w);
            // The above line changes width from 100% to a fixed pixel count. webkit handles this
            // strangely with transitions, so we have to wait a few ms for the change to register
            // before starting the resize stuff, otherwise it will instantly snap to origW
            setTimeout(function(){
                $obj.width(origW).height(origH).addClass('hiding');
                if (dont100 == false || dont100 == undefined) {
                  setTimeout(function(){
                      $obj.removeClass('active').removeClass('hiding');
                  },400);
                } else {
                  $obj.removeClass('active').removeClass('hiding');
                }
            }, 3);
        }
    
    });
};
