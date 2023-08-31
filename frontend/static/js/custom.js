
  (function ($) {
  
  "use strict";

    

    // REVIEWS CAROUSEL
    $('.reviews-carousel').owlCarousel({
    items:2,
    loop:true,
    autoplay: true,
    margin:30,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:1
        },
        1000:{
          items:2
        }
      }
    })

    
})(window.jQuery);


