window.addEventListener("scroll", function() {
    if (window.scrollY > 350) {
        $('.navbar-fixed-top').fadeOut();
    }
    else {
        $('.navbar-fixed-top').fadeIn();
    }
},false);
