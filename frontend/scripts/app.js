/**
 * App
 */

$(document).ready(function(){

    var source   = $("#entry-template").html();
    var template = Handlebars.compile(source);
    var context = {title: "My New Post", body: "This is my first post!"};
    var errormessage =
        '<div class="error">' +
            'Be sure to add a title' +
        '</div>'
    ;
    var menuActive = false;

    $('.menu-trigger').click(function(e){
        var $self = $(this),
            activeClass = 'is-active';
        if(!menuActive){
            menuActive = true;
            $self.parent().addClass(activeClass);
        }else{
            menuActive = false;
            $self.parent().removeClass(activeClass);
        }
        e.preventDefault();
    });
    $('.menu-option a').each(function(){
        $(this).click(function(e){
            var type = $(this).data('type');
            var target = '.' + type;
            $('.entry--add').removeClass('is-active');
            $(target).addClass('is-active');
            $('.menu').removeClass('is-active');
            e.preventDefault();
        });
    });

    $('.share-btn').click(function(e){
        e.preventDefault();
    });

    $('.entry-form').each(function(){
        var $self = $(this);
        var hasError = false;
        var date = new Date().toLocaleString().split(',')[0];
        $(this).find('#date').value = date;
        $(this).find('button').click(function(e){
            var obj = {},
                inputs = $self.find('input'),
                vals = [];
            for(var i=0;i<inputs.length;i++){
                var $input = $(inputs[i]),
                    inputlabel = $input.attr('id'),
                    inputval = $input.val();
                vals.push(inputval);
                obj[inputlabel] = inputval;
            }
            console.log(obj,vals.length,vals);
            if(vals[1]!== ''){
                var html = template(obj);
                $('.entries').prepend(html);
                $self.closest('.entry--add').removeClass('is-active');
            }else{
                if(!hasError){
                    $self.prepend(errormessage);
                    hasError = true;
                }
            }
            e.preventDefault();
        });
    });

var profileMenuActive = false;
    var $window = $(window);
    var $header = $('.page-header');
    var props = {
      headerheight : $header.height(),
      stickyclass : 'sticky'
    }

    function setsticky(){
      var pos = $window.scrollTop();
      if(pos >= props.headerheight){
        $header.addClass(props.stickyclass);
      }else{
        $header.removeClass(props.stickyclass);
      }
    }

    $window.on('scroll', setsticky);;


 $('.profileinfo-name .label').click(function(e){
    var $self = $(this),
        activeClass = 'is-active';
    if(!profileMenuActive){
        profileMenuActive = true;
        $self.parent().addClass(activeClass);
    }else{
        profileMenuActive = false;
        $self.parent().removeClass(activeClass);
    }
    e.preventDefault();
});

var publicProfile = false;
 $('.profileinfo-menu a').click(function(e){
    var $self = $(this),
        activeClass = 'public-profile';
    if(!publicProfile){
        publicProfile = true;
        $('body').addClass(activeClass);
    }else{
        publicProfile = false;
        $('body').removeClass(activeClass);
    }
    e.preventDefault();
});

});

