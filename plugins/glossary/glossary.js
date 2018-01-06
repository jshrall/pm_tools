<script>
// Handle glossary mouse events
f.showDefinition = function() {
    /* This is our handle on the div to show */
    var show = this.getAttribute("data-show");
    var definition = document.getElementById(show);
    var definition_arrow = document.getElementById(show + "arrow");

    /* Set the coordinates based on this element's position and set it to visible */
    var term_rect = this.getBoundingClientRect();
    var main_rect = document.getElementById("MAIN").getBoundingClientRect();
    var wl = main_rect.left;
    var wr = main_rect.right;

    // Margin should be same as width
    var arrow_margin = 10;

    /* setting display=block here allows us to discover the width. Without it, width is zero */
    definition.style.position = "absolute";
    definition_arrow.style.position = "absolute";
    definition.style.display = "block";
    definition_arrow.style.display = "block";

    // Vertically place the arrow first, then definition
    // Note that we need to handle scrolling, hence the addition of the window.pageYOffset
    // Also note that the arrow box is 2x the margin / linewidth. So goose it up by the margin to 
    // be as close as possible to the element we are pointing to.
    definition_arrow.style.top = (term_rect.bottom + window.pageYOffset - arrow_margin + 4) + "px";
    arrow_rect = definition_arrow.getBoundingClientRect();
    definition.style.top = (arrow_rect.bottom + window.pageYOffset) + "px";

    /* decide right or left aligned */
    if (wr - term_rect.right < definition.offsetWidth / 2) {
        /* anchor at the right, add a little padding for small acronyms */
        var left = term_rect.right - wl - definition.offsetWidth + arrow_margin;
        definition.style.left = left + "px";
    }
    else if (term_rect.left - wl < definition.offsetWidth / 2) {
        /* anchor at the left, add a little padding for small acronyms*/
        var left = term_rect.left - main_rect.left - arrow_margin;
        definition.style.left = left + "px";
    }
    else {
        /* anchor in the middle */
        var left = (((term_rect.right + term_rect.left) / 2) - wl - definition.offsetWidth / 2);
        definition.style.left = left + "px";
    }
    // Always place the arrow in the middle of the word
    definition_arrow.style.left = ((term_rect.right + term_rect.left) / 2 - wl - arrow_margin) + "px";
};

f.hideDefinition = function() {
    /* This is our handle on the div to show */
    var show = this.getAttribute("data-show");
    var definition = document.getElementById(show);
    var definition_arrow = document.getElementById(show + "arrow");
    definition.style.display = "none";
    definition_arrow.style.display = "none";
};

/* Get all glossary links and instantiate the pop-ups */
var classname = document.getElementsByClassName("glossary_link");

/* Assign a mouse over listener to each */
for (var i = 0; i < classname.length; i++) {
    classname[i].addEventListener('mouseover', f.showDefinition);
    classname[i].addEventListener('mouseout', f.hideDefinition);
}

</script>
