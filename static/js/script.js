$(document).ready(function(){
  /*mobile side nav bar */
    $('.sidenav').sidenav({edge: "right"});

  /*dropdowns on forms */
    $('select').formSelect();
  /*tool tip helpers */
    $('.tooltipped').tooltip();
  });

  /* tags - need to change data if using */
    $('.chips').chips();
    $('.chips-initial').chips({
      data: [{
        tag: 'Apple',
      }, {
        tag: 'Microsoft',
      }, {
        tag: 'Google',
      }],
    });
    $('.chips-placeholder').chips({
      placeholder: 'Enter a tag',
      secondaryPlaceholder: '+Tag',
    });
    $('.chips-autocomplete').chips({
      autocompleteOptions: {
        data: {
          'Apple': null,
          'Microsoft': null,
          'Google': null
        },
        limit: Infinity,
        minLength: 1
      }
    });

  