# Testing

## Manual Testing 
| User Action | Expected Result | Y/N |
|-------------|----------------|-----|
| Site logo link not logged in | directs user to home.html | Y |
| Footer link not logged in | directs user to home.html | Y |
| Footer youtube link | opens blank page for correct site | Y |
| Footer twitter link | opens blank page for correct site | Y |
| Footer instagram link | opens blank page for correct site | Y |
| Navbar Register link | opens the signup.html page | Y |
| Navbar Sign In link | opens the login.html page | Y |
| Navbar Search Events link | opens the event_search.html page | Y |
| Navbar My Events > Hosting link | opens the event_hosting.html page | Y |
| Navbar My Events > Attending link | opens the event_attending.html page | Y |
| Navbar Create Event link | opens the create_event.html page | Y |
| Navbar My Profile link | opens the profile.html page | Y |
| Navbar Sign Out link | opens the logout.html page | Y |
| Clicking Sign Out | opens the logout.html page and signs a user out | Y |
| Register new user | registers a user if details are correct | Y |
| Register user using existing email | does not register | Y |
| Register user with a password that doesn’t fit criteria | does not register | Y |
| Register user with a malformed email | does not register | Y |
| Sign In with wrong email or password | throws validation error on form | Y |
| Sign in with correct email and password | signs the user in | Y |
| Site logo link when logged in | directs user to event_search.html | Y |
| Footer link when logged in | directs user to event_search.html | Y |
| Search events | Events are not in the past | Y |
| Click event on search_event.html | navigates to correct event detail page | Y |
| Click delete | brings up a confirm modal | Y |
| Clicking close on confirm modal | closes the modal | Y |
| Clicking delete on the confirm modal | deletes the event | Y |
| Clicking edit on the event detail | Shows the edit page with the event details | Y |
| Blank event title when editing event | Does not save | Y |
| Blank description when editing event | Does not save | Y |
| Blank category when editing event | Does not save | Y |
| Blank image when editing event | Does save | Y |
| Blank date when editing event | Does not save | Y |
| Blank start time when editing event | Does not save | Y |
| Blank end time when editing event | Does not save | Y |
| Blank location when editing event | Does not save | Y |
| Blank limit when editing event | Does save | Y |
| Date in the past when editing event | Does not save | Y |
| Start time in the past when editing event | Does not save | Y |
| End time less than start time when editing event | Does not save | Y |
| End time equals Start time when editing event | Does not save | Y |
| Blank event title when creating event | Does not save | Y |
| Blank description when creating event | Does not save | Y |
| Blank category when creating event | Does not save | Y |
| Blank image when creating event | Does save | Y |
| Blank date when creating event | Does not save | Y |
| Blank start time when creating event | Does not save | Y |
| Blank end time when creating event | Does not save | Y |
| Blank location when creating event | Does not save | Y |
| Blank limit when creating event | Does save | Y |
| Date in the past when creating event | Does not save | Y |
| Start time in the past when creating event | Does not save | Y |
| End time less than start time when creating event | Does not save | Y |
| End time equals Start time when creating event | Does not save | Y |
| Click event on event_hosting.html | navigates to the correct event detail page | Y |
| Click event on event_attending.html | navigates to the correct event detail page | Y |
| Blank First name when editing profile | Does not save | Y |
| Blank Last name when editing profile | Does not save | Y |
| Blank email when editing profile | Does not save | Y |
| Blank profile image when editing profile | Does save | Y |
| Blank location when editing profile | Does save | Y |
| Blank phone number when editing profile | Does save | Y |
| Blank about when editing profile | Does not save | Y |
| If an event has a limit | It's shown in the event details page | Y |
| If an event is in the past | It's shown in the event details page | Y |
| If an event is in the past | The host can only delete and not edit | Y |
| If an event is in the past | A non-host or attendee will not be able to attend | Y |
| If a user clicks 'Attend' on an event | A message should inform them saying they are going | Y |
| If an attendee of an event views an event they’re attending | They should see a 'Can't Attend' button | Y |

## Validation
### HTML Validation 
+ [HTML Validation Report](/documentation/validation/html_validation.pdf)
+ No errors or warnings were found when passing through the official [W3C validator](https://validator.w3.org/). This checking was done manually by copying the view page source code (Ctrl+U) and pasting it into the validator.

### CSS Validation 
+ [CSS Validation Report](/documentation/validation/css_validation.pdf)
+ No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri). 

### JS Validation 
+ [JS Validation Report](/documentation/validation//js_validation.pdf)
+ No errors or warnings were found when passing through the official [JS Hint)](https://jshint.com/). 
+ One warning: The 'esversion' option cannot be set after any executable code.
+ One undefined variable: bootstrap. Bootstrap is imported on the base.html and needed to show the modal.

### Python Validation
+ [Python Validation Report](/documentation/validation/python_validation.pdf)
+ No errors were found when the code was passed through [CI Python Linter](https://pep8ci.herokuapp.com/#). According to the reports, the code is Pep 8-compliant. This checking was done manually by copying python code and pasting it into the validator.


## Lighthouse Report
The low Best Practives score is coming from Cloudinary due to insecure URL's/

### home.html 
![home page](/documentation/validation/lighthouse/home.png)
### profile.html 
![home page](/documentation/validation/lighthouse/profile.png)
### create_event.html 
![home page](/documentation/validation/lighthouse/create_event.png)
### event_attending.html 
![home page](/documentation/validation/lighthouse/attending.png)
### event_detail.html 
![home page](/documentation/validation/lighthouse/event_detail.png)
### event_edit.html 
![home page](/documentation/validation/lighthouse/edit_event.png)
### event_hosting.html 
![home page](/documentation/validation/lighthouse/hosting.png)
### event_search.html 
![home page](/documentation/validation/lighthouse/search_events.png)
### signup.html 
![home page](/documentation/validation/lighthouse/register.png)
### login.html 
![home page](/documentation/validation/lighthouse/login.png)