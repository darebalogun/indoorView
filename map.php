<?php
  require_once('includes/database.inc.php');
  $pdo = getConnectionInfo();

?>
<!DOCTYPE html>
<html>
  <head>
    <title>Indoor View</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta charset="utf-8" />
    <link
      href="//fonts.googleapis.com/css?family=Lora|Open+Sans"
      rel="stylesheet"
      type="text/css"
    />
    <link href="styles/style.css" rel="stylesheet" type="text/css" />
    <!--script src="https://storage.googleapis.com/vrview/2.0/build/vrview.min.js"></script-->
    <style></style>
  </head>
  <body>
    <div id="image_map">
      <map name="coord_map">
        <area
          href="360.html"
          target="_blank"
          shape="rect"
          coords="0,0,100,100"
        />
      </map>
      <img src="images/map.png" usemap="#coord_map" />
    </div>
  </body>
</html>
