odoo.define('my_module.my_script', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    var MyWidget = publicWidget.Widget.extend({
        selector: '#explore_cities',
        // Add any other necessary properties or methods
        start: function () {
            alert('Hello!')
            var $targetElement = this.$el.find('#yh-cities-row');
            this._rpc({
            route: '/cities/',
            params: {}
            })
            .then(data=>{
                data.foreach(country=>{
                    let html ='<div class="col-lg-3 mt-5">
                        <div class="d-flex align-items-center">
                            <div class="img-container mr-3 rounded">
                                <img class="country-image rounded"
                                     src="/theme_home/static/src/img/city8.png"/>
                            </div>
                            <div>
                                <h5 class="mb-0">Country Name</h5>
                                <div>City name</div>
                            </div>
                        </div>
                    </div>'
                })
            $targetElement.html(html); // Change the inner HTML

            })


            return this._super.apply(this, arguments);
    }
    });
    publicWidget.registry.explore_cities = MyWidget;
    return MyWidget;
});
