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
		<link
			href="//fonts.googleapis.com/css?family=Lora|Open+Sans"
			rel="stylesheet"
			type="text/css"
		/>
		<link rel="stylesheet" href="assets/css/main.css" type="text/css"/>
    	<script src="includes/jquery-3.4.1.min.js"></script>
    	<script src="includes/imageMapResizer.min.js"></script>
    	<script src="includes/jquery.maphilight.min.js"></script>
    	<script src="https://storage.googleapis.com/vrview/2.0/build/vrview.min.js"></script>
	</head>
	<body class="subpage">
		<style> 
			body {
				background-image:url(images/bluewhite.jpg)
			}		
		</style>
		<header id="header">
			<div class="logo"><a href="index.php">SYSC 4907</span></a></div>
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
				<li><a href="background.html">Background</a></li>
				<li><a href="applications.html">Applications</a></li>
				<li><a href="about us.html">About Us</a></li>
			</ul>
		</nav>

		<div id="main">
			<section class="wrapper">
				<div class="inner">
					<header class="align-center">
						<span class="image right"><img src="images/IV.JPG" alt="" /></span><h1><?php echo $map_name ?></h1>
					</header>
						<div class="align-left">
							<h2>Explore and find your way around Carleton Univeristy.</h2>
							<h5>Click on different areas of the map to view a panoramic dispaly of the indoor space.</h5>						
						</div>
				</div>
			</section>
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
				<div id="vrview" class="column vrview"></div>
					<script>
						window.addEventListener("load", function(){
							onVrViewLoad(0);
						});
						var images = [];
						var image_count = <?php echo $index + 1?>;
						var i;
						for (i = 0; i < image_count; i++){
							var j = i + 1;
							images.push("images/" + "<?php echo $map_name ?>" + "/image" + j.toString() + ".jpg" );
						}
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