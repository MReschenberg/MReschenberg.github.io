function openNav() {
    document.getElementById("sidebar").style.transition = ".2s";
   document.getElementById("mySidenav").style.transition = "1.5s";
	document.getElementById("sidebar").style.width = "0px";
    document.getElementById("mySidenav").style.width = "150px";
}

function closeNav() {
    document.getElementById("mySidenav").style.transition = ".2s";
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("sidebar").style.transition = "1.5s";
    document.getElementById("sidebar").style.width = "50px";
}