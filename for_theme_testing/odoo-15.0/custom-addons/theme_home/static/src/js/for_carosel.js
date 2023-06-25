odoo.define('theme_project.carousel_slides', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    var ExploreSlides = publicWidget.Widget.extend({
        selector: '#carousel_test',
//        events: {
//            'click .test_click': '_ontestClick',
//        },

        start: function () {
            var self = this;
            // Call the `all_slide()` method to get the list of slides.
            this._rpc({
                route: '/slide',
                params: {},
            }).then(function (slideData) {
                // Render each slide as an image.
                self._renderSlides(slideData);
            });
        },

//        _ontestClick: function () {
//            alert('hello CLick...');
//        },

        _renderSlides: function (slideData) {
            var $slider = this.$('#slider_view');
            slideData.forEach(function (slide, index) {
                var $slideContainer = $('<div>', { class: 'carousel-item' + (index === 0 ? ' active' : '') });
                var $imageContainer = $('<div>', { class: 'd-flex align-items-center' });
                var $image = $('<img>', { src: slide.image_url });
                $imageContainer.append($image);
                $slideContainer.append($imageContainer);
                $slider.append($slideContainer);
            });
        },
    });

    publicWidget.registry.carousel_test = ExploreSlides;

    return ExploreSlides;
});