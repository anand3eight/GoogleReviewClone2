import streamlit as st
import sys
sys.path.insert(0, '/Users/anand/PycharmProjects/DbmsProject/LoginPage/DBOperations')
import DBUserOperations as DB
from streamlit_star_rating import st_star_rating

def viewCompanyReviews(dbObj) :
    x = st.empty()
    name = st.text_input('Company Name')
    search = st.button('Search Reviews', use_container_width=True)
    if search :
        reviews = dbObj.fetchCompanyReviews(name)
        if reviews != -1 :
            count = 1
            for x in reviews :
                    st.write('<h4>Result ' + str(count) + '</h4>', unsafe_allow_html=True)
                    for i in x :
                        if i == 'Rating' :
                            stars = st_star_rating(label='Rating', maxValue=5, defaultValue=x[i], key="rating"+str(count),
                                                   read_only=True, dark_theme=True)
                        else :
                            st.text_input(key=str(count) + "_" + i,label=i, value=x[i])
                    st.markdown("""---""")
                    count += 1

def viewPlaceReviews(dbObj) :
    x = st.empty()
    name = st.text_input('Place Name')
    search = st.button('Search Reviews', use_container_width=True)
    if search :
        reviews = dbObj.fetchPlaceReviews(name)
        if reviews != -1 :
            count = 1
            for x in reviews :
                    st.write('<h4>Result ' + str(count) + '</h4>', unsafe_allow_html=True)
                    for i in x :
                        if i == 'Rating' :
                            stars = st_star_rating(label='Rating', maxValue=5, defaultValue=x[i], key="rating"+str(count),
                                                   read_only=True, dark_theme=True)
                        else :
                            st.text_input(key=str(count) + "_" + i,label=i, value=x[i])
                    st.markdown("""---""")
                    count += 1


if __name__ == '__main__' :
    dbObj = DB.DBUser()
    x = st.empty()
    st.title('View Details')
    option = st.selectbox('Choose an Option', ('Company', 'Place'))
    if option == 'Company' :
        viewCompanyReviews(dbObj)
    elif option == 'Place' :
        viewPlaceReviews(dbObj)