$(document).ready(function(){
	// google map instance:
    var map;
    
    // the pop-up
    var popup = $('#contacts-popup');
    
    // map marker:
	var activeMarker;
	
    /**
     * Gather the information to show in the pop-up and display the pop-up
     */
    function showPopup(agencyName, position, mouseY) {
    	// remove existing marker if there is one:
    	clearMarker();
    	
    	$('#contacts-popup #pop-up-office-name').text( agencyName );
    	
    	var matchedItems = [];
    	$.each( agencyData, function( idx, value ) {
    		if ( value && value.name && value.name.toUpperCase() == agencyName.toUpperCase() )
    			matchedItems.push(value);
    	});
    	
    	// build the list-items using the template
    	var listItems = buildHTML( matchedItems );
    	$.each( listItems, function( idx, value ) {
    		if (idx < 2)
    			$('#contacts-popup #container-map-container-one').append( value );
    		else
                $('#contacts-popup #container-map-container-two').append( value );
    	});
    	
    	popup.fadeIn();
    	
        if ( popup.css('position') != 'fixed' ) {
        	// check whether the pop-up is opening in last column, in which case it may go off the right side of screen,
            // and whether it is opening at the bottom of the screen:
        	popup.offset({ 	top: (mouseY + popup.height() + 10 > $(window).height()) ? (position.top - popup.height()) : position.top, 
        					left: (position.left + popup.width() + 10 > $(window).width()) ? (position.left - popup.width()) : position.left });
        }
        
        google.maps.event.trigger(map, "resize");
        
        var firstItem = matchedItems[0];
        onlyAddMarker( map, firstItem );
        
		$('.contact-city').eq(1).addClass('active-office');
    }
    
    function buildHTML( matchedItems ) {
        var resultItems = [];
    	
    	// create an entry for each item in matchedItems
        $.each( matchedItems, function( idx, value ) {
            var template = $( $('#popup-office-template')[0].innerHTML );
            template = setTemplateHTML( template, value );
            resultItems.push( template );
        });
    	
    	return resultItems;
    }
    
    /**
     * Dictionary keys represent the names of the template items,
     * the values are the names of the properties of the JSON objects in "agencyData".
     * Example object:
     * { 	
     * 		name: 'wwwins Isobar: Beijing', longitude: '116.414888', latitude: '39.909555', 
     * 		phone: '+86 10 8500 2300', email: 'alvin.huang@isobar.com', url: 'http://www.glueisobar.com',
     * 		address1: 'Unit 908, Level 9, Office Tower E1, Oriental Plaza, 1 East Chang An Avenue, Beijing 100738, Tel: +86 10 8512 7300', 
     * 		address2: 'Unit 908, Level 9, Office Tower E1, Oriental Plaza, 1 East Chang An Avenue, Beijing 100738, Tel: +86 10 8512 7300',
     * 		country: 'China'
     * }
     */
    var jsonPropertyDict = {
		"contact-city": "city", 
		"contact-name": "name", 
		"contact-address-line-one" : "address1", 
		"contact-address-line-two": "address2", 
        "directions-link": null, 
        "website-link": "url", 
        "telephone-link": "phone", 
        "email-link": "email"
    };
    
    function setTemplateHTML( template, agency ) {
        $.each ( jsonPropertyDict, function ( htmlID, jsonProperty ) {
        	element = $( template ).find('.' + htmlID);
        	if ( element[0] ) {
        		if ( htmlID != 'directions-link' )
                    element[0].innerHTML = agency[ jsonProperty ];
        		
                var $element = $( element[0] );

                if ( htmlID == 'contact-city' ) {
                	$element.click(function(e) {
                		e.preventDefault();
                		
                		$('.contact-city').removeClass('active-office');
                		$(this).addClass('active-office');
                		clearMarker();
                		onlyAddMarker(map, agency);
                	});
                }
                
                if ( htmlID == 'contact-address-line-two' && agency[ jsonProperty ] == agency[ jsonPropertyDict[ 'contact-address-line-one' ] ])
                	$element.hide();
                
        		if ( htmlID == 'directions-link' ) {
        			$element.attr( 'href', 'http://maps.google.co.uk/maps?f=d&source=s_d&saddr=&daddr=' + agency.latitude + ',' + agency.longitude );
        		} else if ( htmlID == 'email-link' ) {
        			$element.attr( 'href', 'mailto:' + agency.email );
                } else if ( htmlID == 'telephone-link' ) {
                	$element.attr( 'href', 'tel:' + agency.email );
                } else if ( htmlID == 'website-link' ) {
                	$element.attr( 'href', agency[ jsonProperty ] );
                }
        	}
        });
        
        return template;
    }
    
    $('.map-link').click(function(e) {
    	e.preventDefault();

    	// mobile: don't bring up the pop-up
    	if ( $(window).width() <= 480 )
    		return;
    	
        $('#contacts-popup').css({
            display: "none"
        })
    	
        $('#contacts-popup #container-map-container-one').empty();
        $('#contacts-popup #container-map-container-two').empty();
    	
        var position = $( e.target ).offset();
    	var selectedCountry = e.target.innerHTML;
    	
    	showPopup(selectedCountry, position, e.clientY);
    });
    
    /**
     * Attaches maps to page.
     */
    function attachMaps() {
        var latlng = new google.maps.LatLng(0, 0);

        var myOptions = {
            zoom: 2,
            minZoom: 1,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            panControl: false,
            zoomControl: true,
            mapTypeControl: false,
            scaleControl: true,
            streetViewControl: true
        };

        map = new google.maps.Map(
            document.getElementById("map"),
            myOptions
        );

        $(window).resize(function() {
            map.panTo(latlng);
        });
    }

    /**
     * Attaches marker only to the map given an agency with latitude and longitude properties.
     */
    function onlyAddMarker(map, agency) {
        var agencyLatLng = new google.maps.LatLng( parseFloat(agency.latitude), parseFloat(agency.longitude) );
        
        map.setZoom(15);
        map.panTo(agencyLatLng);
        
        var marker = new google.maps.Marker({
            position: agencyLatLng,
            map: map,
            icon: "/static/img/icons/google-map-marker.png",
            animation: google.maps.Animation.DROP,
            zIndex: 10
        });
        activeMarker = marker;
    }

    /**
     * Clears markers from the map.
     */
    function clearMarker() {
        if ( activeMarker )
        	activeMarker.setMap( null );
    } 

    /**
     * remove pop-up
     */
    function removeMap() {
    	popup.css({
    		display: "none"
    	});
    }
    
    // remove-popup on window resize
    $(window).unbind('resize').resize( removeMap );
    // remove-popup on close button click
    $('#popup-close-button').click(function(e) {
    	removeMap();
    });
    
    // remove pop-up on click outside of an element:
    // http://stackoverflow.com/questions/1403615/use-jquery-to-hide-a-div-when-the-user-clicks-outside-of-it
    $(document).mouseup(function(e)
	{
	    if ( popup.has(e.target).length === 0 )
	    	removeMap();
	});
    
    attachMaps();
});
