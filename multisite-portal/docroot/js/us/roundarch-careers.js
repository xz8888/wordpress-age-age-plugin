(function($, window, document, undefined){
	$(function() {
		var currentJob = -1;
		var currentLocation = "Boston";
		var locations = [ "Chicago", "New York", "Boston", "Denver", "Washington DC", "Detroit" ];
		var loadingImage = '<center><br/><br/><img src="/static/img/icons/loading/light.gif" width="34" height="34" /></center>';

		var params = {};
		
		initUrlParams();
		
		if ( params[ "currentJob" ] != "" && params[ "currentJob" ] != undefined )
			currentJob = unescape( params[ "currentJob" ] );
		if ( params[ "currentLocation" ] != "" && params[ "currentLocation" ] != undefined )
			currentLocation = unescape( params[ "currentLocation" ] );
	
		selectLocation( currentLocation, false );
	
		function clear()
		{
			$( '#jobList' ).html(loadingImage);
			$( '#jobDetails' ).html(loadingImage);
		}
	
		function loadJobList()
		{
			clear();
			$.getJSON(escape(currentLocation) + '/', function(data){
				if (data)
				{
					if (typeof(data) == "string")
						data = $.parseJSON(data);
					
					data.sort(function (a,b) {
				        return (a["title"] < b["title"]) ? -1 : (a["title"] > b["title"]) ? 1 : 0;
				    });
					
					var items = [];
					
					for (var l = 0; l < data.length; l++){
						items.push("<div id=\"jobTitle" + data[l]["id"] + "\" class=\"jobListTitle\" ><a href=\"javascript:selectJob('" + data[l]["id"] + "');\"><p>" + data[l]["title"] + "</p></a></div>");	
					};
					
					$( '#jobList' ).html(items.join(""));
				}
				
				if(currentJob !== -1){
					selectJob(currentJob);
				}else{
					selectJob(data[0]["id"]);
				}
				
			});
		}
	
		function loadJobDetails()
		{
			$( '#jobDetails' ).load( 'job/' + currentJob + '/');
		}
	
		function selectLocation( location, clearSelectedJob )
		{
			currentLocation = location;
			if ( clearSelectedJob == true) currentJob = -1;
			
			clear();
			loadJobList();

			$( '.jobLocation' ).removeClass( 'linkArticleListSelected' );
			
			$( '.jobLocation a' ).each( function(e) {
				var text = $.trim( $(this).html() );
				if (text.indexOf(currentLocation) != -1)
					$(this).parent().addClass( 'linkArticleListSelected' );
			});
			
			updateUrl();
		}
	
		function selectJob( idx )
		{
			$( '#jobDetails' ).html(loadingImage);
	
			currentJob = idx;
			loadJobDetails();
			
			var titleId = null;
			var title = null;
			
			$( '.jobListTitle' ).removeClass( 'jobListTitleSelected' );
			$( '#jobTitle' + idx ).addClass( 'jobListTitleSelected' );
			
			updateUrl();
		}
	
		function updateUrl()
		{
			$.address.value("currentJob="+currentJob+"&currentLocation="+escape(currentLocation));
		}
	
		function initUrlParams()
		{
			var url = $.address.value().substring(1);
			var kvs = url.split( "&" );
			for ( var i=0; i<kvs.length; i++)
			{
				var keyAndVal = kvs[i].split("=");
				params[ keyAndVal[0] ] = keyAndVal[ 1 ];
			}
		}
		
		window.selectLocation = selectLocation;
		window.selectJob = selectJob;
	});
})(jQuery, this, this.document);
