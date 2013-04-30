var $ = function(elem_id) {
    return document.getElementById(elem_id);
};

var $$ = function(elem_class) {
    return document.getElementsByClassName(elem_class);
};

var init_xhr = function() {
    var xhr;
    if (window.XMLHttpRequest) {
        xhr = new XMLHttpRequest();
    }
    else {
        xhr = new ActiveXObject('Microsoft.XMLHTTP');
    }
    return xhr;
};

var get_details = function(cust_id) {
    xhr = init_xhr();
    xhr.open('GET', '/details?id={0}'.replace('{0}', cust_id), true);
    xhr.send();

    console.log(xhr.responseText);
};

window.onload = function() {
    var buttons = $$('btn-show-details');
    for (var i = 0; i < buttons.length; i += 1) {
        buttons[i].onclick = function() {
            get_details(this.id);
        };
    }
};