import base64
import pickle
import streamlit as st
import requests

st.set_page_config(page_title="Movie Recommender")
st.title("Movie Recommender")

movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
movie = st.selectbox(
    'Enter Movie For Recommendations',
    movie_list,
)
def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=968ee501e8560642bcba2bbe0acb32e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    path = "http://image.tmdb.org/t/p/w500/" + poster_path
    return path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_poster.append(get_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]]['title'])
    return recommended_movies_name, recommended_movies_poster

if st.button('Show Recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(movie)
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])
    with c2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])
    with c3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
    with c4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])
    with c5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])