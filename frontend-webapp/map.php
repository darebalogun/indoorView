<?php
  require_once('includes/database.inc.php');
  $pdo = getConnectionInfo();
  $map_name = getMapNameWithIndex($pdo, $_GET['map'])->fetchColumn(0);
  $imagepath = getImagePathWithIndex($pdo, $_GET['map'])->fetchColumn(0);
  $coords = getAllCoordsForMap($pdo, $map_name)->fetchAll();

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
    <script src="includes/jquery-3.4.1.min.js"></script>
    <script src="includes/jquery.maphilight.min.js"></script>
    <script src="includes/imageMapResizer.min.js"></script>
    <script src="https://storage.googleapis.com/vrview/2.0/build/vrview.min.js"></script>
  </head>
  <body>
    <h1>
    </h1>
  <div class="row">
    <div class="column" id="image_map">
      <map name="coord_map">
        <?php
          foreach($coords as $coord){
            $coordarray = explode("," , $coord[0]);
            $convertedcoord = convertCoords($coordarray[0],$coordarray[1]);
            echo("<area 
                    href='javascript:newVrView(1);'
                    target='_self'
                    shape='circle'
                    coords='" . $convertedcoord[0] . "," . $convertedcoord[1] . ",2'
                    />");
          }
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
      window.addEventListener("load", function(){
        onVrViewLoad(0);
      });
      var images = [];
      images.push("images/converted.jpg");
      images.push("images/360.jpg")
      function onVrViewLoad(index) {
        var vrView = new VRView.Player("#vrview", {
          image: images[index],
          is_stereo: false,
          width: "100%",
          height: "100%"
        });
      }

      function newVrView(index){
        console.log("hello");
        var vrview = document.getElementById("vrview");
        vrview.innerHTML="";
        onVrViewLoad(index);

      }
    </script>
    </div>
    <script>
    imageMapResize();
    $('.map').maphilight();
    </script>
  </body>
</html>
