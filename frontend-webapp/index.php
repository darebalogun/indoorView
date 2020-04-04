<!--* @Author: Zoya Mushtaq 
 *    @Date:   2020-03-01
 *    @Last Modified by: Zoya Mushtaq -->

 <!--Home Page used as the starting hub of the web application-->
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
		<header id="header" class="alt">
			<div class="logo"><a href="index.php">IndoorView</a> </div>
			<a href="#menu">Menu</a>			
		</header>
		<nav id="menu">
			<ul class="links">
				<li><a href="index.php">Home</a></li>
				<li><a href="#">Maps</a>
					<ul>
						<?php
              $count = 0;
              $map_array = array();
							foreach ($maps as $map){
                $count++;
                array_push($map_array, $map);
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
		<section id="banner">
			<div class="inner">
				<header>
					<h1>IndoorView</h1>
					<p>An Interactive Panoramic Viewing System for Indoor Spaces</p>
				</header>
				<h1>
				<h3>
        <?php
          $count = 0;
					foreach ($map_array as $map){
            $count++; 
					  echo("<a href='map.php?map=" . $count . "' class='button' style='margin:8px;'>" . $map[0] . "</a>"); 
					}
				?>
				</h3>
			</div>
    </section>
  <script src="assets/js/jquery.min.js"></script>
	<script src="assets/js/jquery.scrolly.min.js"></script>
	<script src="assets/js/jquery.scrollex.min.js"></script>
	<script src="assets/js/skel.min.js"></script>
	<script src="assets/js/util.js"></script>
	<script src="assets/js/main.js"></script>
</body>
</html>