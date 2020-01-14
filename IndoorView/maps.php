<?php
  require_once('includes/database.inc.php');
  //cors();
  $pdo = getConnectionInfo();
  $map_name = getMapNameWithIndex($pdo, $_GET['map'])->fetchColumn(0);
  $imagepath = getImagePathWithIndex($pdo, $_GET['map'])->fetchColumn(0);
  $coords = getAllCoordsForMap($pdo, $map_name)->fetchAll();

?>

<!DOCTYPE HTML>

<html>

	<meta name="pinterest" content="nopin" />
	<head>
<<<<<<< 795f3f9962e58c092e74d037199a1cd95f2c4853:IndoorView/maps.html
		<title>Mackenzie</title>
=======
		<title>Indoor View</title>
>>>>>>> Merge frontend design attempt:IndoorView/maps.php
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="assets/css/main.css" type="text/css"/>
		<link href="styles/style.css" rel="stylesheet" type="text/css" />
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

		<!-- Header -->
			<header id="header">
				<div class="logo"><a href="index.html">SYSC 4907</span></a></div>
				<a href="#menu">Menu</a>
			</header>

		<!-- Nav -->
		
		<nav id="menu">

				
				<ul class="links">
					<li><a href="index.html">Home</a></li>
					<li><a href="#">Maps</a>
						<ul>
								<li><a href="maps.html">Mackenzie L4</a></li>
								<li><a href="minto.html">Minto L7</a></li>
								<li><a href="tunnels.html">Tunnels</a></li>

						</ul>
					</li>
					<li><a href="background.html">Background</a></li>
					<li><a href="applications.html">Applications</a></li>
					<li><a href="about us.html">About Us</a></li>
				</ul>
			</nav>

		<!-- Main -->
			<div id="main">

				<!-- Section -->
					<section class="wrapper">
						<div class="inner">
							<header class="align-center">

								<p><span class="image right"><img src="images/IV.JPG" alt="" /></span><h1>Mackenzie Building - Level 4</h1></p>

							</header>

							<div class="align-left">

								<h2>Explore and find your way around Carleton Univeristy.</h2>

								<ul >
								<li><h5>Click on different areas of the map to view a panoramic dispaly of the indoor space.</h5></li>
								<li><h5>Search for specific rooms in the building using the search bar.</h5></li>

								</ul>

								<form method="post" action="#">
										<div class="row uniform">
											<div class="searchbar">
												<input type="text" name="query" id="query" value="" placeholder = "Enter room number" />
											</div>
											<div class="searchbar">
												<input type="submit" value="Search" class="fit" position: absolute; />
											</div>
										</div>
									</form>								
							</div>
							
							
							<div class="column" id="image_map">
      							<map name="coord_map">
									<?php
									$index = 0;
									foreach($coords as $coord){
										echo("<area 
												href='javascript:newVrView(" . $index . ");'
												target='_self'
												shape='circle'
												coords='" . $coord[0] . "," . $coord[1] . ",2'
											/>");
										$index = $index + 1;
									}
									?>
								</map>
								<?php
									echo('<img src="'. $imagepath .'" usemap="#coord_map" />')
								?>
    							</div>


							

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>