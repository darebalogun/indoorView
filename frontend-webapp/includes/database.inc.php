<?php

    function getConnectionInfo(){
        try {
            define('DBCONNECTION', 'mysql:host=127.0.0.1;dbname=indoorview');
            define('DBUSER', 'admin');
            define('DBPASS', 'admin');

            $pdo = new PDO(DBCONNECTION, DBUSER, DBPASS);
            //$pdo->setAttribute(PDO::ATTR_ERMODE, PDO::ERRMODE_EXCEPTION);
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
        $sql = 'SELECT name FROM maps WHERE id=' .$index;
        return $pdo->query($sql);
    }


?>