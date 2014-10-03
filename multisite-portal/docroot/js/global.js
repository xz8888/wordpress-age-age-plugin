var Isobar = function() {
	var touch_devices = new Array(
		'iPad',
		'iPhone'
	);

	var disabled_devices = new Array(
		'blackberry'
	)


	var isTouchDevice = isTouchDevice();
	var isDisabledDevice = isDisabledDevice();
	var ajaxOpenerActive = false;
	var ajaxContentHeight = 0;
	var ajaxContentBottomMargin = 45;
	var pageTitle = '';

	function init() {
		if (isDisabledDevice) {
			return false;
		}

		$(document.body).removeClass('no-js').addClass('js');
		pageTitle = document.title;

		attachOpenAjaxVerticalScroll();
		attachAjaxDeeplink();
		attachAjaxOpener();
		attachAjaxCarousel();
		attachShowMore();
		attachAjaxSocial();
		attachCarousel();
		attachBoxCorners();
		attachHovers();
		attachMasonry();
		attachOpener();
		attachMaps();
		attachVideoJs();
		pngFix();


		$(window).resize(function() {
			resizeAjaxContainer();
		});


	}

	/**
		Gets content url from href
		AJAXs in content
		Writes content to page, removes default controls
		Moves back button out of view
		Sets AJAX content height to zero
		Animates AJAX content height to default size
		Animates back button into view
		Initalises Video JS
		Scrolls to AJAX content
	*/
	function attachOpenAjaxVerticalScroll () {
		$('.open-ajax-vertical-scroll').live('click', function(e) {
			if (isTouchDevice) {
				return true;
			}

			e.preventDefault();

			var url = setAjaxURL(this);

			if ($('#ajax-slide-content').length > 0) {
				// Existing AJAX content in page so crossfade
				openAjaxContainer(url, 'fade');
			} else {
				openAjaxContainer(url, 'slide');
			}
		});
	}

	function attachAjaxDeeplink() {
		var hash = new String(window.location.hash);
		if (hash.length < 1 || hash.substr(0, 2) != '#!') {
			return false;
		}

		var url = getAjaxURLFromHash(window.location.hash);
		if (url == "") {
			return false;
		}
		
		openAjaxContainer(url, 'slide');
	}


	function getAjaxContentHeight() {
		return ($('#ajax-slide-content .main-content-pad').height() + Isobar.ajaxContentBottomMargin);
	}


	function resizeAjaxContainer() {
		$('#ajax-slide-content').css ( 'height', getAjaxContentHeight());
	}


	function openAjaxContainer(url, transition) {
		if (transition == 'slide') {
			$.ajax({
				url: url,
				cache: false,
				success: function(html){
					var ajaxContent = writeAjaxContent(html);
					var backLink = $('.back-link');
					attachCloseAjaxVerticalScroll();
					var backLinkHeight = backLink.height();
					moveBackButtonOffScreen(backLink,backLinkHeight);
					attachBoxCorners();
					ajaxContent.animate ( {height : 0} , 0, function() {
						ajaxContent.animate ( {height : getAjaxContentHeight()} , 750, function (){
							updatePageTitle();
							showBackButtonAndInitVideoJSAndSocial(backLink, backLinkHeight);
							scrollToAjaxContent($('.wrap-content'));
						});
					});
					
				}
			});

		} else if (transition == 'fade') {

			var backLink = $('.back-link');
			var backLinkHeight = backLink.height();
			scrollToAjaxContent($('.wrap-content'));
			hideBackButton ( backLink, backLinkHeight , function () {
				backLink.hide();
				var ajaxContent = $('#ajax-slide-content');
				var oldAjaxContentHeight = getAjaxContentHeight();

				ajaxContent.fadeOut (500, function () {
					ajaxContent.css({
						'visibility': 'hidden',
						'display': 'block'
					});
					$.ajax({
						url: url,
						cache: false,
						success: function(html){
							var ajaxContent = writeAjaxContent(html);
							var backLink = $('.back-link');
							moveBackButtonOffScreen(backLink,backLinkHeight);
							attachBoxCorners();

							var newAjaxContentHeight = getAjaxContentHeight();

							ajaxContent.fadeOut(0).css({
								'opacity': 0,
								'display': 'block'
							});

							ajaxContent.css ( 'height' , oldAjaxContentHeight );
							ajaxContent.animate ( {height : newAjaxContentHeight} , 500);

							$('#ajax-slide-content').animate ( {opacity : 1}, 500, function (){
								updatePageTitle();
								showBackButtonAndInitVideoJSAndSocial(backLink, backLinkHeight);
							});
						}
					});
				});
			});
		}//end if
	}


	function setAjaxURL(target) {
		var url = getAjaxURL(target);

		// Pull off the 'namespace' from the URL (e.g. work/, people/)
		var hashUrl = url.substring(1);
		hashUrl = hashUrl.substring(hashUrl.indexOf('/')+1);
		hashUrl = hashUrl.replace('.ajax', '');
		hashUrl += '';

		var currentHash = new String(window.location.hash);
		if (currentHash.substring(0, 3) != '#!/') {
			window.location.hash = '#!/';
		} else {
			var regex = /#!\/[0-9](.*)+/
			var currentStr = regex.exec(currentHash);
			if (currentStr != null && currentStr.length > 1) {
				var newHash = currentHash.replace(currentStr[1], '');
				window.location.hash = newHash + '/';
			} else {
				// Reset existing hash
				window.location.hash = '#!/';
			}
		}

		window.location.hash += hashUrl;

		return url;
	}

	function getAjaxURLFromHash(str) {
		path = window.location.pathname;
		// move page number
		var regex = /\/[0-9]/
		var match = regex.exec(str);
		if ( match ) {
			str = str.replace ( match, "" );
		}

		if (str == "#!") {
			return "";
		} else {
			// Pull trailing slash off URL
			path = path + str.replace('#!/', '');
			if(path.substr(-1) == '/') {
				path = path.substr(0, path.length-1);
			}
			return path + '.ajax';
		}
	}

	function getAjaxURL(target) {
		var href = getLink(target);

		if (href.indexOf('http://') != -1) {
			var regex = /http\:\/\/[^/]+\//
			var match = regex.exec(href);
			if (match) {
				href = '/' + href.replace(match, '');
			}
		}

		// Pull trailing slash off URL
		if(href.substr(href.length-1) == '/') {
			href = href.substr(0, href.length-1);
		}

		return href + '.ajax';
	}

	function getPageNumberFromString(str) {
		var regex = /\/([0-9]+)/
		var page = regex.exec(str);

		if (page.length < 1) {
			return false;
		}

		return parseInt(page[1]);
	}


	function scrollToAjaxContent(target) {
		$.scrollTo(target, 500);
	}

	function updatePageTitle() {
		document.title = $('.ajax-page-title-update').html() + ': ' + pageTitle;
	}

	function resetPageTitle() {
		document.title = pageTitle;
	}

	function showBackButtonAndInitVideoJSAndSocial(backButton, backButtonHeight) {
		backButton.delay(50).animate ( {top: "+=" + backButtonHeight + "px"}, 250, function () {
			attachVideoJs();
			attachAjaxSocial();
		}).show();
	}

	function hideBackButton(backButton, backButtonHeight, onComplete) {
		backButton.animate ( {top: "-=" + backButtonHeight + "px", height: 0}, 250, onComplete);
	}

	function moveBackButtonOffScreen(backButton, backButtonHeight) {
		backButton.css('position', 'relative').hide().animate ( {top: "-=" + backButtonHeight + "px"}, 0);
	}

	function writeAjaxContent (html) {
		$('#ajax-slide-content').remove();
		$('.wrap-content').prepend ('<div id="ajax-slide-content"></div>');
		var ajaxContent = $('#ajax-slide-content');
		ajaxContent.html(innerShiv(html));
		$('#video-1').removeAttr('controls');
		return ajaxContent;
	}

	/**
		Animates close button out of view
		Fades out AJAXed content
		Empties ajax content div
		Scrolls to top of the page
	*/
	function attachCloseAjaxVerticalScroll () {
		$('.back-link').live('click', function(e) {
			e.preventDefault();

			if (!$.support.ajax) {
				return true;
			}

			var backLink = $('.back-link');
			hideBackButton ( backLink, backLink.height() , function () {
				backLink.hide();
				var ajaxContent = $('#ajax-slide-content');
				ajaxContent.animate({height: 0}, 750, function (){
					$('#ajax-slide-content').remove();
					var regex = /\/[0-9]/
					var match = regex.exec(window.location.hash);
					var hash = "";
					if ( match ) {
						hash = "#!" + match;
					}
					resetPageTitle();
					window.location.hash = hash;
				});
			});
			$.scrollTo(0, 500);
		});
	}

	/**
	 * Functions that should be run on reinitialisation - typically when
	 * content is AJAXed in to the page.
	 */
	function reinit() {
		attachVideoJs();
		attachBoxCorners();
	}

	/**
	 * If PNGFix plugin is loaded, applies PNGfix across entire document.
	 */
	function pngFix() {
		if (typeof(jQuery.fn.pngFix) == 'function') {
			$(document).pngFix();
		}
	}

	/**
	 * Returns the rendered height of a hidden element.
	 */
	function getHiddenElementHeight(c) {
		// save current values
		var position = $(c).css('position');
		var visibility = $(c).css('visibility');
		var display = $(c).css('diplay');
		$(c).css({'position':'absolute','visibility':'hidden','display':'block'});
		var height = $(c).height();

		// reset to old values
		$(c).css('position', position);
		$(c).css('visibility', visibility);
		if ( display == null || display == '' ) {
			$(c).css('display', 'none');
		}

		return height;
	}

	function attachOpener() {
		$('.trigger').click(function(e) {
			if ( typeof(e.target) != 'undefined' && e.target.className == 'no-trigger') {
				return true;
			}

			var isPanelHidden = $(this).next('.panel').is(":hidden");
			var hasFadeList = $('ul').hasClass('fadelist');
			var time;

			if ( isPanelHidden ) {
				time = getHiddenElementHeight ($(this).next('.panel')) * 2;
				if ( hasFadeList ) {
					$('.fadeitem').each(function(index) {
						$(this).hide().fadeIn((index * 50 ) + 250);
					});
				}
			} else {
				time = $(this).next('.panel').height() * 1.5;
			}
			if ( time < 200 ) {
				time = 300;
			}
			e.preventDefault();
			$(this).toggleClass('active');

			$(this).next('.panel').stop().slideToggle(time, function(){
				if ($(this).parents('li').hasClass('scroll-to')){
					if (!$(this).prev('.trigger').hasClass('active')) {
						$.scrollTo($('body'), 500);
					} else {
						$.scrollTo($(this).parents('li'), 200);
					};
				};
			});
		});
		$('.trigger').bind('mouseover mouseout', function(){
			$(this).toggleClass('hover');
		});
	}

	/**
	 * Attaches sliding openers to links with a class of ajax-opener.
	 * Usage:
	 * <div class="trigger-container">
	 *  <a href="/url-of-content-to-load/" class="ajax-trigger">
	 *  <div class="panel">
	 *   <!-- content will be loaded in here -->
	 *  </div>
	 * </div>
	 */
	function attachAjaxOpener() {
		$('.ajax-trigger').click(function(e) {
			if (!$.support.ajax) {
				return true;
			}

			e.preventDefault();
			$(this).toggleClass('active');
			$panel = $(this).parents('.trigger-container').find('.panel');
			if ($(this).hasClass('active')) {
				// Opening
				link = getLink(this);
				var time = getHiddenElementHeight ($panel) * 2;
				attachLoading($panel, 'dark');
				$panel.stop(true, true).slideToggle(time, function() {
						$.ajax(link, {
							context: $panel,
							dataType: 'html',
							success: function(data) {
								$panel = $(this);
								if ($(this).parents('.trigger-container').find('.ajax-trigger').hasClass('active')) {
									removeLoading(400, function() {
										$panel.css({opacity:'0'});
										$panel.html(innerShiv(data)).animate({opacity: '1'}, 500);
										pngFix();
									});
								}
							}
						});
				});
			} else {
				// Closing
				var time = $('.panel').height();

				$panel.stop(true, true).slideToggle(time, function() {
					if (!$('.ajax-trigger').hasClass('active')) {
						$panel.empty();
						$panel.removeAttr('style');
					}
				});
			}
		});
	}

	/**
	 * Returns a the link attached to the HTML element; or if a rel
	 * attribute is present, returns that.
	 */
	function getLink(element) {
		link = $(element).attr('href');

		if ($(element).attr('rel') && $(element).attr('rel') != '') {
			link = $(element).attr('rel');
		}

		return link;
	}

	/**
	 * Runs AJAX loaders for content that should be overwritten by an
	 * AJAX eqivilent (for example, the random people page).
	 */
	function attachAjaxCarousel() {
		if ($('.carousel-container').length < 1) {
			return false;
		}

		var currentId = getCarouselIdFromUrl();
		if (!currentId) {
			currentId = 1;
		}

		loadCarouselPage(currentId);
	}

	function attachShowMore() {
		$('.show-more-link').click(function(e) {
			e.preventDefault();

			var url = getAjaxURL(this);
			var href = $(this).attr('href');
			pageNumber = getPageNumberFromString(href);
			var nextPageNumber = pageNumber+1;
			var nextHref = href.replace('/'+pageNumber+'/', '/'+nextPageNumber+'/');

			$.ajax({
				url: url,
				cache: false,
				success: function(html) {
					html = innerShiv(html);
					$('.show-more-content').append(html);

					// Make sure we're not sat right on the
					// bottom of the page, or else we'll
					// get a nasty stutter
					$.scrollTo('-=1');

					attachMasonry();

					$('.show-more-link').attr('href', nextHref);
				},
				error: function() {
					$('.show-more-end').show();
				}
			});
		});
	}

	/**
	 * Adds carousel event listeners to pagination controls and touchscreen
	 * gestures.
	 */
	function attachCarousel() {
		$('.carousel-next').click(function(e) {
			e.preventDefault();

			if (!$(this).hasClass('inactive')) {
				scrollCarouselNext();
			}
		});

		$('.carousel-previous').click(function(e) {
			e.preventDefault();

			if (!$(this).hasClass('inactive')) {
				scrollCarouselPrevious();
			}
		});

		$('.carousel-link').click(function(e) {
			e.preventDefault();

			var regex = /\/([0-9]+)\//
			var matches = regex.exec($(this).attr('href'));
			var id = matches[1];

			loadCarouselPage(id);
		});
	}

	/**
	 * Scrolls the carousel to the next item.
	 */
	function scrollCarouselNext() {
		var currentId = getCarouselIdFromUrl();
		var nextId = currentId+1;

		loadCarouselPage(nextId);
	}

	/**
	 * Scrolls the carousel to the previous item.
	 */
	function scrollCarouselPrevious() {
		var currentId = getCarouselIdFromUrl();
		var previousId = currentId-1;

		loadCarouselPage(previousId);
	}

	/**
	 * Loads the carousel item identified by the ID parameter. Sets the
	 * navigation cues appropriately.
	 */
	function loadCarouselPage(id) {
		url = getCarouselUrl(id);

		attachLoading('.carousel-container');

		$.ajax({
			url: url,
			dataType: 'html',
			success: function(data) {
				removeLoading(500, function() {
					$('.carousel-container').html('<div class="carousel-container-inner"></div>');
					$('.carousel-container-inner').hide().html(innerShiv(data)).fadeIn();

					reinit();
					attachMasonry();


					var hash = window.location.hash;
					var orig = "";
					if ( hash ) {
						// move page number
						var regex = /\/[0-9]/
						var match = regex.exec(hash);
						if ( match ) {
							orig = hash.replace (match, "" );
						}
						orig = orig.replace("#!", "");
					}
					window.location.hash = '!/'+id+orig;
					$('.carousel-link').removeClass('selected').eq(id-1).addClass('selected');
				});
			}
		});

		$('.carousel-previous, .carousel-next').removeClass('inactive');
		if (id <= 1) {
			$('.carousel-previous').addClass('inactive');
		}

		if (id >= $('.carousel-link').length) {
			$('.carousel-next').addClass('inactive');
		}
	}

	/**
	 * Returns the URL for the carousel page.
	 */
	function getCarouselUrl(page) {
		carouselStr = new String(CAROUSEL_URL);
		carouselStr = carouselStr.replace('/x/', '/'+page+'/');
		carouselStr = carouselStr.replace('y.ajax', Math.floor(Math.random()*10) + '.ajax');

		return carouselStr;
	}

	/**
	 * Returns the current carousel page ID from the URL.
	 */
	function getCarouselIdFromUrl() {
		var currentId = new String(window.location.hash).replace('#!/', '');
		currentId = parseInt(currentId);

		if (typeof(currentId) == 'NaN') {
			return false;
		}

		return currentId;
	}

	/*
	 * Binds masonry functionality to any element with a class of 'masonry'.
	 */
	function attachMasonry() {
		if ($('.masonry').length > 0) {
			$('.masonry').masonry({
				animate: true,
				columnWidth: 1,
				itemSelector: 'li.box',
				singleMode: false,
				resizeable: true
			});
		}
		
		if ($('.masonry-no-animate').length > 0) {
			$('.masonry-no-animate').masonry({
				animate: false,
				columnWidth: 1,
				itemSelector: 'li.box',
				singleMode: false,
				resizeable: true
			});
		}
		
		if ($('.masonry-news').length > 0) {
			$('.masonry-news').masonry({
				animate: true,
				columnWidth: 50,
				itemSelector: 'li.box',
				singleMode: false,
				resizeable: true
			});
		}
		
		if ($('.masonry-no-animate-news').length > 0) {
			$('.masonry-news').masonry({
				animate: true,
				columnWidth: 50,
				itemSelector: 'li.box',
				singleMode: false,
				resizeable: true
			});
		}
	}

	/*
	 * Binds VideoJS controls to all videos with a class of 'video-js'.
	 */
	function attachVideoJs() {
		if ($('.video-js').length > 0) {
			if (typeof(HTMLVideoElement) != 'undefined') {
				VideoJS.setupAllWhenReady({
					controlsAtStart: true,
					controlsBelow: false,
					controlsHiding: true,
					defaultVolume: 0.8,
					flashVersion: 9,
					linksHiding: true
				});
			}
		}
	}

	/**
	 * Attaches maps to page.
	 */
	function attachMaps() {
		if ($('.local-map').length < 1 || mapData[1] == '') {
			return false;
		}

		var latlng = new google.maps.LatLng(mapData[1], mapData[2]);

		var zoomLevel = mapData[0];

		var myOptions = {
			zoom: parseInt(zoomLevel),
			minZoom: 1,
			center: latlng,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			panControl: false,
			zoomControl: true,
			mapTypeControl: false,
			scaleControl: true,
			streetViewControl: true
		};

		var map = new google.maps.Map(
			document.getElementById("map"),
			myOptions
		);

		onlyAddMarker(map, agencyLocation);

		$(window).resize(function() {
			map.panTo(latlng);
		});
	}

	/**
	 * Attaches marker only to the map given an array of lat/longs.
	 */
	function onlyAddMarker(map, agencies) {

		for (var i = 0; i < agencies.length; i++) {
			var agency = agencies[i];
			var agencyLatLng = new google.maps.LatLng(agency[0], agency[1]);
			var marker = new google.maps.Marker({
				position: agencyLatLng,
				map: map,
				icon: "/static/img/icons/google-map-marker.png",
				animation: google.maps.Animation.DROP,
				zIndex: 10
			});
		}
	}

	/**
	 * Adds a loading animation in to the specified container.
	 */
	function attachLoading(cont, style) {
		if (typeof(style) == 'undefined') {
			style = 'light';
		}

		$(cont).html('<div id="loading-container" style="color:#fff;position:relative">' +
			'<img class="loading" src="'+MEDIA_URL+
			'img/icons/loading/'+style+'.gif" width="33" height="34" alt="Loading"></div>'
		);
	}

	/**
	 * Removes loading animation from page. Invokes the callback function once
	 * completed.
	 */
	function removeLoading(dur, callback) {
		if (typeof(dur) == undefined) {
			dur = 500;
		}

		if (typeof(callback) == 'undefined') {
			callback = function() {};
		}

		$('.loading').fadeOut(dur, callback);
	}

	/**
	 * Attaches the various corner styles to boxes based on their class
	 * names.
	 */

	function attachBoxFeatureCorners(){

		$('.box-feature')
			.css({'padding-bottom':'3px'})
			.parent()
				.append('<div class="br-orange-triangle-inverted"></div>');

		$('.box-feature.tl')
			.css({'padding-top':'0'})
			.parent()
				.prepend('<div class="tl-orange-triangle-inverted"></div>');

	}

	function attachBoxCorners() {

		if ($('#ajax-slide-content').length && !$('#ajax-slide-content .br-orange-triangle-inverted').length) {
			attachBoxFeatureCorners();
		} else if(!$('#ajax-slide-content').length) {
			attachBoxFeatureCorners();
		}

		$('.box-text')
			.not('.box-text-alt')
			.css({'padding-bottom':'3px'})
			.parent()
				.append('<div class="br-white-triangle-inverted"></div>');

		$('.box-text.tl')
			.not('.box-text-alt')
			.css({'padding-top':'0'})
			.parent()
				.prepend('<div class="tl-white-triangle-inverted"></div>');

		$('.box-text-alt')
			.css({'padding-bottom':'3px'})
			.parent()
				.append('<div class="br-grey-triangle-inverted"></div>');

		$('.box-text-alt.tl')
			.css({'padding-top':'0'})
			.parent()
				.prepend('<div class="tl-grey-triangle-inverted"></div>');

		$('.media-box')
			.append('<div class="br-orange-triangle"></div>');

		$('.media-box[rel]').each(function(index) {
		  var country = $(this).attr('rel');
				$(this).prepend('<div class="tl-orange-triangle">'+country+'</div>');
		});
	}

	/**
	 * Attaches rollover animation to small navigation boxes.
	 */
	function attachHovers() {
		$('.sml-media-box a').live('mouseenter', function() {
			$($(this).children('.media-box-rollover'))
				.stop().animate({left: -160, top: -160}, 250);
		}).live('mouseleave', function() {
			$($(this).children('.media-box-rollover'))
				.stop().animate({left: 0, top: 0}, 200);
		});
	}

	function attachAjaxSocial() {
		if ($('.share-box').length) {
			var text = $('.share-box span.title').first().text();
			var turl = $('.share-box span.url').first().text();
			var lang = $('.share-box').data('lang');
			var fburl = $('.share-box').data('fb-url');
			
			$('.share-box').empty();
			$.ajax({
				url: '/'+lang+'/social/share.ajax/',
				dataType: 'html',
				success: function(data){
					$('.share-box').css({opacity:'0'});
					var $d = $(data);
					$d.find('.twitter-share-button').attr('data-text',text);
					$d.find('.twitter-share-button').attr('data-url',turl);
					
					var fbFull = '//www.facebook.com/plugins/like.php?href='+fburl+'&send=false&layout=button_count&width=100&show_faces=false&action=like&colorscheme=light&font&height=21'
					
					$d.find('.share-facebook').attr('src',fbFull);
					
					$('.share-box').html($d).animate({opacity: '1'}, 500);
					
				},
				error: function() {
					$('.share-box').html('');
				}
			});
		}
	}

	function isTouchDevice() {
		return matchDevice(touch_devices);
	}

	function isDisabledDevice() {
		return matchDevice(disabled_devices);
	}

	function matchDevice(devices) {
		for (i = 0; i < devices.length; i++) {
			var regex = new RegExp(devices[i], 'i');
			if (navigator.userAgent.match(regex)) {
				return true;
			}
		}

		return false;
	}

	/**
	 * Returns a native integer value, stripped of pixel declarations.
	 */
	function getInteger(val) {
		val = new String(val).replace('px', '');

		return parseInt(val);
	}

	return {
		init: init,
		isobarBarActive: ajaxOpenerActive,
		ajaxContentHeight: ajaxContentHeight,
		ajaxContentBottomMargin: ajaxContentBottomMargin,
		attachAjaxSocial: attachAjaxSocial
	}
}();

$(document).ready(function(){
	Isobar.init();
});
