$(document).ready(function(){  
	var videoElementsOnPage = VideoJS.getVideoJSTags();
    
	// attach video play functionality to "watch/play video" links
    $('.play-video').each(function(i) {
    	$(this).click(function(e) {
			e.preventDefault();
			
    		if (videoElementsOnPage.length >= i) {
    			videoElementsOnPage[i].play();
    		}
        });
    });

	// attach ending "visit project" links to video when video ends as well as functionality for showing link
    /*
    VideoJS.DOMReady(function() {
	    $.each(videoElementsOnPage, function(i, video) {
	    		var link = VideoJS.createElement("div", { className: "video-end-link",
										    		      innerHTML: "<a href='#' alt='View the Project'>View the Project</a>" });
	    	    video.parentNode.appendChild(link);
	    	    
	    	    VideoJS.player.newBehavior("linkComponent", function(element){
	    	        _V_.addListener(element, "click", this.visitProject.context(this));
	    	      },{
	    	    	  visitProject: function(event){ 
	    	    		  alert("VISITING PROJECT"); 
	    	    	  }
	    	      }
	    	    );
	    	    
	    	    VideoJS.player.activateElement(link, "linkComponent");

	    	    // the following use the HTML5 video API events directly
	    	    // instead of through VideoJS, VideoJS Flash fallback will not
	    	    // show this component as a result
	        	video.player.onEnded(function() {
	        		$('.video-end-link').eq(i).css('display', 'block');
	        	});
	        	video.player.onPlay(function() {
	        		$('.video-end-link').eq(i).css('display', 'none');
	        	});
	        	video.player.onError(function() {
	        		$('.video-end-link').eq(i).css('display', 'none');
	        	});
	    });
    });
    */
});