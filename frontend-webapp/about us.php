<!--* @Author: Zoya Mushtaq 
 *    @Date:   2020-03-01
 *    @Last Modified by: Zoya Mushtaq -->

 <!--About Us Page used to dispaly the team members roles -->

<?php
  require_once('includes/database.inc.php');
  $pdo = getConnectionInfo();
  $maps = getAllMaps($pdo); 
?>
<!DOCTYPE HTML>
<html>
		<meta name="pinterest" content="nopin" />
	<head>
		<title>About Us</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body class="subpage">

			<style> 
					body {
						background-image:url(images/bluewhite.jpg)
					}
					
			</style>

		<!-- Header -->
			<header id="header">
				<div class="logo"><a href="index.php">IndoorView</a></div>
				<a href="#menu">Menu</a>
			</header>

		<!-- Nav -->
		
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

		<!-- Main -->
			<div id="main">

				<!-- Section -->
					<section class="wrapper2">
						<div class="inner">
							<header class="align-center">
								<h1>About Us</h1>
								<h5>Refer below to learn a little bit about our team and the contributions of each team member</h5>
							</header>
							

				<!-- Section -->
					<section class="wrapper2">

						
						<div class="inner">
							
							<div class="flex flex-3">
								<div class="col align-center">
									<div class="image round">
										<img src="images/emad.png" alt="" />
									</div>
									<h4>Emad Arid </h4>
									<h6>Emad Arid is an Electrical Engineering student and worked on the development of the image capturing system.</h6>						
								</div>
								<div class="col align-center">
									<div class="image round">
										<img src="images/zoya.png" alt="" />
									</div>
									<h4>Zoya Mushtaq </h4>
									<h6>Zoya Mushtaq is a Computer Systems Engineering student and worked on the design and development of the Graphical User Interface (Web Application). </h6>	
								</div>
								<div class="col align-center">
									<div class="image round">
										<img src="images/greg.png" alt="" />
									</div>
									<h4>Gregory Koloniaris </h4>
									<h6>Gregory Koloniaris is an Electrical Engineering student and worked on the development of the wireless image capturing control and image transfer system. </h6>	
								</div>

								<div class="col align-center">
									<div class="image round">
										<img src="images/dare.jpg" alt="" />
									</div>
									<h4>Dare Balogun </h4>
									<h6>Dare Balogun is a Computer Systems Engineering student and worked on the data collection process and indoor localization algorithm.</h6>	
								</div>

								<div class="col align-center">
									<div class="image round">
										<img src="images/placeholder.jpg" alt="" />
									</div>
									<h4>Anannya Bhatia </h4>
									<h6>Anannya Bhatia is a Computer Systems Engineering student and worked on the image filtering script. </h6>						
								</div>

								<div class="col align-center">
									<div class="image round">
										<img src="images/atia.jpg" alt="" />
									</div>
									<h4>Dr. Mohamed Atia </h4>
									<h6>Dr. Mohamed Atia is the project supervisor and a professor at Carleton University. He oversaw the progress and development of the project and advised on project decisions.  </h6>						
								</div>
								
							</div>
						</div>
					</section>

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