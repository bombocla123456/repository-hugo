
const selection_jours = document.getElementById("jours");
selection_jours.addEventListener("change", function() {
    const url=this.value ;
    if (url !== "") {
        window.location.href=url ;
    }
} );

selection_jours.selectedIndex = 0;

const selectione_jours = document.getElementById("jour");
selectione_jours.addEventListener("change", function() {
    const url_2=this.value ;
    if (url_2 !== "") {
        window.location.href=url_2 ;
    }
} );

selectione_jours.selectedIndex = 0;