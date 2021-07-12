
function dropdownValue(selectId, selectValue) {    
  document.getElementById(selectId).value = selectValue;
  console.log(selectId, selectValue)
};



$(document).ready(function(){
  /*mobile side nav bar */
    $('.sidenav').sidenav({edge: "right"});

  /*dropdowns on forms */
    $('select').formSelect();
  /*tool tip helpers */
    $('.tooltipped').tooltip();

});

  