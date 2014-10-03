$(function(){
  $('.home-news').masonry({ 
  	isAnimated: IE(6,7,8).pipe(false, true), // Returns false in IE6-8, false in any other browser
  	columnWidth: function(conW){
    	if (conW < 400) return 140;
    	if (conW < 900) return 170;
    	return 150;
    }, 
  	gutterWidth: 10
	});
	
	$('.home-news .slidefill-parent').hover(function() { 
	 $(this).siblings('.slidefill-parent').find('.slidefill.active').slideFill('hide'); 
	 $(this).find('.slidefill').slideFill('show', true); 
  }, function(){ 
    $(this).find('.slidefill').slideFill('hide'); 
  });
  
  // Direct link to case studies by clicking title or paragraph
  $('div[data-href]').each(function(){
    var $target = $(this).children('p'),
        thref = $(this).data('href');
    $target.click(function(){
      window.location = thref;
    }).css('cursor', 'pointer');
  });
  
  
  var $carousel = $('#carousel'),
      $carouselOuter = $('#carousel-outer'),
      $panels = $carousel.find('.slide-panel') ;
      
  // Show the video inline when you click the link    
  $carousel.find('a.play-video').click(function(e){
    e.preventDefault();
    
    // If video is already playing, don't do anything.
    if ($panels.hasClass('showVideo')) {
      return;
    }
    
    var $this = $(this),
        $parentPanel = $this.parents('.slide-panel'),
        $videoDiv = $this.siblings('.casestudy-video');
       
        
    $panels.removeClass('showVideo');
    $parentPanel.addClass('showVideo');
    $videoDiv.children('.video-content').html($videoDiv.children('.hidden').html());
    
    var  $video = $videoDiv.find('video');
    
    
    //if (IE(6,7,8).pipe(false, true) == true) {
      var player = VideoJS.setup( $video.attr('id') );
      if (player && player instanceof VideoJS) {
    	 player.play();
    	}
    	// possibly temporary: positioning issues in panel?
        var $videoControls = $videoDiv.find('div.vjs-controls');
    	$videoControls.css({ position: "relative", display: "block" });
    	$videoControls.css('margin-top', -parseInt( $video.css('margin-top') ));
    //}
    
    // Set up fullscreen helpers
    var $videoControls = $videoDiv.find('.vjs-controls'),
        $videoDivContent = $videoDiv.children('.video-content');
    
    // Create hide function, because we'll need it
    var putBackThisVideo = function(){
      $videoDivContent.prependTo($videoDiv);
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
        $videoDivContent.prependTo('body');
        
        // Bind hide event to esc key
        $(document).keyup(escKeyBinding);
      } else {
        // Put it back
        putBackThisVideo();
      }
      // The above action will pause the video. Resume it automatically if the video was playing before.
      if (!isPaused) {
        player.play();
      }
    });
    
    var $csv = $videoDiv.find('video.case-study-video');

    setTimeout(
      function(){
        if($csv.height() == 0){
          $csv.css({ height: '279px' });
        }
      }, 
    200);

    
    $videoDiv.children('.video-close').unbind('click').click(function(){     
      if (typeof player != "undefined") {
        player.pause();
      }
      $panels.removeClass('showVideo');
      $videoDiv.children('.video-content').empty();
      IE(8).exec(function(){
        $videoDiv.find('.ie8video').addClass('hidden');    
      });
    });
    return false;
  });
 
});
