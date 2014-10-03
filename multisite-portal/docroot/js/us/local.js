var globalNetwork = {
    locationLauncher: $("#global-locations"),
    mapContainer: $(".isobar-map-container"),
    init: function() {
        globalNetwork.locationLauncher.live("click", function(e){
        	e.preventDefault();
            var contactList = $("#global-contact-list");
			var trayHeight = globalNetwork.mapContainer.height() + contactList.height();
            contactList.show();
            $(this).hide();
            globalNetwork.mapContainer.height(trayHeight);
            
        });
        
        var expandButtons = $('#network #global-contact-list a.expand-button-link');
        expandButtons.live("click", function(e) {
        	e.preventDefault();
        	
        	var $sprite = $(this).find('.expand-button');
        	
		    var $expandRegion = $(this).siblings('.region-column');
            var $contactList = $("#global-contact-list");
            var oldHeight = $contactList.height();
            
		    if ( $expandRegion ) {
		        if ( $expandRegion.is(':visible') ) {
		            $expandRegion.hide();
		            $sprite.removeClass('collapse');
		        }
		        else {
		            $expandRegion.show();
		            $sprite.addClass('collapse');
		        }
		    }
		    
            var newHeight = $contactList.height();
			var trayHeight = globalNetwork.mapContainer.height() + ( newHeight - oldHeight );
            globalNetwork.mapContainer.height(trayHeight);
        });
    }
}
window.iPhone = function() {
  return (navigator.userAgent.toLowerCase().indexOf("iphone") || navigator.userAgent.toLowerCase().indexOf("ipod")) > 0;
}
globalNetwork.init();

$(document).ready(function(){  
	if (typeof VideoJS == "undefined") {
		return;
	}
	var videoElementsOnPage = VideoJS.getVideoJSTags();
	
	//attach video play functionality to "watch/play video" links
	$('.play-video').each(function(i) {
		$(this).click(function(e) {
			e.preventDefault();
			
			if (videoElementsOnPage.length >= i) {
				var videoPlayer = videoElementsOnPage[i];
				if (videoPlayer instanceof VideoJS)
					videoPlayer.play();
			}
	    });
	});
});


$(function(){
    
  var $legal = $($('section.legal a')[0]);
  if($legal.attr('href') == '/en/contact/'){
      $legal.attr('href', '/en/contact/global/');
  }

	if ($('figure.video-js-box').length > 0) {
   setTimeout(function(){
    var slidefillPlayer = VideoJS.setup('video-1'),
        $video = $('figure.video-js-box').find('video'),  
        $videoContainer = $('figure.video-js-box'),
        $videoControls = $video.siblings('.vjs-controls');
    
    // Create hide function, because we'll need it
    var putBackThisVideo = function(){
      $videoContainer.prependTo('.isobar-video-header:first li.container-pagination.isobar-span');
    }
    // Create function for window-bound escape key handler
    var escKeyBinding = function(e){
      if(e.keyCode === 27) {
        putBackThisVideo();
        $(document).unbind('keyup',escKeyBinding)
      }
    }
      
    $videoControls.find('.vjs-fullscreen-control').click(function(e) {
      var isFullScreen = $(this).parents('.video-js-box-inner').is('.vjs-fullscreen'),
          isPaused = $(this).parents('.video-js-box-inner').is('.vjs-paused');
        
      if (isFullScreen) {
        // Move the video to the top of the <body> tag so it cant be clipped by parents
        $videoContainer.prependTo('body');
        
        // Bind hide event to esc key
        $(document).keyup(escKeyBinding);
        
      } else {
        // Put it back
        putBackThisVideo();
      }
      // The above action will pause the video. Resume it automatically if the video was playing before.
      if (!isPaused) {
        slidefillPlayer.play();
      }
    });
    }, 1000);
  
  // Video.js is just too awful in IE8. Kill it.
    IE(8).exec(function(){
      $('script[src*="video.js"]').remove();
    });
  }
});

