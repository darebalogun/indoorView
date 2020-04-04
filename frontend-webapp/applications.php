<!--* @Author: Zoya Mushtaq 
 *    @Date:   2020-03-01
 *    @Last Modified by: Zoya Mushtaq -->

 <!--Applications Page used as the starting hub of the web application-->
<?php
  require_once('includes/database.inc.php');
  $pdo = getConnectionInfo();
  $maps = getAllMaps($pdo); 
?>
<!DOCTYPE HTML>

<html>

		<meta name="pinterest" content="nopin" />
	<head>
		<title>Applications</title>
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
					<div class="logo"><a href="index.php">IndoorView</span></a></div>
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
									<h1>Applications</h1>
								<h5>Refer below to read about the different applications of IndoorView</h5>
							</header>
							<div class="flex flex-2">
								<div class="col col2">
									<h7 id="content">Adds viewing functionality to Carleton University's current Campus Map Tool </h7>
									<h3>IndoorView contians an indoor viewing functionality that Carleton University's current Campus Map Tool does not possess.</h3>
									<h6>Carleton University currently has a <a href="https://carleton.ca/campus/map/"><b style="text-decoration:underline;">Campus Map Tool</b></a>  which allows users to view Carleton’s campus from a bird’s eye view. IndoorView is being created to overcome some of the limitations of this mapping tool. The current tool allows users to visually navigate through the campus by clicking on different buildings. When a user clicks on a building on the map a new window displays the outdoor view of that particular building. However, there is no way to view the inside of the buildings. </h6>
									<h6>This is where IndoorView comes in! IndoorView would allow users to view the inside of buildings of Carleton University. IndoorView would display a panoramic view of the inside of the building at specified areas. An application like this is very useful as it is easy to get lost when navigating though the buildings and a visual display of the inside would be very helpful to users. </h6>
								</div>
								<div class="col col1 first">
									<div >
										<a href="https://carleton.ca/campus/map/" class="image main"><img src="images/cuCampusMap.JPG" alt="" /></a>
									</div>
								</div>
							</div>

							<div class="flex flex-2">
								<div class="col col2">
								<h7 id="content">Real Estate Showing  </h7>
								<h6>IndoorView’s 3D view of any building or venue allows for a deeply engaged view of the environment. With IndoorView, one can easily visualize the indoor environment of any building in 3D, which allows for many benefits.  This technology has the potential of transforming the way Real Estate Agents advertise and market buildings. IndoorView can offer home buyers and audiences an immersive experience, which gives them a clear idea of the area they are interested in buying. It gives real estate agents the ability to host an indoor view of home listings. Then, home-buyers can view these listings and have a 3D tour of the space. Initially, in the first assessments of homes, it will allow home buyers to view much more homes in the same period. Therefore, IndoorView can be optimized to be a powerful communication device in the real estate market, when compared to the conventional methods used.</h6>
								
							</div>
								<div class="col col1 first">
									<div >
										
										<a href="" class="image main"><img src="images/realestate.JPG" alt="" /></a>
										
									</div>
								</div>


								<div class="flex flex-2">
										<div class="col col2">
										<h7 id="content">Augmented Reality </h7>
										<h6>Augmented Reality (AR) allows applications that make use of computer-generated perceptual information to be ‘augmented’ or embedded in real world images. In this application the system being developed would be able to generate a realistic walk-through of a room or space and then offer this to developers and artists to add AR models. One example of a use case of this could be in a museum exhibit. Users would be able to view the indoor view of the museum with life size exhibits added in using AR.</h6>
										
									</div>
										<div class="col col1 first">
											<div >
												
												<a href="" class="image main"><img src="images/ar.JPG" alt="" /></a>
											</div>
										</div>
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