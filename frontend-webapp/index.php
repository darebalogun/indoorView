<?php
  require_once('includes/database.inc.php');
  $pdo = getConnectionInfo();

  $maps = getAllMaps($pdo); 

?>
<!DOCTYPE html>
<html>
  <head>
    <title>IndoorView</title>
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
    <h1>
      <?php
        $count = 0;
        foreach ($maps as $map){
          $count++;
          echo("<a href='map.php?map=" . $count . "'>" . $map[0] . "<br>"); 
        }
      ?>
    </h1>
  </body>
</html>
