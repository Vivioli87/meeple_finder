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



### Business Stories


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
    -

### Browser Testing

The website was tested on the following browser types. All browser versions were up to date.
- **Google chrome** - best performance with all cookies allowed.
- Firefox
- Safari
- Edge
- Opera (tested on ubuntu Linux)
- Samsung Internet
- Google chrome for Android 

The website does not work on Internet Explorer (javaScript does not function for some reason), please use Edge if you need to use a microsoft browser.

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

Using lighthouse on Google Chrome developer tools - reports generated 

**images of reports

### Issues highlighted from Lighthouse reports and fixed.


[Back to table of contents](#table-of-contents)

## Encountered Issues



[Back to table of contents](#table-of-contents)