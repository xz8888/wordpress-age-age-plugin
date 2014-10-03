(function($, window, document, undefined){
	$(function(){
		// Carousel
        var $carouselDiv = $('#carousel'),
            $panels = $carouselDiv.find('.slide-panel'),
            $panelsContainer = $carouselDiv.find('.slides'),
            $thumbsDiv = $carouselDiv.find('div.thumbs');
            
        // Hide all but first panel
        $panels.first().addClass('active');
        
        // Set up the thumbs div
        $thumbsDiv.append('<div id="carousel-indicator" class="position0"></div><ul></ul>');
        var $thumbsUl = $thumbsDiv.find('ul').first(),
            $thumbsIndicator = $thumbsDiv.find('#carousel-indicator');
        $panels.each(function(){
            if ($(this).data('thumb')) {
                var thumb = $(this).data('thumb');
                $thumbsUl.append('<li style="background-image: url('+thumb+');">&nbsp;</li>');
            }
        });
        
        // IE conditional behavior: set up default margins for animation
        if (typeof IE == 'function') {
            IE().under(10).exec(function(){
                $panels.first().css('margin-left', '0px');
            });                            
        }
        
        // Set up click actions for the thumbs
        $thumbsUl.find('li').each(function(i){
            $(this).click(function(){
                if ($(this).hasClass('active')) {
                    return;
                }
                var $targetPanel = $panels.removeClass('active').eq(i);
                
                stopVideoIfPlaying();

                $thumbsIndicator.removeClass().addClass('position'+i);
                $thumbsUl.find('li.active').removeClass('active');
                $(this).addClass('active');
                $panels.removeClass('active');
                $targetPanel.addClass('next');
                setTimeout(function(){ 
                    $panels.removeClass('next');
                    $targetPanel.addClass('active');
                    //$panelsContainer.height($targetPanel.outerHeight());
                    
                    // Dynamically size the carousel div only if this is an iPhone (or iPod Touch)
                    if (window.iPhone() && $(window).width() < 700) {
                      var activeHeight = $panelsContainer.children('.active').children().outerHeight(true);
                      $panelsContainer.css('min-height', '0').height(activeHeight + 10)
                    }
                    
                    // IE conditional behavior: Animate divs with JS instead of CSS
                    if (typeof IE == 'function') {
                        IE().under(10).exec(function(){
                            //$panels.stop(false, true);
                            $panels.not('.active').animate({ marginLeft: -940 }, 500);
                            $targetPanel.css('margin-left', '940px').animate({ marginLeft: 0 }, 500);
                        });                            
                    }
                }, 50);
            });
        }).first().addClass('active');
        
        window.carouselNext = function(){
            var $thumbs = $('#carousel').find('.thumbs li'),
                $activeThumb = $thumbs.filter('.active');
            
            if ($activeThumb.next('li').length > 0) {
                var $next = $activeThumb.next('li');
            } else {
                var $next = $thumbs.first();
            }
            
            $next.click();
        };
        window.carouselPrev = function(){
            var $thumbs = $('#carousel').find('.thumbs li'),
                $activeThumb = $thumbs.filter('.active');
            
            if ($activeThumb.prev('li').length > 0) {
                var $next = $activeThumb.prev('li');
            } else {
                var $next = $thumbs.last();
            }
            
            $next.click();
        }
        
        stopVideoIfPlaying = function() {
        	var $panels = $('#carousel .slide-panel'),
            	$videoDiv = $panels.find('.casestudy-video'),
            	$video = $videoDiv.find('video.vjs-playing');
          
        	if ($video) {
	            var videoPlayer = VideoJS.setup( $video.attr('id') );
	            if (videoPlayer && videoPlayer instanceof JRClass)
	            	videoPlayer.pause();
        	}
        	
        	$panels.removeClass('showVideo');
            var $videoDivChildren = $videoDiv.children('.video-content');
            if ($videoDivChildren) {
            	$videoDivChildren.html('');
            }
        }
    
        /*
$('#carousel').find('.slides').swipe({
            swipeLeft: carouselNext,
            swipeRight: carouselPrev,
            allowPageScroll: 'vertical'
        });
*/

		
	});
})(jQuery, this, this.document);
