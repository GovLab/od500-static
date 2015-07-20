/*jshint browser: true*/
/*globals $*/
$(document).ready(function() {
    // Slider for the Event Pictures

    var currentPosition = 0;
    var slideWidth = 320;
    var slides = $('.event-picture-container');
    var numberOfSlides = slides.length;
    var slideShowInterval;
    var speed = 2000;

    $('.event-pictures-strip').css('width', slideWidth * numberOfSlides);

    function changePosition() {
        if(currentPosition === numberOfSlides - 3) {
            currentPosition = 1;
        } else {
            currentPosition += 1;
        }
        moveSlide();
    }

    function moveSlide() {
        $('.event-pictures-strip').animate({
            'marginLeft' : slideWidth*(-currentPosition)
        });
    }

    slideShowInterval = setInterval(changePosition, speed);

});

