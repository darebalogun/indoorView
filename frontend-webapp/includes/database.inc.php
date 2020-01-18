<?php

    // Connect to database using credentials and return connection object
    function getConnectionInfo(){
        try {
            define('DBCONNECTION', 'mysql:host=sql9.freemysqlhosting.net;dbname=sql9317665');
            define('DBUSER', 'sql9317665');
            define('DBPASS', 'Rlkt5e4s9E');

            $pdo = new PDO(DBCONNECTION, DBUSER, DBPASS);
        } catch(PDOException $e){
            die($e->getMessage());
        }

        return $pdo;
    }

    // Get all maps stored in the database
    function getAllMaps($pdo){
        $sql = 'SELECT name FROM maps';
        return $pdo->query($sql);
    }

    // Get image path of the requested map
    function getImagePathWithIndex($pdo, $index){
        $sql = 'SELECT imagepath FROM maps WHERE id=' . $index;
        return $pdo->query($sql);
    }

    // Get name of requested map
    function getMapNameWithIndex($pdo, $index){
        $sql = 'SELECT name FROM maps WHERE id=' . $index;
        return $pdo->query($sql);
    }

    // Get allcoordinates of the map
    function getAllCoordsForMap($pdo, $map_name){
        $sql = 'SELECT mappedx, mappedy FROM ' . $map_name . ' ORDER BY id';
        return $pdo->query($sql);
    }

    function getAllImagePaths($pdo, $map_name){
        $sql = 'SELECT image_path FROM ' . $map_name . ' ORDER BY id';
        return $pdo->query($sql);
    }

    function cors() {

        // Allow from any origin
        if (isset($_SERVER['HTTP_ORIGIN'])) {
            // Decide if the origin in $_SERVER['HTTP_ORIGIN'] is one
            // you want to allow, and if so:
            header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}");
            header('Access-Control-Allow-Credentials: true');
            header('Access-Control-Max-Age: 86400');    // cache for 1 day
        }
    
        // Access-Control headers are received during OPTIONS requests
        if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    
            if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_METHOD']))
                // may also be using PUT, PATCH, HEAD etc
                header("Access-Control-Allow-Methods: GET, POST, OPTIONS");         
    
            if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']))
                header("Access-Control-Allow-Headers: {$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");
    
            exit(0);
        }
    
        echo "You have CORS!";
    }

?>