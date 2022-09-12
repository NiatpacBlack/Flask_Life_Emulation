$(document).ready(function () {
    setInterval(refresher, 250);
});

function refresher() {
    $.ajax({
        url: '/live',
        method: "GET",
        dataType: 'html',
        success: function (response) {
            // jquery call
            var htmlObject = $(response);
            // обновление счётчика
            document.getElementById('counter').innerHTML = htmlObject.find('#counter')[0].innerHTML;
            // обновление таблицы
            document.getElementById('world').innerHTML = htmlObject.find('#world')[0].innerHTML;
        },
        error: function (xhr, status, error) {
            alert(xhr.responseText);
            alert(error);
        }
    });
}
