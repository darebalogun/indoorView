<!--* @Author: Zoya Mushtaq 
      @Author: Dare Balogun 
 *    @Date:   2020-03-01
 *    @Last Modified by: Zoya Mushtaq -->

 <!--Map Page used to dispaly the image maps and panormic image dispaly-->


<?php
  require_once('includes/database.inc.php');
  $pdo = getConnectionInfo();
  $map_name = getMapNameWithIndex($pdo, $_GET['map'])->fetchColumn(0);
  $imagepath = getImagePathWithIndex($pdo, $_GET['map'])->fetchColumn(0);
  $coords = getAllCoordsForMap($pdo, $map_name)->fetchAll();
  $images360 = getAllImagePaths($pdo, $map_name)->fetchAll();	
  $maps = getAllMaps($pdo);
?>

<!DOCTYPE HTML>

<html>

	<meta name="pinterest" content="nopin" />
	<head>
		<title>Indoor View</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
    
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.css">

		<link rel="stylesheet" href="assets/css/main.css" type="text/css"/>
    	<script src="includes/jquery-3.4.1.min.js"></script>
    	<script src="includes/imageMapResizer.min.js"></script>
    	<script src="includes/jquery.maphilight.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.js"></script>
        <link rel="stylesheet" href="https://cdn.pannellum.org/2.3/pannellum.css"/>
		<script type="text/javascript" src="https://cdn.pannellum.org/2.3/pannellum.js"></script>
    </head>
	<body class="subpage">
		<style> 
			body {
				background-image:url(images/bluewhite.jpg)
			}		
		</style>
		<header id="header">
			<div class="logo"><a href="index.php">IndoorView</span></a></div>
			<a href="#menu">Menu</a>
		</header>
		<nav id="menu">
			<ul class="links">
				<li><a href="index.php">Home</a></li>
				<li><a href="#">Maps</a>
					<ul>
						<?php
							$count = 0;
							foreach ($maps as $map){
								$count++;
								echo("<li><a href='map.php?map=" . $count . "'>" . $map[0] . "</a></li>"); 
							}
						?>
					</ul>
				</li>
				<li><a href="background.php">Background</a></li>
				<li><a href="applications.php">Applications</a></li>
				<li><a href="about us.php">About Us</a></li>
			</ul>
		</nav>

		<div id="main">
			<section class="wrapper">
				<div class="inner">
					<header class="align-center">
						<span class="image right"><img src="images/IV.JPG" alt="" /></span><h1><?php echo $map_name ?></h1>
					</header>
						<div class="align-left">
							<h2>Explore and find your way around Carleton University.</h2>
							<h5>Click on different reference areas on the map to view a panoramic dispaly of the indoor space.</h5>	
							<button id="myBtn" class="bigbutton" width="60" height="100">Controls Functionality</button>				
						</div>
				</div>
			</section>



			<!-- modal begin  -->

			<!-- Trigger/Open The Modal -->
					

					<!-- The Modal -->
				<div id="myModal" class="modal">

					<!-- Modal content -->
						<div class="modal-content">
							<span class="modclose">&times;</span>
							<h2>Controls Functionality</h2>

							<table>
									<tr>
										<td>Symbol</td>
										<th>Functionality</th>

									</tr>
									<tr>
										<td><div class="ctrl">&#x25B2; </div></td>
										<th><h5>Navigate forward to the next image in the map</h5></th>
									</tr>
									<tr>
										<td><div class="ctrl">&#9660;</div></td>
										<th><h5> Navigate backward to the previous image in the map</h5></th>
									</tr>
									<tr>
										<td><div class="ctrl">&#x25C0;</div></td>
										<th><h5> Navigate left in the image</h5></th>
									</tr>
									<tr>
										<td><div class="ctrl" >&#9654;</div></td>
										<th><h5>Navigate right in the image</h5></th>
									</tr>
									<tr>
										<td><div class="ctrl" >&plus;</div></td>
										<th><h5> Zoom in </h5></th>
									</tr>
									<tr>
										<td><div class="ctrl" >&minus;</div></td>
										<th><h5> Zoom out </h5></th>
									</tr>
									<tr>
										<td><div class="ctrl">&#x2922;</div></td>
										<th><h5> Enter full screen mode</h5></th>
									</tr>
							</table>

						</div>

				</div>

				<script>
						// Get the modal
						var modal = document.getElementById("myModal");

						// Get the button that opens the modal
						var btn = document.getElementById("myBtn");

						// Get the <span> element that closes the modal
						var span = document.getElementsByClassName("modclose")[0];

						// When the user clicks the button, open the modal 
						btn.onclick = function() {
						modal.style.display = "block";
						}

						// When the user clicks on <span> (x), close the modal
						span.onclick = function() {
						modal.style.display = "none";
						}

						// When the user clicks anywhere outside of the modal, close it
						window.onclick = function(event) {
						if (event.target == modal) {
							modal.style.display = "none";
						}
						}
				</script>


			<!-- modal end -->

			<!-- image map reference area overlay -->

			<div class="row">
				<div class="column map" id="image_map">
    				<map name="coord_map">
						<?php
							foreach($coords as $index=>$coord){
								echo("<area 
										href='javascript:newVrView(" . $index . ");'
										target='_self'
										shape='circle'
										coords='" . $coord[0] . "," . $coord[1] . ",12'	 
										/>");
								}
						?>
					</map>
						<?php
							echo('<img src="'. $imagepath .'" usemap="#coord_map"/>')	
						?>

				</div>

				<!-- control bar display -->

                <div id="panorama" class="column vrview"></div>
                            <div id="panorama">
								<div id="controls">
									<div class="ctrl" id="pan-up">&#x25B2;</div>
									<div class="ctrl" id="pan-down">&#9660;</div>
									<div class="ctrl" id="pan-left">&#x25C0;</div>
									<div class="ctrl" id="pan-right">&#9654;</div>
									<div class="ctrl" id="zoom-in">&plus;</div>
									<div class="ctrl" id="zoom-out">&minus;</div>
									<div class="ctrl" id="fullscreen">&#x2922;</div>
								</div>
							</div>
                        
					<script>
						var remember = 0;

                    // Create viewer
								viewer = pannellum.viewer('panorama', {
									"type": "equirectangular",
									"panorama": "images/" + "<?php echo $map_name ?>" + "/image1.jpg",
									"autoLoad": true,
									"showControls": false,
									"sceneFadeDuration": 10000
								});


						
						var images = [];
						var image_count = <?php echo $index + 1?>;
						var i;
						
						for (i = 0; i < image_count; i++){
							var j = i + 1;
							images.push("images/" + "<?php echo $map_name ?>" + "/image" + j.toString() + ".jpg" );
						}

						//panoramic image display in reference to hotspot

						function onVrViewLoad(index) {
							viewer = pannellum.viewer('panorama', {
													"type": "equirectangular",				
													"panorama":"images/" + "<?php echo $map_name ?>" + "/image" + (index + 1).toString() + ".jpg",
													"autoLoad": true,
													"showControls": false,
													"sceneFadeDuration": 10000 
													});
							remember = index;

							}
						
						//delete previous display

						function newVrView(index){
							var vrview = document.getElementById("panorama");
							vrview.removeChild(vrview.childNodes[0]);
							onVrViewLoad(index);
						}


	
                        // Make buttons work
							document.getElementById('pan-up').addEventListener('click', function(e) {
								if(remember == (image_count -1)){
									onVrViewLoad(0);
								}else{
									onVrViewLoad(remember + 1);
								} 
							});
							document.getElementById('pan-down').addEventListener('click', function(e) {
								if(remember == (0)){
									onVrViewLoad(image_count - 1); 
								}else{
									onVrViewLoad(remember - 1);
								}
							});
							document.getElementById('pan-left').addEventListener('click', function(e) {
								viewer.setYaw(viewer.getYaw() - 10);
							});
							document.getElementById('pan-right').addEventListener('click', function(e) {
								viewer.setYaw(viewer.getYaw() + 10);
							});
							document.getElementById('zoom-in').addEventListener('click', function(e) {
								viewer.setHfov(viewer.getHfov() - 10);
							});
							document.getElementById('zoom-out').addEventListener('click', function(e) {
								viewer.setHfov(viewer.getHfov() + 10);
							});
							document.getElementById('fullscreen').addEventListener('click', function(e) {
								viewer.toggleFullscreen();
							});
					</script>
			</div>
			<script>
				imageMapResize();
				$.fn.maphilight.defaults = {
				fill: true,
				fillColor: 'ff0000',
				fillOpacity: 0.1,
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
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>