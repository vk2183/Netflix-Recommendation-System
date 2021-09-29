import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    recommended_movies=[]
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Netflix Recommendation System')

selected_movie_name = st.selectbox(
'Select a movie or TV show',
 movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

     




















#def recommend(movie):
    #index = movies[movies['title'] == movie].index[0]
    #distances = similar[index]
    #movies_list = sorted(list(enumerate(similar[index])),reverse=True,key = lambda x: x[1])
    #print(distances)
    #recommended_movies=[]
    
    #for i in distances[1:6]:
        #recommended_movies.append([(movies.iloc[i[0]].title)])
    #return recommended_movies
#movies_dict = pickle.load(open('movies.pkl','rb'))
#st.title('Netflix Recommender System')
#movies_dict = pickle.load(open('movies_dict.pkl','rb'))
#movies = pd.DataFrame(movies_dict)

#similar = pickle.load(open('similar.pkl','rb'))

#selected_movie_name = st.selectbox(
#'Select a Movie Name',
#movies['title'].values)

#if st.button('Recommend'):
    #recommend(selected_movie_name)
    #st.write(selected_movie_name)
