# Meeple Finder
## Meeting Meeples is easy...

[Main README.md file]()

[Please view the live project here](http://meeple-finder.herokuapp.com/)

## Table of contents

1. [User Stories Testing](#user-stories-testing)
2. [Code Validation](#code-validation)
3. [Functionality Testing](#functionality-testing)
4. [Performance Testing](#performance-testing)
5. [Encountered Issues](#encountered-issues)

## User Stories Testing

### Visitor Stories

1. As a site visitor, I would like to search a list of board games based on different criteria e.g. number of players, game type, game manufactorer, age level etc.
    - Currently the user can search by free text over the name, description, themes and mechanisms. There is also a filter by game theme/mechanisms option.
    -More filtering options will be added on the list for future implimentation.
2. As a site visitor, I would like to register an account that is secure and private.
    - The site runs on a secure https page. When registering an account the password is hashed before submitting it to the database to ensure that the actual password is never stored anywhere. 
3. As a site visitor, I would like a personalised dashboard to show board games I have in my collection, a wishlist for games I would like to have in my collection which I can easily add to when searching for games.
    - The profile page has a collection and wishlist section where games they have added to either will be kept.
    - Games can be moved from the wishlist to the collection (also removes from wishlist) or removed completely from either list.
    - Each game overview card on the games list will have a link to "add to collection" and "add to wishlist". Users will see a flash message to confirm the action has been completed.
4. As a site visitor, I would like to be able to add reviews but also to edit and delete the reviews if required. I should also be the only user who can edit or delete my reviews, other users can only view them.
    - Users can add reviews on the game's detail page and it will only be them who can edit or delete these. Other users will only be able to see the review.
5. As a site visitor, I would like to be able to add or request to add a game to the board game list if it is not currently listed on the site.
    - Users can add a game to the games list, which will then be reviewed by admin to 1) upload an image the site can use freely and 2) check that the information entered is accurate and appropriate.
6. As a site visitor, I would like to have games that are suggested to me based on the board games in my collection. (*potential future*)
    - See future implementation section
7. As a site visitor, I would like to find board game retailers or cafe's where I can buy or try out new board games on my wishlist.  (*potential future*)
    - See future implementation section
8. As a site visitor, I would like a website that is intuitive, easy to navigate and provides clear feedback on any actions I make (e.g when adding reviews, games etc)
    - The site is easy to navigate with the navbar and call to action buttons. 
    - Each action taken by the user such as adding a game, editing a review or even logging in has a flash message attach to provide clear feedback to the user about what has happened.
9. As a site visitor, I would like a glossary of board game terms used if I am unfamiliar with the terminology.
    - There is a tag list which explains all the different game mechanisms terminology and themes, there is a button for this list on key pages where this glossary might be useful. On these pages it opens in a new tab so that the user is not directed away from the page they were on.


### Business Stories

1. As a site owner, I would like to create a commuinty website where board game enthusiasts (new and old) can share their reviews and seek reccomendations on different board games.
    - Users are able to leave reviews on games that they have played to help recommend games to other users.
2. As a site owner, I would like a site that's easy to navigate, is intuitive and has eye-catching design.
    - Colour scheme and design is consistent throughout the site and the nav bar is present on all pages.
    - The site is intuitive, easy to navigate and understand through its use of colourful buttons, links and icons.
3. As a site owner, I would like for visitors to sign up to the community and add their reviews or reccomendations of board games to help fellow enthusiasts.
     - Users are able to leave reviews on games that they have played to help recommend games to other users.
4. As a site owner, I would like adding reviews to be accessed by registered users only. Non registered users can only view board game listings and their reviews.
    - non registered users can see the games and reviews on the site but cannot add or update any information themselsves.
    - Registered users can add games, add tags (both to be reviewd by admin) and also add reviews. Users can only edit and delete their own reviews.
5. As a site owner, I would like users to be able to edit and/or delete their own reviews only.
    - Buttons to update or delete reviews will only appear next the reviews where the creator matches the user that is logged in.
6. As a site owner, I would like users to be able to add or request to add a game to the board game list if it is not currently listed on the site.
    - Users can add a game to the games list, which will then be reviewed by admin to 1) upload an image the site can use freely and 2) check that the information entered is accurate and appropriate.
7. As a site owner, I would like to have admin access to be able to view, edit and delete any records that may be inaccurate or inappropriate for the website.
    - Admin have their own account. When logged in as Admin the profile page shows them games that havent been reviewd yet, these will all have the stock placeholder image.
    - The game cards on the admin page have update/delete buttons which takes you to an edit game page with the previously inputted information is populated.
8. As a site owner, I would like to support local board games shops and cafes by having a google maps API for users to find shops/cafes local to them. (*potential future*)
    - See future implementation section


[Back to table of contents](#table-of-contents)

## Code Validation

Every page of the project was validated by the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) to ensure there were no syntax errors or issues.

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate CSS code.

[jshint.com](https://jshint.com/) was used to check JS code.

[Python syntax checker](https://extendsclass.com/python-tester.html)

### W3C Markup Validation Service

Checked using validate by URI options.

Have checked all pages, a few issues noted regarding incorrect placement of title on 2 pages and an unclosed div on 2 other pages. Both issues now fixed.
The validation also reminded me to add alt tags to the images which I had previously forgotten to include.

Only warning now showing is regarding a section without a heading. This is relating to the flashes section on the base page.
This does have a heading but is wrapped in a divs so have ignored this warning.


### W3C CSS Validation Service

Checked using direct input.
Entered both style.css and games.css and no errors were found.

### jshint.com

When using jshint ensue to enable the "New JavaScript features (ES6)" in the configure tab. 

As a result of this check I've added missing semi colons and removed unneccessary ones.
The checker advised of unused 3 unused variables (dropdownValue, goBack, refreshPage) however these are used within the websites pages as explained in the javascript comments.

### Python syntax checker

checked syntax using [Python syntax checker](https://extendsclass.com/python-tester.html) as week as the "Problems" tab in gitpod. No Pep8 issues seen in final code, these have been fixed along the way.

There are warnings regarding the pagination code, this code was taken from an online source and works in its current format. I tried to alter it based off the warnings however this made the code not function, therefore I have left the code as it was and ignored the warnings.


## Functionality Testing

- Feature testing on each page in turn and for all screen sizes using the developer tools, my own personal devices and got friends/family to test also.
    - Checked for broken links
    - Checked 404 page works if there is a broken link/an incorrect url is used.
    - Checked logged in required decorator works so if a page that requires login is attempted while logged out, the visitor will be directed to the login page.
    - Checked filter and search function work as expected.
    - Checked all prepulated information works on edit pages.
    - Checked responsiveness of website so that no elements are hidden or have not formatted correctly.

### Browser Testing

The website was tested on the following browser types. All browser versions were up to date.
- **Google chrome** - best performance with all cookies allowed.
- Firefox
- Safari
- Edge
- Opera (tested on ubuntu Linux)
- Samsung Internet
- Google chrome for Android 

The website does not work as well on Internet Explorer (styling of game cards in grid view doesn't seem to work), please use Edge if you need to use a microsoft browser.

The website is functioning and fully responsive on all above mentioned browsers.

### Device Testing

For all my media queries, I used the following page for help on [standard device sizes](https://css-tricks.com/snippets/css/media-queries-for-standard-devices/)

The website was tested on the following devices:
- Windows laptop
- Samsung Galaxy A70

The site has been tested on friend's devices also. These include:


I have tested other devices using the chrome developer tools including:
- Moto G4
- Galaxy S5
- Pixel 2 / Pixel 2 XL
- iPhone 5 / SE / 6 / 7 / 8 (incl Plus options) / X
- iPad / iPad Pro
- Surface duo
- Laptop

The website is platform-cross compatible and has a consistant result. However as noted on the main README doc, for the best user experience larger device sizes are recommended to be able to view cards without excessive scrolling on the gmaes/profile pages.

[Back to table of contents](#table-of-contents)

## Performance Testing

Using lighthouse on Google Chrome developer tools - reports generated, pages come back with 85+ scores on all pages.

Some issues that hamper the performance score are based on the Materialize framwork so these have not been fixed.

Another issue mentioned was regarding a "more info" link that is not descriptive enough for accessibility, however this link is for taking the user to the game detail page. This link is repeated 3 times on the game card for optimum accessability and is on the game title which is more decriptive and on the image which has an alt tag. 

### Issues highlighted from Lighthouse reports and fixed.

1. Main issue that was highlighted on Lighthouse report was that the page was running on http instead of https, which is insecure.
    - I fixed this by using Flask Talisman and followed the instructions on [this page](https://github.com/GoogleCloudPlatform/flask-talisman)
    - Initially I had the syntax of the csp settings wrong so once deployed the CSS, fonts and external styling was not rendering.
    - After fixing the styling I then realised that due to the csp settings the small amount of inline javascript was being blocked so I had to refactor this code into a separate .js file without the use of jinja templating where that was being used. (pre-populating forms with db information)
2. The report highlighted a few missed alt tags as well as a suggestion to add 'rel="preload" to stylesheet links in the head element.
3. Missing a meta description.



[Back to table of contents](#table-of-contents)

## Encountered Issues

- The biggist issue I found was the re-work that presented after installing and implementing flask Talisman. (See above in Lighthouse report issues.)

- Getting the filter bar to function as expected if searching with an array. i.e if 2 items are being filtered by they both must in the returned results. Previously they were returning either/or the filtered selections. I used the [$and](https://docs.mongodb.com/manual/reference/operator/query/and/) operator for this.
- In addition the above, I found that if no options were selected to filter and I had a blank array to search based on my code that this would throw an error so I also had to produce code that if the array length was 0 to just bring up all games and flash a message.

- When using a materialize modal for a "are you sure you want to delete?" message for deleting reviews or games that were populated from the database in a for loop, the function would delete the wrong thing. I realised that the modal being populated in the for loop was always related to the first review/game on the list. I fixed this by adding {{loop.index}} on the required attributes/elements.

[Back to table of contents](#table-of-contents)