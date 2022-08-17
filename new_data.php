
<!-- Dette er et stort formfelt hvor man kan sætte den data til den film man ville tilføje til siden-->
<form action="save_data.php" enctype="multipart/form-data" method="post">
Billed:<input name="uploadedimage" type="file"><br>
Navn:<input type="text" name="movie_name"><br>
Spille tid:<input type="time" name="runtime"><br>

<input name="Upload Now" type="submit" value="Upload data">
</form>

<!--Tilbage til start -->
<a href="index.php">Tilbage til start</a>
