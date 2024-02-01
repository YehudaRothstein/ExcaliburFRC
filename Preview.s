; This project is a web application developed using Python and JavaScript.
; The backend is written in Python using the Flask framework.
; The frontend is written in HTML, CSS, and JavaScript.

; The application has several routes defined in the main.py file.
; Each route corresponds to a different page or functionality of the web application.

; The "/Login" route is used for user authentication. It checks the username and password against a SQLite database.
; If the credentials are correct, the user is redirected to the "/Scout" page.

; The "/Scout" route is used to process scouting data. It accepts POST requests with JSON data.
; The data is then appended to a JSON file in the static directory.

; The "/get-json-data" route is used to retrieve the JSON data stored in the static directory.

; The "/process_form" route is used to process form data.

; The "/home" and "/test_new" routes return a test page.

; The "/ReportBugs" route returns a page where users can report bugs.

; The "/static/<path:path>" route is used to serve static files.

; The "/<usr>" route returns a personalized greeting for the user.

; The "/Autonomous" route returns a page related to autonomous functionality.

; The "/ScoutHomePage" and "/ScoutGuest" routes return the scout home page and guest page respectively.

; The "/get-json" route is used to retrieve the JSON data stored in the static directory.

; The "/" route returns the home page.

; The "/Dashboard" route returns a dashboard page.

; The "/Queen-Of-Scouting" route returns a page related to the "Queen of Scouting".

; The application is run on a local server at port 5000.
