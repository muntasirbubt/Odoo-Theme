
odoo.define('theme_home.my_script', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');


    var MyWidget = publicWidget.Widget.extend({
        selector: '#explore_cities',
        // Add any other necessary properties or methods
        start: function () {
//            alert('Hello!')
            var $targetElement = this.$el.find('#yh-cities-row');
            rpc.query({
                route:'/cities',
                params: {}
            }).then(function (data) {
                var html =``;
                data.forEach(city=>{
                    html += `<div class="col-lg-3 mt-5">
                                <div class="d-flex align-items-center">
                                    <div class="img-container mr-3 rounded">
                                        <img class="country-image rounded"
                                             src="data:image/png;base64,` + city.image + `"/>
                                    </div>
                                    <div>
                                        <h5 class="mb-0">${city.country_id ? city.country_id[1]: ''}</h5>
                                        <div>${city.state_id ? city.state_id:''}</div>
                                    </div>
                                </div>
                            </div>`
//                    console.log(country);
                })
                $targetElement.html(html);

            })

//            $targetElement.html('<div><p> tuhin </p></div>');
            return this._super.apply(this, arguments);
    },
    });
    publicWidget.registry.explore_cities = MyWidget;
    return MyWidget;
});