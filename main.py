import streamlit as st
from PIL import Image

st.set_page_config(page_title="1 Year With You 💖", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: pink;'>1 - year already? The time flyes with you my zhanm❤️</h1>",
    unsafe_allow_html=True,
)
st.balloons()

st.markdown("## 💌 I love everything about you")
# st.write("""

# """)


def resize_image(image_path, max_width=300):
    img = Image.open(image_path)
    img.thumbnail((max_width, max_width))  # Keeps aspect ratio
    return img


# Photo grid (simplified)
col1, col2, col3 = st.columns(3)
img1 = Image.open("./her/bao_leaning.JPG").rotate(-90, expand=True)
with col1:
    st.image(img1, use_container_width=True, caption="I love when you lean towards me")
with col2:
    st.image(
        resize_image("./her/standup_flash.JPG"),
        use_container_width=True,
        caption="I love to look at you when doing photos",
    )
with col3:
    st.image(
        resize_image("./her/dawn.JPG"),
        use_container_width=True,
        caption="I love to be with you from dusk till dawn",
    )

# Timeline or expander
st.markdown("## 🕰️ Our Journey")
with st.expander("Our First Eye Catch"):
    st.write(
        "It is funny that even though we knew about each other at some point, we met at get to know eachother after some time. I will not forget how I was curious about you, when we first talked after volleyball 02.06.2024, and for the next day met and talked a bit at MATH 251"
    )

    img1 = Image.open(
        "./her/the_day.JPG",
    ).rotate(180, expand=True)

    # Create two columns
    left_col, right_col = st.columns([1, 2])  # Ratio 1:2 for more text space

    with left_col:
        st.image(img1, use_container_width=True, caption="02.06.2024")

    with right_col:
        st.markdown("### THE volleyball")
        st.write("""
        This was the photo that I took to parents that day. Who knew that it will be the day that I will encounter feelings that I have never before.
        I was amazed by your tattoo, and partially it was the cause of our log lasting (тутуту) relationship. I love how you play volleyball.
        I am gratefull to come to volleyball at that exact day <3. I am even red at that photo, I guess it was foreshadowing of some kind. Sizdi korip uialyp dep pa 😆
        
        I also remember how you just didn't give a damn about me, but I was not wondered at all, since I just loved sharing thoughts of mine).
        It is one of the my favorite parts of you, that you can listen to me, so I could share all of my feelings and wonders about any situation that I am going rn.
        """)

with st.expander("💬 Not a day without youter"):
    st.write(
        "However, it would be hard to see you only at volleyball. Fortunatelly, we have the goat here."
    )

    img1 = Image.open(
        "./her/the_lectures.PNG",
    )

    # Create two columns
    left_col, right_col = st.columns([2, 1])  # Ratio 1:2 for more text space

    with left_col:
        st.markdown("### Zhanbota the GOAT")
        st.write("""
        Summer semester looks scary. The lectures of lenght over an hour and repeting over and over till friday. But I was waiting for these lectures.
        You were on of the main reasons to come to lectures (the other is mandatory attendance😝). The first what I did after entering the class, is looking for you
        over allll the auditory. You are really easy to be caught by an eye, at leas for me 😍.
        The first day I was amazed for that coincedence, and the way you left the place SPECIAllY for me 🥰🥰🥰
        
        I love to run to you and just starting to yapp about anything, and you just listen without any hesitation. Aidanaaaa dep jugiru keremet ediii
        """)

    with right_col:
        st.image(img1, use_container_width=True, caption="03.06.2024")


# Music embed (replace with your song)
st.markdown(
    """
## 🎶 Our Song
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/yourtrackid" width="100%" height="80" frameBorder="0" allowtransparency="true" allow="encrypted-media"></iframe>
""",
    unsafe_allow_html=True,
)
