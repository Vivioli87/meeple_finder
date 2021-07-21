document.addEventListener("DOMContentLoaded", function(){

    let resetButton = document.getElementsByClassName("reset-button")[0];
    resetButton.addEventListener("click", refreshPage);

    let backButton = document.getElementsByClassName("back-button")[0];
    backButton.addEventListener("click", goBack);

    let dropdowns = ['min_player', 'max_player', 'playing_time', 'type', 'use']
    dropdowns.forEach(dropdownValue);

})


/* function to go back to previous page */
function goBack() {
    window.history.back();
  };

/* function to reset forms/refresh page */
function refreshPage() {
    window.location.reload();
  };

  /*function to populate game information on dropdowns when editing game*/
function dropdownValue(selectId) {
  try {
    let initval = document.getElementById(selectId).getAttribute("initval");
    document.getElementById(selectId).value = initval;
  } catch (error) {}
  };