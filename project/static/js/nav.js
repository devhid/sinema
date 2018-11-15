$('.has-sub').on('click', function(e) { // Get all dropdown menu toggles
    $('.dropdown-menu').not($(this).children('.dropdown-menu')).removeClass('dropdown-shown'); // Hide all other dropdown menus
    $('.has-sub').not($(this)).removeClass('active'); // Remove the active selector from the other dropdown toggles
    $(this).children('.dropdown-menu').toggleClass('dropdown-shown'); // Show/hide the dropdown menu associated with the toggle being clicked
    $(this).toggleClass('active'); // Toggle the active selector on the nav-item
});

// Get all the nav-btns in the page
let navBtns = document.querySelectorAll('.nav-btn');

// Add an event handler for all nav-btns to enable the dropdown functionality
navBtns.forEach(function (ele) {
    ele.addEventListener('click', function() {
        // Get the dropdown-menu associated with this nav button (insert the id of your menu)
        let dropDownMenu = document.getElementById('#user-menu');

        // Toggle the nav-btn and the dropdown menu
        ele.classList.toggle('active');
        dropDownMenu.classList.toggle('active');
    });
});

