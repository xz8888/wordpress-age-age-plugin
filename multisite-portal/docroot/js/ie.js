/*
*         IE()
* 
* Chainable versioning and testing method to perform JS and
* CSS changes to specific versions of Internet Explorer.
* 
*     Aaron Dunlap
* 
* Example usage:
* 
*   -Perform a function (myFunction()) in any version of IE above 5 and below 9 
*   IE().over(5).under(9).exec(function() { myFunction(); });
* 
*   -Apply some CSS styles to an element with ID "myDiv" in any version of IE
*   IE().id('myDiv').css({ marginRight: '4px', background: '#444444' });
* 
*   -Perform 2 different functions and hide a div in IE version 9 and 6
*   IE().is(9).also(6).exec(function() { myFunction(); }).exec(myOtherFunction).id('myDiv').hide(); 
* 
* 
* Note: This script also applies classes to the html <html> of the page to allow easier CSS styling.
* In all versions of IE it applies class "msie" to the <html>, as well as "IE[version]" (e.g. IE7 in Internet Explorer 7)
* 
* This allows you to use selectors in your CSS sheets such as:
* 
*  div#myDiv {
*     //Applied to all browsers
*  }
*  .msie div#myDiv {
*     //Applied to all IE versions
*  }
*  .IE8 div#myDiv {
*     //Applied only to IE8
*  }
*  .IE7 div#myDiv, .IE6 div#myDiv {
*     //Applied to IE6 and IE7
*  }
*
*/

