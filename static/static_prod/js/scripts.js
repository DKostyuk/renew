$(document).ready(function(){
   var form = $('#form_buying_product');
   console.log(form);
   var form_1 = $('#form_buying_product_1');
   console.log(form_1);


   function basketUpdating(product_id, nmb, is_delete) {
       // ajax()
       var data ={};
       data.product_id = product_id;
       data.nmb = nmb;
       var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
       data["csrfmiddlewaretoken"] = csrf_token;

       if (is_delete){
            data["is_delete"] = true;
        }

       var url = form.attr("action");

       console.log(data);

       $.ajax({
           url: url,
           type: 'POST',
           data: data,
           cache: true,
           success: function (data) {
               console.log("OK");
               console.log(data.products_total_nmb)

               if (data.products_total_nmb || data.products_total_nmb == 0){
                   $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                    console.log(data.products);
                   $('.basket-items ul').html("")
                   $.each(data.products, function(k, v){
                       $('.basket-items ul').append('<li>'+ v.name +', '+ v.nmb +' штук по '+ v.price_per_item +' грн.          ' +
                            '<a class="delete-item" href="" data-product_id="'+v.id+'">X</a>'+
                            '</li>');
                   })
               }
           },
           error: function(){
               console.log("ERROR");
           }
       })
   }

   form.on('submit', function (e) {
       e.preventDefault();
       console.log('258');
       var nmb = $('#number').val();
       console.log(nmb);
       var  submit_btn = $('#submit_btn');
       var product_id = submit_btn.data("product_id");
       var product_name = submit_btn.data("name");
       var product_price = submit_btn.data("price");
       console.log(product_id);
       console.log(product_name);
       console.log(product_price);

       basketUpdating(product_id, nmb, is_delete=false)

   });

   form_1.on('submit', function (e) {
       e.preventDefault();
       console.log('999');
       var nmb = $('#number_1').val();
       console.log(nmb);
       var  submit_btn = $('#submit_btn_1');
       var product_id = submit_btn.data("product_id");
       var product_name = submit_btn.data("name");
       var product_price = submit_btn.data("price");
       console.log(product_id);
       console.log(product_name);
       console.log(product_price);

       basketUpdating(product_id, nmb, is_delete=false)

   });

    function showingBasket(){
       $('.basket-items').removeClass('hidden');
    }

    $('.basket-container').on('mouseover', function(e){
        e.preventDefault();
        showingBasket();
    });

    $('.basket-container').on('mouseout', function(e){
        e.preventDefault();
        $('.basket-items').addClass('hidden');
    });

    $(document).on('click','.delete-item', function(e){
        e.preventDefault();
        product_id = $(this).data("product_id");
        nmb = 0;
        basketUpdating(product_id, nmb, is_delete=true)
    });

    function calculatingBasketAmount(){
        //console.log(123);
        var total_order_amount = 0;
        // проходим по каждому элементу с таким class (ИД может быть только у одного элемента на странице !!!!)
        $('.total-product-in-basket-amount').each(function(){
            // прибавляем с переменной то что взяли при проходе элемента
            total_order_amount +=parseFloat($(this).text()); //преобразовывает текст в число parseFloat
        });
        //console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount.toFixed(2)); // вписываем значение текстом на ИД
    };
    calculatingBasketAmount();

    $(document).on('change','.product-in-basket-nmb', function () { //отслеживаем изменения на классе
        var current_nmb = $(this).val(); // считыаем текущее кол-во и получаем значение в переменную
        var current_tr = $(this).closest('tr');//находим строку-ячейку где произошли изменения - ближайшая tr
        // console.log('current_tr   ', current_tr);
        var current_price = parseFloat(current_tr.find('.product-price').text()); // из этого ряда находим span
                                                                                  // с нужным классом.
                                                // из него берем текст и переводим с помощью ParseFloat в число
        var total_amount = parseFloat(current_nmb*current_price).toFixed(2); // получаем новую сумму, новое кол-во на сущ.цену
        current_tr.find('.total-product-in-basket-amount').text(total_amount); //находим в текущей строке span с нужным
                                        // классом и записываем туда текстом переменную - общую новую сумму по строке
        calculatingBasketAmount();
    });

    calculatingBasketAmount();

    //------------------------------------------------------------
});

function initMapMy() {
    var element = document.getElementById('map');
    var options = {
        zoom: 17,
        center: {lat: 52.280973, lng: 20.967678}
    };

    var myMap = new google.maps.Map(element, options);

    var marker = new google.maps.Marker({
       position: {lat: 52.280973, lng: 20.967678},
       map: myMap
    });

    var infoWindow = new google.maps.InfoWindow({
        content: '<h4>Renew-Polska</h4>' +
        '<p>Biuro RENEW-POLSKA Sp. z o. o.' + '<br>Oficjalny dystrybutor TM RENEW oraz TM Alvi-Prague' +
        '<br>Warszawa, ul. Lektykarska 26 (wejście z ul. Cząstkowska)</br>'
    });

    infoWindow.open(myMap, marker);

    marker.addListener('mouseover',function () {
        infoWindow.open(myMap, marker);
    })
}