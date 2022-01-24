var SPMaskBehavior = function (val) {
  return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
  onKeyPress: function(val, e, field, options) {
      field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};


django.Jquery(function(){

    django.Jquery('.mask-telefone').mask(SPMaskBehavior, spOptions);

    django.Jquery('.mask-cpf').mask('000.000.000-00', {reverse: true});

     django.Jquery('#pessoa_form').submit(function(){
         django.Jquery('#pessoa_form').find(":input[class*='mask-']").unmask();
     });

});



