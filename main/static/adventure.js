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

var init_button = function() {
    get_details(this.getAttribute('id').replace('btn_', ''));
};

var show_detail_plate = function(details, row_id) {
    var target = $(row_id);
    var new_row = document.createElement('tr');
    var render_plate = function(details) {
        var plate = "<table>" + 
                        "<tr>" +
                            "<td>email address</td>" +
                            "<td>{{ email }}</td>" +
                        "</tr>" +
                        "<tr>" +
                            "<td>company name</td>" +
                            "<td>{{ company }}</td>" +
                        "</tr>" +
                    "</table>";

        return plate.replace('{{ email }}', details.email).replace('{{ company }}', details.company_name);
    };

    target.parentNode.insertBefore(new_row, target.nextSibling);
    var cell = new_row.insertCell(0);
    cell.colSpan = "5";
    cell.innerHTML = render_plate(details);
    
    return new_row;
};

var show_details = function(details, cust_id) {
    var button = $('btn_{0}'.replace('{0}', cust_id));
    var plate = show_detail_plate(details, 'row_{0}'.replace('{0}', cust_id));
    
    button.innerHTML = "close";
    button.onclick = function() {
        $('tbl_customers').deleteRow(plate.rowIndex);
        this.innerHTML = "show";
        this.onclick = init_button;
    };
};

var get_details = function(cust_id) {
    var xhr = init_xhr();
    
    xhr.open('GET', '/details/{0}/'.replace('{0}', cust_id), true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            show_details(JSON.parse(xhr.responseText), cust_id);
        }
    };
    xhr.send();
};

window.onload = function() {
    var buttons = $$('btn-show-details');
    
    for (var i = 0; i < buttons.length; i += 1) {
        buttons[i].onclick = init_button;
    }
};