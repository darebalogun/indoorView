<?php
  require_once('includes/database.inc.php');
  $pdo = getConnectionInfo();
  $map_name = getMapNameWithIndex($pdo, $_GET['map'])->fetchColumn(0);
  $imagepath = getImagePathWithIndex($pdo, $_GET['map'])->fetchColumn(0);

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
    <script src="includes/imageMapResizer.min.js"></script>
    <script src="https://storage.googleapis.com/vrview/2.0/build/vrview.min.js"></script>
  </head>
  <body>
  <div class="row">
    <div class="column" id="image_map">
      <map name="coord_map">
        <?php
          echo('<area')
        ?>

        <area
          href="map.php?map=1"
          target="_blank"
          shape="circle"
          coords="2,2,2"
        />
      </map>
      <?php
        echo('<img src="'. $imagepath .'" usemap="#coord_map" />')
      ?>
    </div>
    <div class="column" id="vrview"></div>
    <script>
      window.addEventListener("load", onVrViewLoad);
      function onVrViewLoad() {
        var vrView = new VRView.Player("#vrview", {
          image: "images/converted.jpg",
          is_stereo: false,
          width: "100%",
          height: "100%"
        });
      }
    </script>
    </div>
    <script>imageMapResize()</script>
  </body>
</html>
