$(document).ready(function(){
  
  // URL handling
  window.raURL = new raURLinstance({
    0: function(){
      window.raPageCarousel[0].activatePage();
      setTimeout(window.raPageCarousel[0].activatePage, 1200);
      return;
    },
    services: function(){
      $(function(){ 
        var raPageIndex = $('li.pagecarousel-thumb a[href$="/about/services/"]').data('raPageCarouselIndex');
        window.raPageCarousel[raPageIndex].activatePage();
      });
    },
    partners: function(){
      $(function(){ 
        var raPageIndex = $('li.pagecarousel-thumb a[href$="/about/partners/"]').data('raPageCarouselIndex');
        window.raPageCarousel[raPageIndex].activatePage();      
      });
    }
  });
    
    /**
     * About-page profile switching:
     */
    function setProfileSummaries() {
    	if ($('div#partner-summaries')) {
    		// Set up links
    		var $partners = $('.partner-container'),
    			  $thumbs = $('img.partner-thumb');
				    $aboutLink = $('li.pagecarousel-thumb a[href$="/about/"]');
    			
    		// Show the first partner container
    		$partners.first().addClass('active');
    		$thumbs.first().addClass('active-partner-thumb');
    		
    		// Add a dynamic class to identify the # of thumbs
    		$('#partner-thumbs').addClass('totalThumbs'+$thumbs.length);
    		
    		$thumbs.each(function(i){
    			// When this thumb is clicked, show the respective container
    			$(this).click(function(){
    				$partners.removeClass('active').eq(i).addClass('active');
    				if (window.raPageCarousel) {
    				  window.raPageCarousel[0].activatePage();
    				  setTimeout(window.raPageCarousel[0].activatePage, 300);
    				}
    				$thumbs.removeClass('active-partner-thumb').addClass('inactive-partner-thumb');
    				$thumbs.removeClass('inactive-partner-thumb').eq(i).addClass('active-partner-thumb');
    				
    			});
    		});
    	}
    }

    /**
     * Set the services boxes to be the same height.
     */
    function sizeServiceContainers() {
    
    	$('.service-long-description').css({
    		display: "block"
    	});
    	
    	var currentTallest = findLargestHeight( $('.service-container .service-short-description .service, .service-container .service-long-description .service') );
    	var serviceContainers = $('.service-container .service-short-description .service, .service-container .service-long-description .service');
    	serviceContainers.css({
			height: currentTallest + 'px'
  		});
  		// the 20 pixels below account for the "dog ear" div size
  		$('.service-container .service-long-description .service').css({
  			height: (currentTallest + 20) + 'px'
  		});

    	// full-length service containers:
    	serviceContainersShort = $('.service-container-full .service-short-description');
    	serviceContainersLong  = $('.service-container-full .service-long-description');
    	if (serviceContainersLong.length > 0) {
    		serviceContainersLong.each(function(i, item){
    			var height = serviceContainersShort.eq(i).height();
    			var serviceContainer = serviceContainersLong.eq(i).find('.service');
    			// 20 is for the "dog-ear" sizing
    			serviceContainer.height( height - 20 );
    		});
    	}

    	$('.service-long-description').css('display', "");
    	
    	// In IE8 only, apply nth-child logic using JS rather than CSS selector 
    	IE(8).exec(function(){    
        $('.service-container:nth-child(4)').css({ marginRight: 0  }); 
      });
      
       /**
       * Add hover state to services panels when clicking
       */
       $('.service-container, .service-container-full').click(function(){
        $(this).toggleClass('hover');
      });
    }

    /**
     * Set the partner boxes to be the same height.
     */
    function sizePartnerContainers() {
    	$('.partner-text').css({
    		display: "block"
    	});
    	
    	var currentTallest = findLargestHeight( $('.partner-text p') );
    	if (currentTallest < 120) {
      	currentTallest = 120;
    	}
    	$('.partner').css({
  			height: (currentTallest + 15) + 'px'
  		});

    	$('.partner-text').css('display', "");
    }
    
    /**
     * Gets the largest height from a group of elements
     */
    function findLargestHeight( elements ) {
  		var currentTallest = 100;
  		if (elements) {
  			elements.each(function(i){
  				currentTallest = Math.max( $(this).height(), currentTallest );
  			});
  		}
  		return currentTallest;
    }


   

    setProfileSummaries();
    sizeServiceContainers();
    sizePartnerContainers();
    
    if ( !window.ISOBAR )
    	window.ISOBAR = {};
    
	window.ISOBAR.setProfileSummaries = setProfileSummaries;
	window.ISOBAR.sizeServiceContainers = sizeServiceContainers;
	window.ISOBAR.sizePartnerContainers = sizePartnerContainers;


});
