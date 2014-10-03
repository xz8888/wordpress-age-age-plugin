/**
 *  Roundarch Isobar URL Handler
 *  roundarch-urls.js
 *	@author Aaron Dunlap
 *	@copyright 7/10/12
 *  --
 *  Handles url slugs and history manipulation. Sort of informal hash routing.
 */


/*

  Easiest usage (Assuming this is page /en/whatever/:
  window.raURL = new raURL({
    0: defaultCallback, // callback function run at url /en/whatever/
    about: aboutCallback, // callback run at url /en/whatever/about/
    contact: contactCallback // callback run at /en/whatever/contact/
  });
  
  Or you don't have to pass in any routing options at first.
    window.raURL = new raURL();
    raURL.watchSlug( 'about', aboutCallback ).watchSlug( 'contact', contactCallback ).slugCheck();
    
  Or you can skip the routing and just use its helper functions
  raURL.urlSegments() 
    Object - 
      fullUrl: "/en/whatever/"
      locale: "en"
      page: "whatever"
      slug: undefined
*/
(function($, window, document, undefined){
	window.raURLinstance = function(){
    var self = this;
    self.watchSlugs = arguments[0] || {};
    
    // Return information about the current URL
    self.urlSegments = function() {
      var urlRegex = /\/([a-z]{2})\/([a-z]+)(\/[a-z0-9-_]+\/)*([a-z0-9-_]+)*/ig,
          urlMatch = urlRegex.exec(location.pathname);
      return {
        fullUrl : location.pathname,
        locale: urlMatch[1] || null,
        page: urlMatch[2] || null,
        slug: urlMatch[3] || null,
        subslug: urlMatch[4] || null
      };
    }
    
    // Return a clean version of the current page (no slugs)
    self.cleanUrl = function() {
      var urlSegments = self.urlSegments();
      return '/' + urlSegments.locale + '/' + urlSegments.page + '/';
    }
    
    // Return the current URL with the requested slug attached
    self.slugUrl = function( slug ) {
      return self.cleanUrl() + self.stringToSlug(slug) + '/';
    }
    
    // Set the full url 
    self.setUrl = function( url ) {
      if (url == undefined || url == self.urlSegments().fullUrl) return self;
      if ('replaceState' in history) {
        history.replaceState(false, '', url);
      } else {
    	 location.href = url; 
      }
      return self;
    }
    
    // Return a clean, url-friendly slug/string from a given string
    self.stringToSlug = function ( str ) {
      if ( str == null ) return '';
      return str.replace(/\s/g, '-').replace(/[^a-zA-Z0-9-]*/ig, '').replace(/\-{2,}/g,'-').replace(/-$|^-/g,'').toLowerCase();
    }
    
    // Assign a function to be run based on the existence of a specific slug
    self.watchSlug = function( slug, func ) {
      if (typeof func != 'function' || typeof slug != 'string' || slug == '') return self;
      var slug = self.stringToSlug(slug);
      self.watchSlugs[slug] = func;
      return self;
    }
    
    // If the current slug has a function defined for it, perform it
    self.slugCheck = function() {
      var urlSegments = self.urlSegments(),
          slug = self.stringToSlug( urlSegments.slug );
      
      if (slug == undefined || slug == null || slug == '') slug = 0;
      // See if there's a watchSlug set for the current slug
      if (self.watchSlugs[slug] != undefined) {
        var runFunc = self.watchSlugs[slug];
        if (typeof runFunc == 'function') {
          runFunc.apply();
        }
      }
      return self;
    }
    
    // Load a URL and place its contents within a container
    self.ajaxUrl = function(slug, selector, callback) {
      var $container = $(selector),
          urlSegments = self.urlSegments();
          
      if ($container.length == 0) return;
      
      var fullUrl = self.slugUrl( slug ) + 'ajax/';
      
      // Use jQuery to load the ajax url into the container
      $(function(){
        $container.load(fullUrl, callback);
      });
      
    }
    
    // Set up listener for back/forward button
//    if ('pushState' in history) {
//      window.onpopstate = function(e){
//        self.slugCheck();
//      };     
//    }
    return self.slugCheck();
  };
  window.raURL = new raURLinstance();
})(jQuery, this, this.document);
  
