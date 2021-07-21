/* jquery from Materialize function */
$(document).ready(function(){
  /*mobile side nav bar */
    $('.sidenav').sidenav({edge: "right"});

  /*dropdowns on forms */
    $('select').formSelect();
  /*tool tip helpers */
    $('.tooltipped').tooltip();
  /*modal to confirm deletions*/
    $('.modal').modal();
  /*collapsible for search bar*/
    $('.collapsible').collapsible();
});

  