document.write('\
    <div id = "side_nav_id" class = "side_nav">\
        <div class = "side_grid">\
          <a href = "boardgame.html">Brætspil</a>\
          <button class = "dropdown_btn">\
              <i class = "fa-solid fa-caret-down"></i>\
          </button>\
          <div class = "dropdown_container">\
            <a href = "base.html">Grund spil</a>\
          </div>\
        </div>\
        <div class = "side_grid">\
          <a href = "books.html">Bøger</a>\
          <button class = "dropdown_btn">\
            <i class = "fa-solid fa-caret-down"></i>\
          </button>\
          <div class = "dropdown_container">\
            <a href = "Comic.html">Comic</a>\
            <a href = "Manga.html">Manga</a>\
            <a href = "Roman.html">Roman</a>\
          </div>\
        </div>\
        <a href = "lego.html">LEGO</a>\
        <a href = "switch.html">Switch</a>\
        <!--\
        <div class = "side_grid">\
          <a href = "switch.html">Switch</a>\
          <button class = "dropdown_btn">\
          <i class = "fa-solid fa-caret-down"></i>\
          </button>\
          <div class = "dropdown_container">\
            <a href = "Mario.html">Mario</a>\
            <a href = "Zelda.html">Zelda</a>\
          </div>\
        </div>-->\
        \
    </div>\
    \
    <script src = "https://kit.fontawesome.com/81245a9c23.js" crossorigin = "anonymous"></script>\
    <!-- Use any element to open the side_nav -->\
    <span class = "open_nav" onclick = "nav_bool = navClick(nav_bool)" position: fixed;> <i id = "nav_icon" class = "fa-solid fa-bars"></i></span>\
    <span class = "compress" onclick = "compressClick()"><i id = "compress_toggle" class="fa-solid fa-toggle-on"></i></span>\
    <span class = "home"><a href = "index.html"><i class = "fa-solid fa-house"></i></a></span>\
');



var nav_bool = true;
function navClick(value) {

  if (value){
    value = false;
    if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
      // true for mobile device
      document.getElementById('side_nav_id').style.width = '100%';
  
    }else{
      // false for not mobile device
      document.getElementById('side_nav_id').style.width = '250px';
    }  
  } else {
    document.getElementById('side_nav_id').style.width = '0';
    value = true;
  }
  var menu_icon = document.getElementById('nav_icon');
  menu_icon.classList.toggle('fa-bars-staggered');

  return value
}


// compress or uncompress entries
function compressClick(){
  var toggle_icon = document.getElementById('compress_toggle');
  toggle_icon.classList.toggle('fa-toggle-on');
  toggle_icon.classList.toggle('fa-toggle-off');
  // toggle_icon.style.display = 'none'


  var compressed_elements = document.getElementsByName('compressed');

  for(var i = 0; i < compressed_elements.length; i++){
    compressed_elements[i].classList.toggle('hide_entry');
  }

  noncompressed_elements = document.getElementsByName('noncompressed');
  for(var i = 0; i < noncompressed_elements.length; i++){
    noncompressed_elements[i].classList.toggle('hide_entry');
  }
}
if (compress_on_load){
  window.onload = compressClick;
}

//
function hideCompressToggle(){
  var toggle_icon = document.getElementById('compress_toggle');
  toggle_icon.style.display = 'none'
}
if (!compressed_entries){
  window.onload = hideCompressToggle;
}


/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName('dropdown_btn');
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener('click', function() {
    
    this.classList.toggle('active');
    var dropdownContent = this.nextElementSibling;

    if (dropdownContent.style.display === 'block') {
      dropdownContent.style.display = 'none';

    } else {
      dropdownContent.style.display = 'block';
    }

    var icon = this.children[0];
    icon.classList.toggle('fa-caret-up');
    icon.classList.toggle('fa-caret-down');
  });
}


