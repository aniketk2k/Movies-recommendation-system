import streamlit as st
import pandas as pd 
import time
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
import ast
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import  PorterStemmer


movies=pd.read_csv('tmdb_5000_movies.csv')

def search(mov):
    
    warnings.filterwarnings('ignore')
    movies=pd.read_csv('tmdb_5000_movies.csv')
    credits=pd.read_csv('tmdb_5000_credits.csv')

    movies=movies.merge(credits,on='title')

    movies=movies[['movie_id','title','release_date','overview','genres','keywords','cast','crew','runtime','vote_average']]

    movies.isnull().sum()
    movies.dropna(inplace=True)
    movies.duplicated().sum()
    
    def congenre(obj):
        genre=[]
        for i in ast.literal_eval(obj):
            genre.append(i['name'])
        return genre
    movies['genres']=movies['genres'].apply(congenre)
    movies['keywords']=movies['keywords'].apply(congenre)

    def concast(obj):
        L=[]
        counter=0
        for i in ast.literal_eval(obj):
            if counter!=3:
                L.append(i['name'])
                counter+=1
            else:
                break
        return L


    def Director(obj):
        L=[]
        for i in ast.literal_eval(obj):
            if i['job']=='Director':
                L.append(i['name'])
                break
        return L

    movies['crew']=movies['crew'].apply(Director)
    movies['cast']=movies['cast'].apply(concast)

    movies['overview']=movies['overview'].apply(lambda x:x.split())

    movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])

    movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])#we need to remove spaces from all the column data
    movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
    movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])

    movies['tag']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']

    new_df=movies[['movie_id','title','tag','runtime','vote_average']]
    new_df['title']=new_df['title'].apply(lambda x:x.lower())
    new_df['tag']=new_df['tag'].apply(lambda x: " ".join(x))
    new_df['tag']=new_df['tag'].apply(lambda x:x.lower())
    

    cv=CountVectorizer(max_features=5000,stop_words='english')
    vector_movies=cv.fit_transform(new_df['tag']).toarray()


    #vector_movies.shape  # no of movies,no of words we chose

    ps=PorterStemmer()


    def stem(text):
        y=[]
        for  i in text.split():
            y.append(ps.stem(i))
        return " ".join(y)


    new_df['tag']=new_df['tag'].apply(stem)
  
    vectors=cv.fit_transform(new_df['tag']).toarray()

    similarity=cosine_similarity(vectors)


    result=pd.DataFrame()
    result['movie_id']=movies['movie_id']
    result['title']=movies.title+"("+movies['release_date']+")"
    result['vote_average']=movies['vote_average']
    result['genre']=movies['genres'].apply(lambda x:",".join(x))
    result['runtime']=movies['runtime']
    result['cast']=movies['cast'].apply(lambda x:",".join(x))
    result['overview']=movies['overview'].apply(lambda x:" ".join(x))

    progress=st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    
    def recommend(mov):

            n=x #no of movies user desire to be recommended
            movies_index=new_df[new_df['title']==mov.lower()].index[0]
            distance=similarity[movies_index]
            movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:n+1]
            L=[]
            for i in movies_list:
                t=result.iloc[i[0]]
                df=pd.DataFrame()
                t.runtime=int(t.runtime)
                #t.runtime.prec=2
                df=[t.movie_id,t.title,t.vote_average,t.genre,t.runtime,t.cast,t.overview]
                L.append(df)
            #columnwidth=[1,1,1,1,1,1,1]
            header=['Movie_id','Title(Release Date)','Rating(10)','Genres','Runtime(In Mins)','Top Casts','A Brief Overview']
            Movie=pd.DataFrame(L,columns=header)
            return Movie
    return recommend(mov)


st.title("Movie Recommendion System")
st.image("image//logo2.jpg")

nav=st.sidebar.radio("Navigation",["Search","Our Data"])
if nav=="Search":
    moviename=st.text_input("Movie Name")
    global x
    x=st.slider("Select the range of suggestions you want",min_value=5,max_value=50,value=10, step=5)
    if len(moviename)==0:
        st.write("Please enter movie name in the box")
    else:    
        st.write("Movies to watch if you like ",moviename.upper())
        p=search(moviename)
        st.dataframe(p,width=1500,height=500)


if nav=="Our Data":
    st.write("Click the checkbox if you want to see the data:")
    if st.checkbox("Show Data Table"):
        st.write("The table contains data of more than 4800 movies, so it may take some time.")
        st.write("Loading the Data. Please Wait...")
        progress=st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)
        st.table(movies)