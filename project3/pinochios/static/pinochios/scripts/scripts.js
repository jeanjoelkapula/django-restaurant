$(document).ready(function () {
  document.getElementsByClassName('body-container')[0].onscroll = function(){
    scrollFunction()
  }
});
function scrollFunction(){
  var sn = document.getElementsByClassName('navbar')[0];
  if(document.getElementsByClassName('body-container')[0].scrollTop > 100){
    $('#navbar').css('animation-name', 'sticky_nav');
  }
  else {
    if($('#navbar').css('animation-name') == 'sticky_nav'){
      $('#navbar').css('animation-name', 'nav_normal');

    }
  }
}


$(document).ready(function () {

  //INPUT ACTIVE CODE
  $("input").focus(function() {
    $(this).css("color", "rgb(254, 197, 3)");
    $(this).parent().css("border-color", "rgb(254, 197, 3)");
  });

  $("input").focusout(function(){
    $(this).css("color", "rgb(118, 118, 118)");
    $(this).parent().css("border-color", "rgb(118, 118, 118)");
  });
});


//INPUT SELECT
function DropDown(el, remain_open) {
  this.dd = el;
  this.placeholder = this.dd.children('span');
  this.opts = this.dd.find('ul.drop li');
  this.value = '';
  this.values = [];
  this.index = -1;
  this.remain_open = remain_open;
  this.initEvents();
}

DropDown.prototype = {
  initEvents: function () {
    var obj = this;
    obj.dd.on('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      if (obj.remain_open == false) {
        $(this).toggleClass('active');
        $(this).parent().siblings().addClass('.wrap-dropped');
        $(this).css('display', 'relative');
        $(this).css('z-index', '999');
      }
      else {
        if (e.target == $(this)[0]) {
          $(this).toggleClass('active');
        }
        else {
          return;
        }
      }
    });

    obj.opts.on('click', function () {
      var opt = $(this);
      if (obj.remain_open != true) {
        obj.value = opt.text();
        obj.index = opt.index();
        obj.placeholder.text(obj.value);
        opt.siblings().removeClass('selected');
        opt.filter(':contains("' + obj.value + '")').addClass('selected');
      
        /*if ($(this).parent().parent()[0].id = "noble-gases" && opt.text() =='Pizza') {
          $('.topping-selection').css('display', 'block');
          $('.subs-selection').css('display', 'none');
          $('.pasta-selection').css('display', 'none');
          $('.salad-selection').css('display', 'none');
          $('.dinner-platter-selection').css('display', 'none');
        }

        if ($(this).parent().parent()[0].id = "noble-gases" && opt.text() =='Sub') {
          $('.pizza-type-selection').css('display', 'none');
          $('.topping-selection').css('display', 'none');
          $('.subs-selection').css('display', 'block');
          $('.pasta-selection').css('display', 'none');
          $('.salad-selection').css('display', 'none');
          $('.dinner-platter-selection').css('display', 'none');
        }

        if ($(this).parent().parent()[0].id = "noble-gases" && opt.text() =='Burger') {
          $('.pizza-type-selection').css('display', 'none');
          $('.topping-selection').css('display', 'none');
          $('.subs-selection').css('display', 'none');
          $('.pasta-selection').css('display', 'none');
          $('.salad-selection').css('display', 'none');
          $('.dinner-platter-selection').css('display', 'none');
        }

        if ($(this).parent().parent()[0].id = "noble-gases" && opt.text() =='Salad') {
          $('.pizza-type-selection').css('display', 'none');
          $('.topping-selection').css('display', 'none');
          $('.subs-selection').css('display', 'none');
          $('.pasta-selection').css('display', 'none');
          $('.salad-selection').css('display', 'block');
          $('.dinner-platter-selection').css('display', 'none');
        }

        if ($(this).parent().parent()[0].id = "noble-gases" && opt.text() =='Pasta') {
          $('.pizza-type-selection').css('display', 'none');
          $('.topping-selection').css('display', 'none');
          $('.subs-selection').css('display', 'none');
          $('.pasta-selection').css('display', 'block');
          $('.salad-selection').css('display', 'none');
          $('.dinner-platter-selection').css('display', 'none');
        }

        if ($(this).parent().parent()[0].id = "noble-gases" && opt.text() =='Dinner Platter') {
          $('.pizza-type-selection').css('display', 'none');
          $('.topping-selection').css('display', 'none');
          $('.subs-selection').css('display', 'none');
          $('.pasta-selection').css('display', 'none');
          $('.salad-selection').css('display', 'none');
          $('.dinner-platter-selection').css('display', 'block');
        }*/
      }
      else {
        if (($(opt[0]).find('img')[0].style.display == 'none') || (window.getComputedStyle($(opt[0]).find('img')[0]).display == 'none')) {
            $(opt[0]).find('img')[0].style.display = 'block';
            $(opt[0]).find('a')[0].style.color = 'rgb(254,197,3)';
            obj.values.push(opt.text());
            opt.filter(':contains("' + obj.value + '")').addClass('selected');
        }
        else {
            $(opt[0]).find('img')[0].style.display = 'none';
            $(opt[0]).find('a')[0].style.color = 'rgb(118,118,118)';
            if (obj.values.includes(opt.text())) {
                var index = obj.values.indexOf(opt.text());
                obj.values.splice(index,1);
                opt.removeClass('selected');
            }
        }
        if (obj.values.length == 0) {
          obj.placeholder.text('select a topping');
        }
        else {
          obj.placeholder.text(obj.values);
        }
      }
    }).change();
  },
  getValue: function () {
    return this.val;
  },
  getIndex: function () {
    return this.index;
  }
};



