var IsobarMap = function() {
	function init() {
		attachIsobarMap();
	}

	/**
	 * Adds map to Isobar.com contact page.
	 */
	function attachIsobarMap() {
		if ($('.isobar-map').length < 1) {
			return false;
		}

		var latlng = new google.maps.LatLng(20.5238, 0);

		var myOptions = {
			map: map,
			zoom: 1,
			minZoom: 1,
			center: latlng,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			panControl: false,
			zoomControl: true,
			mapTypeControl: false,
			scaleControl: true,
			streetViewControl: true
		};

		var map = new google.maps.Map(document.getElementById("map"), myOptions);
		var geocoder = new google.maps.Geocoder();

		var markers = new Array();

		markers = addMarkers(map, agencyData);

		$('ul.list-city a').click(function(e) {

			// We're on mobile, so the map won't be visible
			if ($('.not-mobile:visible').length == 0) {
				return true;
			}

			e.preventDefault();
			$('ul.list-city li').removeClass('selected');
			$(this).addClass('selected');

			var agencyId = $(this).attr('rel');

			$.scrollTo('.site-header', 500, {
				onAfter: function(){
					infoBox(map, markers[agencyId]);
					map.setZoom(16);
				}
			});
		});
	}

	/**
	 * Attaches markers to the map with relevant infobox call to actions.
	 */
	function addMarkers(map, agencies) {

		var markers = new Array()

		for (var i = 0; i < agencies.length; i++) {
			var agency = agencies[i];
			var agencyLatLng = new google.maps.LatLng(agency[1], agency[2]);
			var marker = new google.maps.Marker({
				position: agencyLatLng,
				id: agency[9],
				map: map,
				icon: "/static/img/icons/google-map-marker.png",
				animation: google.maps.Animation.DROP,
				zIndex: 10,
				html: makeWindowHtml(
					agency[0],
					agency[3],
					agency[4],
					agency[5],
					agency[7],
					agency[8]
				)
			});

			google.maps.event.addListener(marker, "click", function(){
				infoBox(map, this);
				map.setZoom(16);
			});

			markers[marker.id] = marker;
		}

		return markers;
	}

	function infoBox(map, marker) {
		$('.info-box').hide();
		var infoBox = document.createElement("div");
		infoBox.style.cssText = "margin-bottom: 40px; background: rgb(47,47,47); padding: 0 20px 5px; color: #fff";
		infoBox.innerHTML = marker.html

		var boxOptions = {
			alignBottom: true,
			boxClass: 'info-box',
			content: infoBox,
			disableAutoPan: false,
			maxWidth: "330px",
			pixelOffset: new google.maps.Size(-16, 3),
			zIndex: null,
			boxStyle: {
				background: "url('/static/img/bg/infobox.gif') no-repeat 5% 100%",
				opacity: 0.95,
				width: "330px"
			},
			closeBoxMargin: "16px 16px 2px 2px",
			closeBoxURL: "/static/img/icons/infobox-close.gif",
			infoBoxClearance: new google.maps.Size(50, 50),
			isHidden: false,
			pane: "floatPane",
			enableEventPropagation: false
		};

		var infoBoxWindow = new InfoBox(boxOptions);

		infoBoxWindow.close(map, marker);

		infoBoxWindow.open(map, marker);
	}

	/**
	 * Returns an HTML string containing the content for the infobox on
	 * the Isobar contact page.
	 */
	function makeWindowHtml(name, phone, email, address, link, desc){
		var windowStr = "<ul class='list-details'><li style='border-bottom:#4e4e4e 1px solid;'>"+
				"<h1 class='title'>"+name+"</h1></li><li class='clearfix contact-info' style='border-bottom:#4e4e4e 1px solid;'>"+
				"<p class='address'>"+address+"</p><ul class='list-nested-details'>";

		if (new String(phone).length > 0) {
			windowStr += "<li class='phone'>"+phone+"</li>";
		}

		if (new String(link).length > 0) {
			windowStr += "<li class='link'><a href='"+link+"' target='_blank'>Visit website</a></li>";
		}

		if (new String(email).length > 0) {
			windowStr += "<li class='email'>"+email+"</li>";
		}

		windowStr += "</ul>"+
			"</li><li class='further-info'>"+desc+"</li>"+
			"</ul>";

		return windowStr;
	}

	return {
		init: init
	}
}();

$(document).ready(function(){
	IsobarMap.init();
});