(function(window,document,undefined){

  // Create an IE() function scoped exclusively to this anonymous function
  var IE = function() {
    var self = this;
    self.ieVersionNumber = null;
    self.aborted = false;
    self.fnStack = [];
    self.objStack = [];
    
    //  smartPerform will perform a a passed function and return its returned values
    //  only if the chain hasn't been aborted. Otherwise it returns the aborted object
    //  to allow continued chaining to fail gracefully.
    self.smartPerform = function( passedFunction ) {
      if (self.aborted) return self;
      if (!self.ieVersionNumber) {
        self.ieVersionNumber = self.findIEVersion();
        if (self.ieVersionNumber < 0) {
          self.aborted = true;
          return self;
        }
      }
      return passedFunction();
    }

    //  Filter function: allows any version of IE greater than n
    self.over = function(n) {
      return self.smartPerform(function(){
        if (self.ieVersionNumber > n) return self;
        self.aborted = true;
        return self;
      });
    };
    self.gt = self.over; // Alias function: gt() -> over()

    //  Filter function: allows any version of IE less than n
    self.under =  function(n) {
      return self.smartPerform(function(){
        if (self.ieVersionNumber < n) return self;
        self.aborted = true;
        return self;
      });
    };
    self.lt = self.under; // Alias function: lt() -> under()

    //  Filter function: allows only the exact version of IE specified
    self.is = function(n) {
      return self.smartPerform(function(){
        if (self.ieVersionNumber == n) return self;
        self.aborted = true;
        return self;
      });
    };
    self.version = self.is; // Alias function: version() -> is()
    self.exactly = self.is; // Alias function: exactly() -> is()

    //  Filter function: *also* allows the exact version of IE specified ( similar to is() ). See note below.
    self.also = function(n) {
      //  NOTE: This function can return the object back from the dead!
      //  Example: (Assume browser is IE8)
      //    IE().is(7).exec(function(){ alert(1); }).also(8).exec(function(){ alert(2); });
      //  Result: alert(2) will execute in IE8. Both alerts will execute in IE7
      //  Why?: The chain dies for IE8 at the is(7) but is brought back by the also(8)

      if (self.ieVersionNumber == n) {
        self.aborted = false;
        return self;
      }
      return self;
    };

    //  Object stack function: Adds a DOM element to the object stack given its id attribute
    self.id = function(id) {
      return self.smartPerform(function(){
        d = document.getElementById(id);
        if (d) {
          self.objStack.push(d);
        }
      });
    };

    //  Object stack function: Adds a passed object to the stack
    self.object = function(o) {
      return self.smartPerform(function(){
        if (typeof o == 'object') self.objStack.push(o);
        return self;
      });    
    };

    //  Object stack function: Apply CSS styles to the object stack. 
    //  Accepts either a string ( 'height: 5px; background-color: blue;' )
    //  Or an object containing JS styles ({ height: '5px', backgroundColor: 'blue' })
    self.css = function(c) {
      return self.smartPerform(function(){ 
        if (self.objStack.length == 0) return self;
        var toc = typeof c;
        for (var z = 0; z < self.objStack.length; z++) {
          if (toc == 'string') {
            self.objStack[z].style.cssText += ';' + c;
          }
          else if (toc == 'object') {
            for (var o in c) {
              self.objStack[z].style[o] = c[o];
            }
          }
        }
        return self;
      });
    };

    //  Object stack function: Hide all DOM elements in the stack
    self.hide = function() {
      return self.smartPerform(function(){ 
        if (self.objStack.length == 0) return self;
        for (var z = 0; z < self.objStack.length; z++) {
          // Save the current display property to _disp so it can be restored later
          self.objStack[z].setAttribute('_disp', self.objStack[z].style.display);
          self.objStack[z].style.display = 'none';
        }
        return self;
      });
    };

    //  Object stack function: Show all DOM elements in the stack
    self.show = function() {
      return self.smartPerform(function(){ 
        if (self.objStack.length == 0) return self;
        for (var z = 0; z < self.objStack.length; z++) {
          d = self.objStack[z].getAttribute('_disp');
          if (d) self.objStack[z].style.display = d;
          else self.objStack[z].style.display = '';
        }
        return self;
      });
    };

    //  Execute a passed function immediately (if the chain is alive)
    self.exec = function(fn) {
      return self.smartPerform(function(){
        if (typeof fn != 'function') return self;
        fn.call(self);
        return self;
      });
    };

    //  Function stack: Add a passed function to the stack
    self.stack = function(fn) {
      return self.smartPerform(function(){
        if (typeof fn != 'function') return self;
        self.fnStack.push(fn);
        return self;
      });
    };

    //  Function stack: Execure every function in the function stack (if chain is alive)
    self.doStack = function() {
      return self.smartPerform(function(){
        if (self.fnStack.length > 0) {
          for (z = 0; z < self.fnStack.length; z++) {
            self.fnStack[z].call();
          }
          self.fnStack = [];
        }
        return self;
      });
    };
    
    // Return any given variable if the chain is alive (or return a second argument's variable if it isn't)
    self.pipe = function() {
      if (!self.aborted) { 
        return arguments[0];
      } else if (arguments[1] != undefined) {
        return arguments[1];
      }
    }

    //  Find the version of IE. Returns -1 if any other browser.
    self.findIEVersion = function() {

      // Uses Microsoft's recommended IE detection method
      // http://msdn.microsoft.com/en-us/library/ms537509(v=vs.85).aspx    
      var rv = -1;
      if (navigator.appName == 'Microsoft Internet Explorer') {
        var ua = navigator.userAgent;
        var re = new RegExp("MSIE ([0-9]{1,}[\.0-9]{0,})");
        if (re.exec(ua) !== null) rv = parseFloat(RegExp.$1);
      }
      return rv;
    };

    // Establish the ieVersionNumber variable up front
    self.ieVersionNumber = self.findIEVersion();
    if (self.ieVersionNumber < 0) self.aborted = true;

    return self;
  }

  //  Apply IE() container function to DOM for global scope
  //  IE() will return a clean instance of IE() if no arguments are passed
  //  Otherwise, it will perform some smart filtering based on the args
  window.IE = function(v) {
    var z = new IE();
    if (v == undefined) return z;
    if (arguments.length > 1) {
      // Perhaps multiple numbers were passed ( IE(7,8,10) )
      for (var key = 0; key < arguments.length; key++) {
        if (key == 0) {
          z.is(arguments[key]);
          continue;
        }
        z.also(arguments[key]);
      }
      return z;
    }
    if (typeof v == 'function') return z.exec(v); // Shorthand: IE(function(){ }) = _IE.exec(function(){});
    if (typeof v == 'number') return z.is(v); // Shorthand: IE(9) = _IE.is(9); 
    if (v.indexOf(',')>-1) {
      // Allow passing a comma-separated string of specific version numbers ('6,7,8')
      var versions = v.split(',');
      for (var key in versions) {
        if (parseInt(versions[key]) == NaN) continue; // Must be a number
        if (key == 0) {
          z.is(versions[key]);
          continue;
        }
        z.also(versions[key]);
      }
      return z;
    }
    // Shorthands for over/under functions
    if (v.substr(0,2) == '<=') return z.under(parseInt(v.substr(2))).also(parseInt(v.substr(2)));
    if (v.substr(0,2) == '>=') return z.over(parseInt(v.substr(2))).also(parseInt(v.substr(2)));
    if (v.substr(0,1) == '<') return z.under(parseInt(v.substr(1)));
    if (v.substr(0,1) == '>') return z.over(parseInt(v.substr(1)));
    return z;  
  };

})(this,this.document);

(function(window,document,undefined){
  /* Apply version specific class names to the <html> element of the DOM if browser is IE */
  IE(function(){
    var v = this.ieVersionNumber,
      c = document.documentElement.className + ' msie IE' + v;
    document.documentElement.className = c.replace(/^\s\s*/, '').replace(/\s\s*$/, '');     
  });
})(this,this.document);