//NUMERIC UP AND DOWN
$(document).ready(function() {
    $('.minus').click(function () {
      var $input = $(this).parent().find('input');
      var count = parseInt($input.val()) - 1;
      count = count < 1 ? 1 : count;
      $input.val(count);
      $input.change();
      return false;
    });
    $('.plus').click(function () {
      var $input = $(this).parent().find('input');
      $input.val(parseInt($input.val()) + 1);
      $input.change();
      return false;
    });
  });

$(document).ready(function (){
  // create new variable for each menu
  var menu_items_dd = new DropDown($('#menu-items-dd'), false);
  var dd2 = new DropDown($('#topping-dropdown'), true);
  var dd3 = new DropDown($('#subs-dropdown'), false);
  var dd4 = new DropDown($('#pasta-dropdown'), false);
  var dd5 = new DropDown($('#salad-dropdown'), false);
  var dd6 = new DropDown($('#platter-dropdown'), false);

  $(document).click(function () {
    // close menu on document click
    $('.wrap-drop').removeClass('active');
  });

  //get selected item from menu
  menu_option_container = document.getElementById('menu-options-container');

  menu_option_container.innerHTML = '';
  var innerHTML = ``;
  menu[0].menu_options.forEach(function(item, index) {
    innerHTML += `<li><a>${item.menu_option_name}</a><img src="images/checkmark.png"></li>`;
  });

  menu_option_container.innerHTML= innerHTML;

  $(menu_items_dd.opts).click(function(){
      var opt = $(this);
      
      //get selected item from menu
      menu.forEach(function(item, index){
        if (item.menu_item_name == opt.text()) {
          menu_item = item;
        }
      });
      
      menu_option_container = document.getElementById('menu-options-container');

      menu_option_container.innerHTML = '';
      var innerHTML = ``;
      menu_item.menu_options.forEach(function(item, index) {
        console.log('Item: ' + opt.text() + ' menu option name: ' + item.menu_option_name);
        innerHTML += `<li><a style='display: flex;'>${item.menu_option_name}</a><img src="images/checkmark.png"></li>`;
      });

      menu_option_container.innerHTML= innerHTML;
  });

  

  $('#order-menu-item-span')[0].innerHTML = menu[0].menu_item_name;
  $('.more-button').click(function (){
    $('#modal-toggle-button').click();
  });

  
});
