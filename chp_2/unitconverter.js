conversion_map = {
    "inch cm":1.0/2.45,
    "cm inch":2.45
    };
// covert  button element into button-widget
button = $("button").button({
      icons: {
        primary: "ui-icon-locked"
      }});
button.click(function(){
            value = $("input[name = 'from']").val();
            f = $("select['tounit'] option = selected").val();
            t = $("select['fromunit'] option = selected").val();
            if (t != f){
                c = conversion_map[ f + " " + t];
                result = parseFloat(value) * c;
            } else {
                c = conversion_map[ t + " " + t];
                result = value;
            }
            $("input[name = 'to']").val(result);
    });

$("form *").addClass("ui-widget");
