                              Cinematch - Movie Recommendation Web App



Overview :

The Movie Recommendation Web App is a Flask-based web application designed to help users discover new movies based on their preferences. Built as part of a group project, this app allows users to select their favorite movies from a dataset of 5,000 movies and receive personalized recommendations. The app features a clean and intuitive user interface, powered by Bootstrap, with a scrollable table for movie selection, a year filter to narrow down the movie list, and a recommendation system that processes user selections to suggest similar movies.

The backend is implemented in Python using Flask, with data processing handled by pandas. The recommendation logic is encapsulated in a custom module (functions/f.py), which processes user-selected movies and generates recommendations. The frontend uses HTML, CSS, and JavaScript (with jQuery for AJAX requests) to provide a seamless user experience, including a loading spinner during recommendation processing and client-side validation to restrict movie selections.

Key Features
- Movie Selection: Users can browse a table of 5,000 movies, with columns for Title, Year, Directors, and Movie ID.
- Year Filter: Filter the movie list by release year using a dropdown menu.
Selection Limit: Users can select 1 to 5 movies, enforced by both client-side (JavaScript) and server-side validation.
- Recommendation Generation: After selecting movies, users can click "Get Selected" to receive personalized movie recommendations, which are displayed on a separate page.
- Responsive Design: The app is styled with Bootstrap, ensuring a responsive layout that works on both desktop and mobile devices.
- Loading Feedback: A loading spinner provides visual feedback while recommendations are being generated.

Setup Instructions :
Prerequisites
- Python 3.7 or higher
- Git
- A terminal or command-line interface
- A web browser

To run Flask WebApp
- Clone Repository to machine
- Install any necessary requirements
- In MovieRecc/MovieGroupProj/movie_app/functions/f.py, there are 3 path files between line 12 and line 27. Update these as necessary.
- Open MovieRecc/MovieGroupProj/movie_app in terminal
- Enter "flask run" in terminal
- Open the link in the terminal which will launch the app

To View Model and Testing without running Flask
- In MovieRecc/MovieGroupProj/movie_app/functions/model_test.ipynb, change any path file in the first two code cells as necessary, then run all cells.

Usage
1) Home Page:
Upon launching the app, you’ll land on the home page, which provides an introduction to the movie recommendation system.
Click on the "Get Recommendations" link to start selecting movies.
2) Movie Selection:
On the "Get Recommendations" page, you’ll see a table of movies with columns for Title, Year, Directors, and Movie ID.
Use the "Filter by Year" dropdown to filter the movie list by release year.
Select 1 to 5 movies by checking the boxes in the "Select" column. (You’ll be restricted from selecting more than 5 movies.)
3) Get Recommendations:
Click the "Get Selected" button to generate recommendations based on your selections.
A loading spinner will appear while the recommendations are being processed.
You’ll be redirected to the "Suggestions" page, where your recommended movies will be displayed.

Limitations :

- Sample data has been used for this project. More data is needed for real-time use cases to improve accuracy and recommendations.