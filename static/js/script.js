/*function to populate game information on dropdowns when editing game*/
function dropdownValue(selectId, selectValue) {    
  document.getElementById(selectId).value = selectValue;
  console.log(selectId, selectValue)
};

/* function to go back to previous page */
function goBack() {
  window.history.back();
};


$(document).ready(function(){
  /*mobile side nav bar */
    $('.sidenav').sidenav({edge: "right"});

  /*dropdowns on forms */
    $('select').formSelect();
  /*tool tip helpers */
    $('.tooltipped').tooltip();
  /*modal to confirm deletions*/
    $('.modal').modal();
});

  