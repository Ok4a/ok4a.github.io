document.write('\
    <div id="mySidenav" class="sidenav">\
        <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>\
        <a href="boardgame.html">Brætspil</a>\
        <div class = "side_grid">\
          <a href="books.html">Bøger</a>\
          \
          <button class="dropdown-btn">\
            <i class="fa fa-caret-down" style="color: #63E6BE;"></i>\
          </button>\
          <div class="dropdown-container">\
            <a href="Comic.html">Comic</a>\
            <a href="Manga.html">Manga</a>\
            <a href="Novel.html">Novel</a>\
          </div>\
        </div>\
        <a href="lego.html">LEGO</a>\
        <a href="switch.html">Switch</a>\
        \
    </div>\
    \
    <!-- Use any element to open the sidenav -->\
    <span class = "open_nav" onclick="openNav()" position:fixed;>&#9776;</span>\
');

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}
  
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}


/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}