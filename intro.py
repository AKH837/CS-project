import streamlit as st
import time
st.title ("Title")
st.header("Header")
st.subheader("subheader")
st.text("Text")
st.markdown("""# h1
## h2
### h3
:moon: <br>
:sunglasses:
**bold**
_italic_
""",True)

st.latex("Strings or expressions")
st.write("# this is heading" , "Anything can be written here ")
st.write(st)
st.write(sum)
st.table()

st.cache_data
def ret_time():
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time())

if st.checkbox("2"):
    st.write(ret_time())
    st.write("You chose option 2")