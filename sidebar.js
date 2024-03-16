document.write('\
    <div id="mySidenav" class="sidenav">\
        <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>\
        <a href="boardgame.html">boardgame</a>\
        <a href="books.html">Books</a>\
        <a href="lego.html">LEGO</a>\
        <a href="switch.html">Switch</a>\
        <button class="dropdown-btn">Dropdown \
        <i class="fa-solid fa-caret-down" style="color: #63E6BE;"></i>\
        </button>\
        <div class="dropdown-container">\
            <a href="#">Link 1</a>\
            <a href="#">Link 2</a>\
            <a href="#">Link 3</a>\
        </div>\
    </div>\
    \
    <!-- Use any element to open the sidenav -->\
    <span style="font-size:25px;cursor:pointer" onclick="openNav()">&#9776; Nav Bar</span>\
\
    <script>\
        function openNav() {\
        document.getElementById("mySidenav").style.width = "250px";\
        }\
        \
        function closeNav() {\
        document.getElementById("mySidenav").style.width = "0";\
        }\
        </script>\
');
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