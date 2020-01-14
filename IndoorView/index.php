<?php
  require_once('includes/database.inc.php');
  $pdo = getConnectionInfo();
  $maps = getAllMaps($pdo); 
?>
<!DOCTYPE HTML>

<html>
	<head>
		<title>IndoorView</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<link rel="stylesheet" type="text/css" href="assets/css/style.css" />

	</head>
	<body>

		<!-- Header -->
			<header id="header" class="alt">
				<div class="logo"><a href="index.html">SYSC 4907 </a> </div>
				
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

		<!-- Banner -->
			<section id="banner">
				<div class="inner">
					<header>
						<h1>IndoorView
						
						</h1>
						<p>An Interactive Panoramic Viewing System for Indoor Spaces</p>
					</header>
					<h1>
					<h3>
					<?php
						$count = 0;
						foreach ($maps as $map){
						$count++;
						echo("<a href='map.php?map=" . $count . "' class='button' style='margin:8px;'>" . $map[0] . "</a>"); 
						}
					?>
					</h3>
				</div>
			</section>

	

	<!-- Scripts -->
	<script src="assets/js/jquery.min.js"></script>
	<script src="assets/js/jquery.scrolly.min.js"></script>
	<script src="assets/js/jquery.scrollex.min.js"></script>
	<script src="assets/js/skel.min.js"></script>
	<script src="assets/js/util.js"></script>
	<script src="assets/js/main.js"></script>

</body>
</html>