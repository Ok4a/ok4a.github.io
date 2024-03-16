document.write('\
    <div id="mySidenav" class="sidenav">\
        <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>\
        <a href="boardgame.html">boardgame</a>\
        <a href="books.html">Books</a>\
        <a href="lego.html">LEGO</a>\
        <a href="switch.html">Switch</a>\
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

if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)){
    // true for mobile device
    document.write("mobile device");
  }else{
    // false for not mobile device
    document.write("not mobile device");
  }
  