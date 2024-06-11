<?php
$firstName = $_POST['FullName'];
$number = $_POST['MobileNumber'];
$marks = $_POST['Cut-off'];
$course = $_POST['course']

//database connection
$conn = new mysqli('localhost','root','','userdata');
if 
($conn->connect_error) 

{die
('Connection Failed : '.$conn->connect_error);
}

else { 
    $stmt = $conn->prepare 
    ("insert into registration(FullName,MobileNumber,Cut-off,course) values(?,?,?,?)")
}

  $stmt->bind_param("siis",$FullName, $MobileNumber, $CutOff,$course );
  $stmt->execute();
  echo "College Fetched Successfully...";
  $stmt->close();
  $conn->close();
?>