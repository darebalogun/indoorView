<?php
    // Connect to database using credentials and return connection object
    function getConnectionInfo(){
        try {
            define('DBCONNECTION', 'mysql:host=127.0.0.1;dbname=indoorview');
            define('DBUSER', 'admin');
            define('DBPASS', 'admin');

            $pdo = new PDO(DBCONNECTION, DBUSER, DBPASS);
        } catch(PDOException $e){
            die($e->getMessage());
        }

        return $pdo;
    }

    function getAllMaps($pdo){
        $sql = 'show tables from indoorview';
        return $pdo->query($sql);
    }

    function getImagePathWithIndex($pdo, $index){
        $sql = 'SELECT imagepath FROM maps WHERE id=' . $index;
        return $pdo->query($sql);
    }

    function getMapNameWithIndex($pdo, $index){
        $sql = 'SELECT name FROM maps WHERE id=' . $index;
        return $pdo->query($sql);
    }

    function getAllCoordsForMap($pdo, $map_name){
        $sql = 'SELECT coordinates FROM ' . $map_name;
        return $pdo->query($sql);
    }

    function convertCoords($x, $y){
        $floatx = ((float) $x)/0.05 + 80;
        $floaty = (-1*((float) $y))/0.05 + 80;
        return array($floatx, $floaty);
    }


?>