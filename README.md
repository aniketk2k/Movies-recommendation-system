# Movies-recommendation-system

# Problem Statement:
Identify a list of movie recommendations, which contains at least one that the user will start watching as their next selection, along with what might be more related to the User’s choice of movies Based on a single input(Just one movie name).

# Methodlogy:
### DataSet Used:
  - Kaggle, a subsidiary of Google LLC, is an online community of data scientists and machine learning practitioners.
  - We've used TmDb dataset (available on kaggle) which consists of more than 4800 unique details about movies of the last 3 decades. 
### Framework Used:
  - Streamlit is an open-source app framework for Machine Learning and Data Science teams. Create beautiful data apps in hours, not weeks. All in pure Python!
### Technique Used:
  - At first, changes were made in the dataset because the dictionary is not a very appropriate way to showcase and work with. 
  - For recommendation and filtering purposes, we have converted each data related to particular movies into mathematical vectors.
  - We have used the Bag of Words technique for choosing the required k-nearest neighbor vectors(most close ones are supposed to provide the most relevant results). 
  - For output, the User will be shown these particular details- 
      - Movie Id ; Title(Release Date) ; Rating(Out of 10) ;Genres ; Runtime(In Minutes) ; Top Casts & A Brief Overview.
    
# Layout, Design and Working:
<p align="center" width="100%">
    <img width="47%" height="500" src="https://user-images.githubusercontent.com/94344711/181692280-a8ab6d0b-748e-4399-9901-9884b2a19269.png">
    <img width="47%" height="500" src="https://user-images.githubusercontent.com/94344711/181692315-c94830ef-76e6-4d1e-a71d-9421f22f8139.png">
</p>

# Result and Discussion:
  - We Implemented very eﬃcient,easy to use, predicting, easy to explain movie recommendation system on basis of a input of movie name from user.
  - We conclude that the model provides a neat user interface for user to work with as well as good choice of recommendations.



