function openNav() {
    document.getElementById("mySidenav").style.width = "150px";
    document.getElementById("maintext").style.marginLeft = "150px";
    document.getElementById("maintext").style.width = "80%";
    document.getElementById("sidebar").style.dispaly = 'none';

}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("maintext").style.marginLeft = "50px";
    document.getElementById("maintext").style.width = "90%";
    document.getElementById("sidebar").style.dispaly = '';


}