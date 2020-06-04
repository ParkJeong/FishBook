window.onload = function(){
  var menu = document.getElementById('menu'),
  btnShowMenu = document.getElementById('show-menu');
  btnHideMenu = document.getElementById('hide-menu');
  
  
  btnShowMenu.addEventListener("click", function showMenu(e) {
    classie.toggle(this, 'active');
    classie.toggle(menu, 'menu-open');
  });
  btnHideMenu.addEventListener("click", function showMenu(e) {
    classie.toggle(this, 'active');
    classie.toggle(menu, 'menu-open');
  });
};
