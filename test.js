list = $("tbody").children()
for (var i = 0; i < list.length; i++){
    z = list[i].children[2]
    a = z.children[0].href
}

list = $("tbody").children()
for (var i = 0; i < list.length; i++){
    z = list[i].children[0]
    a = z.children[0]
    u = a.href
    // console.log(u)
    // $.get(u, function (data, status){console.log(status)})
    // jquery实现：
    try {
        $.ajax({
            url: u,
            type: 'get',
            dataType: 'jsonp',  // 请求方式为jsonp
            crossDomain: true,
            success: function(data) {console.log(u + "success")},
            data: {}
        });
    } catch (error) {
        // do nothing
    }
}