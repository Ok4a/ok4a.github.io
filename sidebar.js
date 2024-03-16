document.write('\
    <div id="mySidenav" class="sidenav">\
        <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>\
        <a href="boardgame.html">About</a>\
        <a href="#">Services</a>\
        <a href="#">Clients</a>\
        <a href="#">Contact</a>\
    </div>\
    \
    <!-- Use any element to open the sidenav -->\
    <span onclick="openNav()">open</span>\
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