# Meeple Finder
## Meeting Meeples is easy...

*Developed and designed for Code Institue, Milestone Project 3: Backend Development (Python and Data Centric Development)

[Please view the live project here](http://meeple-finder.herokuapp.com/)

![Mockups]()

## Table of Contents

1. [Overview](#overview)
2. [User Experience](#ux-(user-experience))
    - [User Stories](#user-stories)
        - Visitor Stories
        - Business Stories
    - [Structure](#structure)
    - [Skeleton](#skeleton)
        - Wireframes
    - [Design](#design)
        - Colour Scheme
        - Fonts
        - Imagery
        - Audio
3. [Features](#features)
    - Current Features
    - Future Implementation
4. [Technologies](#technologies)
    - Languages
    - Frameworks, Libraries and Tools
    - Validation
5. [Testing](#testing)
6. [Deployment](#deployment)
    - GitHub pages
7. [Credits](#credits)
    - Code
    - Media
    - Content
8. [Acknowledgements](#acknowledgements)
9. [Disclaimer](#disclaimer)

## Overview

My MS3, Data Centric Development project, for my Code Institute course. I decided to base my project on board games as I play a lot in my spare time with friends.

I have called the website "Meeple finder", meeples are small figures used as a playing piece in most modern board games and have a stylized human form.

The purpose of this site is to act as Board Games Community where users can search for new board games based on various criteria and learn more about them based on user reviews. 

A registered user has access to their own profile page that contains a personalised collection and wishlist and they then can also leave reviews on games they have played to help other users.

[Back to table of contents](#table-of-contents)

## UX (User Experience)

The user types for this website would be for Board Game Fans (entry level or established) to find more Board Games that they would enjoy, 

### Visitor Stories
1. As a site visitor, I would like to search a list of board games based on different criteria e.g. number of players, game type, game manufactorer, age level etc.
2. As a site visitor, I would like to register an account that is secure and private.
3. As a site visitor, I would like a personalised dashboard to show board games I have in my collection, a wishlist for games I would like to have in my collection which I can easily add to when searching for games.
4. As a site visitor, I would like to be able to add reviews but also to edit and delete the reviews if required. I should also be the only user who can edit or delete my reviews, other users can only view them.
5. As a site visitor, I would like to be able to add or request to add a game to the board game list if it is not currently listed on the site.
6. As a site visitor, I would like to have games that are suggested to me based on the board games in my collection. (*potential future*)
7. As a site visitor, I would like to find board game retailers or cafe's where I can buy or try out new board games on my wishlist.  (*potential future*)
8. As a site visitor, I would like a website that is intuitive, easy to navigate and provides clear feedback on any actions I make (e.g when adding reviews, games etc)
9. As a site visitor, I would like a glossary of board game terms used if I am unfamiliar with the terminology.


### Business Stories
1. As a site owner, I would like to create a commuinty website where board game enthusiasts (new and old) can share their reviews and seek reccomendations on different board games.
2. As a site owner, I would like a site that's easy to navigate, is intuitive and has eye-catching design.
3. As a site owner, I would like for visitors to sign up to the community and add their reviews or reccomendations of board games to help fellow enthusiasts.
4. As a site owner, I would like adding reviews to be accessed by registered users only. Non registered users can only view board game listings and their reviews.
5. As a site owner, I would like users to be able to edit and/or delete their own reviews only.
6. As a site owner, I would like users to be able to add or request to add a game to the board game list if it is not currently listed on the site.
7. As a site owner, I would like to have admin access to be able to view, edit and delete any records that may be inaccurate or inappropriate for the website.
8. As a site owner, I would like to support local board games shops and cafes by having a google maps API for users to find shops/cafes local to them. (*potential future*)

[Back to table of contents](#table-of-contents)

## Structure

The Meeple finder website is designed to be effective, consistent and user friendly.
- Interaction Design
    - Consistent design will be used throughout the website to maintain a good UX.
    - The simple navigation bar will be consistent across all pages.
    - The navigation links when hovered over will provide a visual indication to the site visitors what they are selecting.
    - The navigation link on the active page will provide a visual indication to the site visitors of what page they are currently viewing.
    - Buttons when hovered over and clicked will provide a visual indication to the site visitors what they are selecting.
    - Consistent colour scheme will be used throughout the site.
    - Links to external pages, if applicable, will open in a new tab so the user is not taken away from the game website.
    - Links to glossary page, will open in a new tab so the user is not taken away from the page they were on. Helper text next to the button will indicate these buttons on the page.
    - All pages with forms on will have a reset button to reset the information on that form (more useful for editing forms) and will have a cancel/go back button to take the user back to the previous page.

- Information Architecture (IA)
    Website:
    - Logged in users:
        - Consists of a home page/games list page, profile page, add game page, tags list page and logout page.
        - The home page has a search and filter functionality
        - From the home page/games list page and profile page you can access more detail about a game - games detail page.
            - From the games detail page you can add a review and edit/delete your own reviews. You can also access the tag list/glossary page from here.
        - From the tag list/glossary page you can add a new tag.
    - Admin user:
        - Same as logged in users with a few differences.
        - From the home page/games list page and profile page admin can also access the edit game page to update information/delete game record from the database.
        - From the tag list/glossary page admin can also edit or delete an existing tag.
    - Non logged in users (similar to logged in users but with no ability to add/edit/delete functionality - can only view information):
        - Consists of a home page/games list page, tags list page, register and login pages.
        - The home page has a search and filter functionality and has links to login/register pages.
        - From the games detail page you can only view information and reviews. You can access the tag list/glossary page from here as well as login/register pages.
        - The tag list has the add tag functionality removed.
    
    Database:
    - Information on my mongodb database is stored in the following 4 collections:
        - Games:
            - _id (created by mongodb. ObjectId).
            - name (string)
            - description (string)
            - image (string - of image URL)
            - publisher (string)
            - type (string)
            - min_player (string)
            - max_player (string)
            - age (string)
            - playing_time (string)
            - mechanisms (An array of mechanism names)
            - themes (An array of theme names)
        - Reviews:
            - _id (created by mongodb. ObjectId).
            - id_of_game (string - taken from game _id above)
            - name (string)
            - review_comments (string)
            - created_by (string - pulled from session user)
            - created_date (string - pulled from datetime python function)
        - Tags:
            - _id (created by mongodb. ObjectId).
            - name (string)
            - use (string - either mechanisms or themes)
            - description
        - Users:
            - _id (created by mongodb. ObjectId).
            - username (string)
            - password (hashed so password information is safe)
            - my_collection (an array of objects). Each object (a game) has the following fields:
                - id (object id of the game)
                - name (string)
                - image (string - of image URL)
                - date_added (string - pulled from datetime python function)
            - my_wishlist (an array of objects). Each object (a game) has the following fields:
                - id (object id of the game)
                - name (string)
                - image (string - of image URL)
                - date_added (string - pulled from datetime python function)

    - An index has been created on the games collection (to enable search functionality) for the followingfields:
        - Name
        - Description
        - Mechanisms
        - Themes

        - ** Add player count and playing time? **


[Back to table of contents](#table-of-contents)

## Skeleton

The initial webpage layouts were sketched on the paper. The wireframes were then created in Balsamiq. Please view the wireframes for desktop, tablet and mobile screens on the following pdf.

[Wireframe PDF](#)

[Back to table of contents](#table-of-contents)

## Design

### Colour Scheme

- The color scheme, is based on a complementary color scheme palette i found on the coolors website. It's a palette of teal colors and soft pink/peach/orange color. [Coolor palette inspiration](https://coolors.co/006d77-83c5be-edf6f9-ffddd2-e29578)
- Teal is a cool tone color so the soft warm peach color works well as a contrast.
- I used the darkest teal color for the nav bar and footer, as well as most of the general buttons and text, against the very light teal background these items  stand out.
- The soft peach color is used for the home page welcome message, as well as table or form background colors to allow these to stand out against the otherwise monochromatic teal colors.
- According to color psycologyy website [empower yourself with color psychology](https://www.empower-yourself-with-color-psychology.com/color-turquoise.html) turqoise and teal colours are good colors to aid communication, calmness and creativity.

### Fonts

- I used two fonts through this project, Merriweather and Lato.
    - Merriweather, is used for the headings and is a serif font which I feel works well as text for the headings.
    - Lato, is used for non heading text and is sans-serif, making the paragraph text less formal looking.
- Both fonts were imported from [Google Fonts](https://fonts.google.com/)

### Imagery

- For the teal and white meeple images used in the brand logo, "delete" modals and the 404 page. These pictures were taken by my partner Phil Stott of my own meeples, edited to match the colour scheme and gifted to me for this project.
- All other images of the board games have been taken from either wikipedia or where these weren't available the board games companies websites. These are fine to use as this project is for educational use only.
- The "awaiting image" photo used on games that have no image has been taken from [logolynx](https://www.logolynx.com/topic/awaiting+image)


[Back to table of contents](#table-of-contents)

## Features

### Current Features
- Navigation bar (consistant on all pages):
    - an easy way to navigate through the website to specific sections.
    - The navigation bar is different depending on whether a user is logged in or not. (More options are availible to users that are logged in)
    - The navigation bar is fully responsive and it collapses to navbar-toggler-icon (hamburger menu) on smaller devices, bringing up the link options a side navigation bar.
- Footer (consistant on all pages):
    - The footer has a disclaimer about the use of images and confirms that they are for educational use only.
- Responsive
    - Side navigation bar on smaller devices.
    - Size and layout differences to be more aesthetically pleasing on medium and small devices, which is discussed in the specific pages below.
- Flashes
    - I have used flash messages throughout the site to confirm to the user when actions have been successful. Such as adding a game to the user's collection/wishlist or confirming what filters have been used on the games list page. etc
- Pagination
    - Pagination is used where applicable to limit results to a certain number per page. Allowing the user to not have to scroll a lot on 1 page.
- 404 page
    - If an error occurs, I have built a 404 page to help direct users and visitors back to safety.
- login required
    - I have restricted access to pages that should only be accessed when logged in using a python decorator. If non logged in, visitors will be redirected to the log in page with a flash message if they try to access a bookmarked page for their profile for example.

- Home/Games page
    - Welcome text that explains what the site is about and call to actions to either register or to Log in if the visitor is not logged in. If the user is logged in the call to actions disappear.
    - Games list - with a search and filter collapsible components.
        - As standard all games are shown when the page is loaded.
        - Visitors can search games using a free text option in the search bar to find a specific game or they can filter games by themes or game mechanisms to find a new game based on their likes.
    - Game information.
        - Games on the results list are displayed on a card format and are limited to 8 per page, with pagination to click through more results if required.
        - All games have some sort of image whether this is the actual image of a game or a placeholder image. This is a clickable image which takes you to the game's own page.
        - Each game card has a title (also clickable link), truncated game description and a button which takes the user to games own page.
        - For users - there are also links to be able to add the game to the users collection or wishlist.
- Game detail page
    - on large screens the game information takes up one third of the page with two thirds showing the reviews. On smaller devices, the game information and reviews will each be full width and will be stacked on top of each other.
        - Game detail: 
            - This section shows the game title, the description, the game publisher, type, age, number of players and playing time. It also shows what game mechanisms and themes are in the game. 
            - To help users out there is a button which opens the tag glossary page in a new tab so they can understand what each means.
        - Reviews:
            - If logged in a user can leave a review (which opens a new page), they can edit/delete their own review but can only view others.
            - If not logged in the visitor can only view reviews and cannot add a review. There are again call to action buttons for the visitor to log in or register.
            - Reviews will show the user who added the review and the date it was reviewd.
            - Reviews are sorted by the most recent are are paginated.
- Add a Review (logged in users only)
    - A simple form to add a comments based review, opens on a new page.
    - The name field is prepopulated and cannot be updated as the review is game specific.
    - The form has submit, reset and cancel buttons.
- Edit a Review (review user only)
    - A simple form to edit a previous comments based review that user has left, opens on a new page.
    - The name field is prepopulated and cannot be updated as the review is game specific.
    - The previous comments are pre-poulated. 
    - The form has submit, reset and cancel buttons.
- Delete a Review (review user only)
    - The delete button triggars a modal to confirm whether the user wants to delete their review as this cannot be undone.   
- Profile page (logged in users only)
    - Admin profile page:
        - The profile page will show all newly added games (which are found by games with the placeholder image * see add a game below as to why).
        - The game cards will have a edit/delete button so that the admin can update the game with an image and check details are accurate, or delete the game if the content added is a duplicate
    - Non -admin users:
        - The profile is split into two sections "My collection" and "My wishlist" where users will see the games they have added to these lists.
        - If no games have been added there will be a message confirming this, with a call to action to go to the games list.
        - The game cards on the profile's collection list will have a button to go to the game detail/review page and a link to be able to remove the game from their collection.
        - The game cards on the profile's wishlist list will have a button to go to the game detail/review page and a link to be able to remove the game from their wishlist or move it to their collection (i.e if they have now purchased the game), this also removes it from their wishlist.
- Add a game (logged in users only)
    - Simple form to allow users to add a game to the general games list if the game they are looking for isnt on the site.
    - The form comes with a disclaimer that admin will review the game added and may edit the entry to include an image or correct inaccurate detail.
    - Non admin users, will not be able to upload images of the games as I want to control what images are used for copyright reasons and images that may fall outside of my disclaimer.
    - There are helper text to aid a user to fill out the form and for the tag section again there is a link to the tag glossary which opens in a new tab.
    - There are buttons to submit the form, reset or to go back to the previous page the user was on.
- Edit a game (admin only)
    - pulls through the game information already submitted to the database and uses the same form style as the add a game form.
    - There are buttons to submit the form, reset or to go back to the previous page the user was on.
    - As well as the submit, cancel and reset button as per add game page, there is also a delete game button. This triggars a modal to get admin to confirm they want to delete this record as it cannot be undone.
- Game Tags
    - This page is predominantly a glossary for the tags used in game mechanisms and game themes in case the user isnt sure of board game terminology. 
    - The lists are sorted alphabetically in a table and there is a table per tag use (mechanisms and themes)
    - if logged in users will be able to add a new tag with a simple form. There is a button at the end of the tag list to do this. This button will not show for visitors that are not logged in.
    - On an admin log in, the admin can edit or delete tags that have been added.
- Add a tag (logged in users only)
    - Simple form consisting of a dropdown option for use, the tag name and the tag description.
    - There are buttons to submit the form or to reset it or to cancel and go back to the previous page.
    - The form has a helper text to ask the user to check the tag doesn't already exist before adding.
    - The full tag list can also be seen at the bottom of the page.
- Edit a tag (admin only)
    - Opens the edit tag form, which has the same layout as the add tag page but the information is pre-populated with the previous information.
    - There are buttons to submit the form or to reset it or to cancel and go back to the previous page.
- Delete a tag (admin only)
    - The delete button triggars a modal to confirm whether the admin wants to delete the tag as this cannot be undone. 
- Log in
    - Login page, simple form to check log in details of the visitor.
      - the form input lines turn red if the user has not met the input requirements
    - If log in is successful the user will be directed to their profile page, if not the form will reset and a flash message will confirm that the username/password didnt match.
    - Call to action button below the login form for if the visitor is new and needs to register.
- Register
    - registration page, simple form to check register details of the visitor.
    - the form input lines turn red if the user has not met the input requirements
    - If registration is successful the user will be directed to their profile page, if not the form will reset and a flash message that the username already exists.
    - Call to action button below the registration form for if the visitor is already registered and needs to login.
- Log out (logged in users only)
    - logs the user out of the session and redirects them to the log in page.
    


### Future Implementation

There are ideas and features for this project that I would have likes to implement if I had more time and/or knowledge to do so. Such as:
    - Reviews, allowing a user to add a star rating on the reviews. One that is stylized to have clickable stars that fill in for the rating that is given.
        - This would then be translated to the filter function on the main games page to allow vistors to filter by highest rated games.
    - Have a session timeout for users who "forget" to log out.
    - Amend the game card styling for mobile layouts as currently this view is not as user-friendly as it could be.
    - Allow for multiple admins or different roles e.g. "moderator" for if the site grew and needed more support staff for it. User records on the database would have a "role" field, this would be set and updated by the current main admin account.
    - Have a page with a google maps API to allow users to find board games shops and board games cafes in their area.
    - Change password/forgotten password feature.

[Back to table of contents](#table-of-contents)

## Technologies

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5) was used as the main language to complete the structure of the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) was used to style the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for responsive aspects within bootstrap but also my own JavaScript code to add interactivity to the game play.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was used for back end data centric work and connecting to the database.
- [Markdown](https://en.wikipedia.org/wiki/Markdown) - used for the readme documnetation.

### Database

- [MongoDB](https://en.wikipedia.org/wiki/MongoDB) used to store data which is used on the site.

### Frameworks, Libraries and Tools

- [flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
    - [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) a template engine which allows me to pull through python variables and extend pages from a base template.

- [Google Fonts](https://fonts.google.com/) was used to import the fonts to the website.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes for the website.
- [CSS Tricks](https://css-tricks.com/) was used as a general source.
- [W3Schools](https://www.w3schools.com/) was used as a general source.
- [StackOverflow](https://stackoverflow.com/) was used as a general source.
- [GitHub](https://github.com/) was used for repository hosting and for storing the source code.
- [Gitpod](https://gitpod.io/) was used as the development environment for writing the code.
- [Git](https://git-scm.com/) was used as version control system to add, commit and push code to GitHub.
- [Techsini](https://techsini.com/multi-mockup/) was used to create the responsive mockup image.
- [W3C Spell checker](https://www.w3.org/2002/01/spellchecker) was used to check the spelling of the webpage.
- [Markdown guide](https://www.markdownguide.org/basic-syntax/)

### Validation

- [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) was used for Markup validation.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) was used for CSS code validation.
- [jshint.com](https://jshint.com/) was used to check JS code.

See further information on results found during validation on the separate [Testing document]().

[Back to table of contents](#table-of-contents)

## Testing

Testing process was written in a separate document [Testing document]()

[Back to table of contents](#table-of-contents)

## Deployment

### Github/Heroku
### How to run this project locally

[Back to table of contents](#table-of-contents)

## Credits

### Code

- Resource used to help with adding pagination to the site.
    - [Pagination resource](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9)

- MongoDB documentation in general but more specifically:
    - [filter $and expressions](https://docs.mongodb.com/manual/reference/operator/query/and/)

- Concatinating array items into a string for filter function's flash messages.
    - [Stack overflow](https://stackoverflow.com/questions/12453580/how-to-concatenate-items-in-a-list-to-a-single-string)

- Handling 404 errors
    - [Geeks for Geeks](https://www.geeksforgeeks.org/python-404-error-handling-in-flask/)

- Refresher on footer stlying
    - [Stack overflow](https://stackoverflow.com/questions/3443606/make-footer-stick-to-bottom-of-page-correctly) 

- login required decorator
    - [Python programming](https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/?fbclid=IwAR2Lk2PIZVCXOlm5ARd-AQbPcB04LAfOOdXJU_ovfXJqhhfmnXbO4IVAzy8)

- Code Institute learning platform & mini projects, specifically the search/indexing lesson for the task manager mini project.


### Media

- The teal and white individual meeple pictures (including the favicon), are pictures created by my partner Phil Stott of my own meeples. These pictures were specifically created for this project and I have permission to use them.
- Most images of the board games have been taken from their wikipedia site. e.g. [Machi Koro - Wikipedia page](https://en.wikipedia.org/wiki/Machi_Koro).
- If the image of the board game box has not been available on wikipedia I have sourced the image from the board games company who produces/published the game.
- All images have been used as part of the "fair use" policy as they are being used for educational purposes only and to illustrate the product or brand in question.

[Back to table of contents](#table-of-contents)

## Acknowledgements

- My mentor, Mr. Victor Miclovich, for the helpful feedback and guidance.
- [Code Institute](learn.codeinstitute.net) for all course materials and ongoing support.
- Fellow Code Institute students for their feedback, suggestions and resource links.
- My family and friends for testing and useful feedback.
- My partner for taking images of meeples and editing them for my use.

[Back to table of contents](#table-of-contents)

## Disclaimer

The information provided and images used on this website are for educational purposes only.

[Back to table of contents](#table-of-contents)
