

document.addEventListener("DOMContentLoaded",function(event){

    // Get the Sidebar
    var mySidebar = document.getElementById("mySidebar");

    // Get the DIV with overlay effect
    var overlayBg = document.getElementById("myOverlay");

    //Get NAVANCHOR
    var navAnchor = document.getElementById("navAnchor");
    
    navAnchor.addEventListener("click",w3_open);
    overlayBg.addEventListener("click",w3_close);
    mySidebar.addEventListener("click",w3_close);

});

// Toggle between showing and hiding the sidebar, and add overlay effect
function w3_open() {
    if (mySidebar.style.display === 'block') {
        mySidebar.style.display = 'none';
        overlayBg.style.display = "none";
    } else {
        mySidebar.style.display = 'block';
        overlayBg.style.display = "block";
    }
}

// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
    overlayBg.style.display = "none";
}
