import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=a4bc233b601475ffc8725bfa9f3244be".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id

        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names,recommended_movie_posters


movies_list= pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_list)
st.title('Movie Recommender System')

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)
# if st.button('Recommend'):
#      st.write(selected_movie)
#      recommendations = recommend(selected_movie)
#      for i in recommendations:
#          st.write(i)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5,gap="large")
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0],width=200,use_column_width='never')
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1],width=200,use_column_width='never')

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2],width=200,use_column_width='never')
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3],width=200,use_column_width='never')
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4],width=200,use_column_width='never')



