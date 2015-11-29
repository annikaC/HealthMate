/**
 * App
 */

var handleModal = {
    open : function(e) {
        var $self = $(this),
            $target = $('.modal');
        $target.addClass('is--active');
        e.preventDefault();
    },
    close : function(e) {
        var $self = $(this),
            $target = $('.modal');
        $target.removeClass('is--active');
        e.preventDefault();
    }
}

$('.modal-trigger').click(handleModal.open);
$('.modal-close').click(handleModal.close);
