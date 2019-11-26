<?php
  require_once('includes/database.inc.php');
  cors();
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
    <script src="includes/imageMapResizer.min.js"></script>
    <script src="includes/jquery.maphilight.min.js"></script>
    <script src="https://storage.googleapis.com/vrview/2.0/build/vrview.min.js"></script>
  </head>
  <body>
    <h1>
    </h1>
  <div class="row">
    <div class="column" id="image_map">
      <map name="coord_map">
        <?php
        $index = 0;
          foreach($coords as $coord){
            $index = ($index + 1) % 2;
            echo("<area 
                    href='javascript:newVrView(" . $index . ");'
                    target='_self'
                    shape='circle'
                    coords='" . $coord[0] . "," . $coord[1] . ",2'
                  />");
          }
        ?>
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
      images.push("https:cu-indoorview.herokuapp.com/images/converted.jpg");
      images.push("https:cu-indoorview.herokuapp.com/images/360.jpg")
      function onVrViewLoad(index) {
        var vrView = new VRView.Player("#vrview", {
          image: images[index],
          is_stereo: false,
          width: "100%",
          height: "100%"
        });
      }

      function newVrView(index){
        var vrview = document.getElementById("vrview");
        vrview.removeChild(vrview.childNodes[0]);
        onVrViewLoad(index);
      }
    </script>
    </div>
    <script>
    imageMapResize();
    $.fn.maphilight.defaults = {
      fill: true,
      fillColor: 'ff0000',
      fillOpacity: 0.2,
      stroke: true,
      strokeColor: 'ff0000',
      strokeOpacity: 1,
      strokeWidth: 1,
      fade: true,
      alwaysOn: true,
      neverOn: false,
      groupBy: false,
      wrapClass: true,
      shadow: false,
      shadowX: 0,
      shadowY: 0,
      shadowRadius: 6,
      shadowColor: '000000',
      shadowOpacity: 0.8,
      shadowPosition: 'outside',
      shadowFrom: false
    }
    $('img[usemap]').maphilight();
    </script>
  </body>
</html>
