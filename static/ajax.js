/**
 * Created with PyCharm.
 * User: root
 * Date: 02.06.13
 * Time: 13:51
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function(){
    $('#clickme').click(function(){
        $.ajaxSetup({
            success: function(data){
                data = $.parseJSON(data);
                alert(data['new-text']);
            }
        });
        $.post('/ajax/test/', {'text': $('#test-ajax').val()});
    });