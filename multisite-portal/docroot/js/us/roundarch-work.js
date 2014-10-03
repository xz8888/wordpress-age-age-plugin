(function($, window, document, undefined){
  $(function(){
  	// URL handling
    window.raURL = new raURLinstance({
      0: function(){
        $(function(){ 
          var raPageIndex = $('li.pagecarousel-thumb a[href$="/work/"]').data('raPageCarouselIndex');
          if (raPageIndex != undefined) {
            window.raPageCarousel[raPageIndex].activatePage();        
          }
        });
      },
      clients: function(){
        $(function(){ 
          var raPageIndex = $('li.pagecarousel-thumb a[href$="/work/clients/"]').data('raPageCarouselIndex');
          window.raPageCarousel[raPageIndex].activatePage();        
        });
      },
      casestudy: function(){
        $(function(){
        	var subslug = raURL.urlSegments().subslug
          if (subslug != null) {
            subslug = subslug.toLowerCase();
            $('a[data-slug="'+subslug+'"]').click();
          }
          var raPageIndex = $('li.pagecarousel-thumb a[href$="/work/"]').data('raPageCarouselIndex');
          if (raPageIndex != undefined) {
            window.raPageCarousel[raPageIndex].activatePage();        
          }
        });
      }
    });

  	
  });
  
  function setUpSlideshow() {
    var $csSlideshowContainer = $('.slidefill.active .case-study-slideshow'),
        $csSlides = $csSlideshowContainer.children('img'),
        csSlideCount = $csSlides.length,
        counterItem = '<span class="inactive">&#9679;</span>',
        counterItemActive = '<span class="active">&#9679;</span>',
        autoPlay = true,
        autoPlaySeconds = 5,
        pauseOnHover = false;
        
    // Give up if there is no slideshow
    if ($csSlideshowContainer.length == 0) {
      return;
    }
        
    // Remove counter div if it already exists
    $csSlideshowContainer.children('.counter').remove();

    // Figure out the tallest/widest image and size the div accordingly
    var smartSizeSlideshow = function(){ 
      var  tallest = 0,
          widest = 0;
      $csSlides.each(function(i){ 
        var $this = $(this);
        if ($this.height() > tallest) { 
          tallest = $this.height(); 
        }
        if ($this.width() > widest) {
          widest = $this.width();
        }
      }).first().addClass('active'); // Make the first one active
      
      $csSlideshowContainer.height(tallest).width(widest);
    }
    smartSizeSlideshow();
    $(window).resize(smartSizeSlideshow);
    $csSlideshowContainer.prepend('<div class="counter"></div>'); // Add the counter div
    
    var $csSlideshowCounter = $csSlideshowContainer.children('.counter'),
        setCounter = function() {
          // Function to populate the counter div with the appropriate # of bullets
          var $active = $csSlides.filter('.next');
          if ($active.length == 0) {
            $active = $csSlides.filter('.active');
          }
          if ($active.length == 0) {
            $active = $csSlides.eq(0);
          }
          var before = $active.prevAll('img').length,
              after = $active.nextAll('img').length;
          
          $csSlideshowCounter.html( new Array(before+1).join(counterItem) + counterItemActive + new Array(after+1).join(counterItem) );
          
          // Create click events to jump to a specific image
          $csSlideshowCounter.find('span.inactive').css('cursor', 'pointer').click(function(){ 
            // Determine which was clicked
            var $this = $(this),
                before = $this.prevAll('span').length;
                
            // Activate respective slide
            $csSlides.removeClass('active next').eq(before).addClass('active');
            setCounter();
          });
        }
    if (csSlideCount > 1) {
    	setCounter();
    }
    
    // Create function to switch to the next slide
    window.nextSlide = function(){
      var $active = $csSlides.filter('.active'),
          $next = ($active.next('img').length > 0)? $active.next('img'):$active.prevAll('img').last(); // If the currently active image has no .next(), it must be the last, so loop back to the first
      
      $next.addClass('next');
      setCounter();
      $active.fadeOut(600, function(){
        $active.removeClass('active');
        $next.addClass('active');
        $csSlides.show().removeClass('next');
        
      });
    }
    if (autoPlay && csSlideCount > 1) {
      var initiateAutoPlay = function(){ 
        window.slideInterval = setInterval(window.nextSlide, autoPlaySeconds * 1000);
      };
      var pauseAutoPlay = function(){
        clearInterval(window.slideInterval);
      }
      // Pause interval when hovering over container
      if (pauseOnHover) {
        $csSlideshowContainer.hover( pauseAutoPlay, initiateAutoPlay);
      }
      initiateAutoPlay();
    }
  }
  
  function setUpSlideFill() {
    var $slidefill = $('.slidefill'),
        $slidefillContent = $slidefill.find('.slidefill-content'),
        $slidefillParent = $slidefill.parents('.slidefill-parent');
    
    // Click events for case studies
    $('.case-studies article a').click(function(e){
      // Abort if the animation is still going
      if ($slidefill.hasClass('showing') || $slidefill.hasClass('hiding')) {
        return false;
      }
      
      // Change the address bar URL to this case study's direct link
      if ('replaceState' in history) {
        history.replaceState(false, '', $(this).attr('href'));
      }
      
      // Populate the slidefill div with this case study's details
      var $caseStudyDetails = $(this).parents('li').find('.case-study-details'),
          caseStudyContent = $caseStudyDetails.html();
          $slidefillContent.html(caseStudyContent);
          $caseStudyDetails = $slidefillContent;
          
      // Get case study name to add to title
      var caseStudyName = $slidefillContent.find('.case-study-body h1').html().match(/([^<]+)/ig)[0].replace(/[\s]{2,}/ig,'');
      if (caseStudyName != '') {
        window.oldTitle = document.title;
        document.title = 'Roundarch Isobar: ' + caseStudyName;
      }
      
      //Activate social share buttons
      Isobar.attachAjaxSocial();

      // In IE8, populate the <object>'s params manually
      IE(8).exec(function(){
        var $video = $caseStudyDetails.find('object'),
            $videoClone = $video.clone(),
            $videoDiv = $('.slidefill.active .case-study-videobox');
        window.videoClone = $videoClone;
        
        setTimeout(function(){
          $('.slidefill.active .case-study-videobox').empty().append(window.videoClone)
        }, 600);
      });
      
      // If this slidefill contains a slideshow, set that up
      if  ($slidefillContent.find('.case-study-slideshow').length > 0) {
        $slidefillContent.find('.case-study-slideshow').find('img').last().load(setUpSlideshow);
      }
            
      
      // Position the slidefill to the corner where the clicked item is
      var pos = $(this).parents('li').position();
      if (pos.left > ($slidefillParent.width() - 20) * 0.499) {
        $slidefill.css({
          right: 0,
          left: 'auto'  
        });
      } else {
        $slidefill.css({
          right: 'auto',
          left: 0  
        });
      }
    
      if (pos.top >= ($slidefillParent.height()) * 0.5) {
        $slidefill.css({
          bottom: '0px',
          top: 'auto'  
        });
      } else {
        $slidefill.css({
          bottom: 'auto',
          top: 0  
        });
      }
      
      // Activate slidefill
      $slidefill.slideFill('show', false);
      e.preventDefault();
      
      // If this slidefill contains a video, set up fullscreen helpers
      if ($('#casestudy-slidefill-video').length > 0) {
        var slidefillPlayer = VideoJS.setup('casestudy-slidefill-video'),
            $video = $('#casestudy-slidefill-video'),  
            $videoContainer = $('.slidefill .case-study-videobox'),
            $videoControls = $video.siblings('.vjs-controls');
            
        // Create hide function, because we'll need it
        var putBackThisVideo = function(){
          $videoContainer.prependTo('.slidefill .slidefill-content');
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
            putBackThisVideo()
          }
          // The above action will pause the video. Resume it automatically if the video was playing before.
          if (!isPaused) {
            slidefillPlayer.play();
          }
        });
      }
      
	  // if this slidefill has a facebook like button, update it with the correct URL:
	  // the current code in global.js applies the same URL to all facebook buttons on the page,
	  // this is a problem for the work-isobar page where each "slidefill" item needs to have it's own URL
	  var $fbSlidefillButton = $slidefillContent.find('.share-box');
		if ($fbSlidefillButton.length) {
			// URL code extracted from global.js
			var fburl = $fbSlidefillButton.data('fb-url');
			var fbFull = '//www.facebook.com/plugins/like.php?href='+fburl+'&send=false&layout=button_count&width=100&show_faces=false&action=like&colorscheme=light&font&height=21'
			$fbSlidefillButton.find('.share-facebook').attr('src',fbFull);
		}

    });
    
    // Slidefill-close button hides slidefill
    $slidefill.find('.slidefill-close').click(function(){
      if (window.oldTitle != undefined) {
        document.title = window.oldTitle;
      }
      var cleanUrl = raURL.cleanUrl();
      
      if ('replaceState' in history) {
        history.replaceState(false, '', cleanUrl);
      } else if (raURL.urlSegments().subslug != null) {
        /*
           If the browser doesn't support replacestate but there is a subslug, it must mean the user 
           came here from a direct link. In that case, when they click the close button it should take
           them to the /work/ homepage. Otherwise, the case study direct URL will stay in their browser
           address bar throughout the page, which would be yucky badtimes.
        */
        window.location = cleanUrl;
      }
      $slidefill.slideFill('hide');
      
      // Clear the content of the slidefill div (this will kill any playing video to prevent hearing it in the bg)
      $slidefillContent.empty();
      
      // Size the pagecarousel
      setTimeout(function(){
        var tempHeight = $('#work-casestudies').outerHeight(), tempPerform = $('.work-carousel').height(tempHeight);
      }, 500);
    });
    
  }
  
  function attachShowMoreClients() {
  
	 $("#showMoreClients").click(function(){
      
      var client_container = $(".clients_container");
      var pagecarousel = $('#pagecarousel');
      
      if($(this).text() == "See More Clients"){
        client_container.show();
        var raPageIndex = $('li.pagecarousel-thumb a[href$="/work/clients/"]').data('raPageCarouselIndex');
        window.raPageCarousel[raPageIndex].activatePage();
	      $(this).text("See Less Clients");
      }
      else{
        client_container.hide();
        var raPageIndex = $('li.pagecarousel-thumb a[href$="/work/clients/"]').data('raPageCarouselIndex');
        window.raPageCarousel[raPageIndex].activatePage();
        $(this).text("See More Clients");
      }
	
    });
  }
  
  function attachShowMoreWork() {
	  $('#showMoreWorkLink').click(function(e) {
	  	e.preventDefault();
	  	
	  	var hiddenItems = $('.hidden-work-item').slice(0, 6);
	  	var pagecarousel = $('#pagecarousel');
      var link = $('.seeMoreWork');
	  	if (hiddenItems) {
        var wwidth = $(window).width()
        var heightOfNewItems;
	  		// get the height of new items by grabbing the height of the first item (all items have the same height)
	  		// and multiplying it by either 1 or 2 (1 to 3 items = 1 row of items, 4 to 6 = 2 rows to add)
	  	  
        if(wwidth > 1000){
    	    heightOfNewItems = hiddenItems.eq(0).height() * Math.ceil(hiddenItems.length / 3 /* items in a row */);
        }
        else if(wwidth < 1000 && wwidth > 765){
          heightOfNewItems = hiddenItems.eq(0).height() * Math.ceil(hiddenItems.length / 2);
        }
        else{
          heightOfNewItems = hiddenItems.eq(0).height() * Math.ceil(hiddenItems.length);
        }

        pagecarousel.height( pagecarousel.height() + heightOfNewItems + link.height());
        hiddenItems.removeClass('hidden-work-item').show();

      }
	  	if ( $('.hidden-work-item').length == 0 ) {
            pagecarousel.height(pagecarousel.height() - link.height());
	          $(this).parent().hide();
	  	}
	  });
  }
  
  $(document).ready(function() {
	  setUpSlideFill();
	  attachShowMoreClients();
	  attachShowMoreWork();
  });
      
  // Apply functions to global scope
  if (!window.ISOBAR) {
	  window.ISOBAR = {};
  }
  window.ISOBAR.setUpSlideFill = setUpSlideFill;
  window.ISOBAR.attachShowMoreClients = attachShowMoreClients;
  window.ISOBAR.attachShowMoreWork = attachShowMoreWork;
  
})(jQuery, this, this.document);
