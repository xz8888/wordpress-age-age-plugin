(function($, window, document, undefined){
  $(function(){   

    var $carouselItems = $('.pagecarousel-panel'),
        $carousel = $carouselItems.parent(),
        defaultHeight = $carousel.outerHeight();
    
    // Apply numerated classes to the panels, because nth-child selectors aint cutting it
    $carouselItems.each(function(i){
      $(this).addClass('position'+(i+1));
    });
    
    // Activate the first panel
    $carouselItems.first().addClass('active');
    
    // Set up click events to show carousel items
    window.raPageCarousel = [];
    
    $('li.pagecarousel-thumb a').each(function(i){
      var $this = $(this),
          $parentLi = $this.parent(),
          $siblingLis = $parentLi.siblings('li'),
          pageFuncs = {};
          
      $this.data('raPageCarouselIndex',i);
          
      // Determine target;
      if ($this.data('target') != '') {
        var targetSelector = $this.data('target'),
            $target = $(targetSelector);
      } else {
        var $target = $carouselItems.eq(i);
      }
      
      // Define function for activating the respective pagecarousel page
      pageFuncs.activatePage = function() {
        $siblingLis.removeClass('active');
        $parentLi.addClass('active');
        $carouselItems.removeClass('active').removeClass('beforeActive').removeClass('afterActive');
        $target.addClass('active');
        $target.prevAll('.pagecarousel-panel').addClass('beforeActive');
        $target.nextAll('.pagecarousel-panel').addClass('afterActive');
        
        // resize carousel for carousel children that have greater height than the carousel-height
        function smartResize(){
          if ( $carousel.height() <= $target.outerHeight() ) {
          	$carousel.height( $target.outerHeight() );
          }
          else {
          	$carousel.height( defaultHeight );
          }
        }
        smartResize();
        $(window).unbind('resize').resize(smartResize);
      }
      // Define function for changing URL
      pageFuncs.setUrl = function(){
        if (typeof window.raURL != 'undefined') {
          window.raURL.setUrl($this.attr('href'));
        }
      }
      // On click, do both URL change and page change
      $this.add( $this.parent('li') ).click(function(e){
        e.preventDefault();
        pageFuncs.setUrl();
        
        // Only activate page on click if the browser supports pushstate
        if ('replaceState' in history) {
          pageFuncs.activatePage();
        }
      });
      
      // Apply this page's functions to the global raPageCarousel container
      window.raPageCarousel.push(pageFuncs);
    });
  });
})(jQuery, this, this.document);
