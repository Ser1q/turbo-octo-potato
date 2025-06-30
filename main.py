import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="1 Year With You 💖", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: pink;'>1 - year already? The time flyes with you zhanm❤️</h1>",
    unsafe_allow_html=True,
)
# CSS for confetti animation and styling
st.markdown(
    """
<style>
@keyframes confettiFall {
  0% {
    transform: translateY(-10vh) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: translateY(110vh) rotate(360deg);
    opacity: 0;
  }
}

.confetti {
  position: fixed;
  top: -10vh;
  width: 10px;
  height: 10px;
  border-radius: 2px; /* Set to 50% for circles */
  animation-name: confettiFall;
  animation-timing-function: ease-in;
  z-index: 9999;
}
</style>
""",
    unsafe_allow_html=True,
)

# Colors for confetti
colors = ["#FF5F5F", "#FFC93C", "#6AAB9C", "#5F9DF7", "#B983FF", "#FF85B3", "#7BE495"]

# Generate confetti divs
confetti_html = ""
for i in range(80):
    left = random.randint(0, 100)
    duration = round(random.uniform(2, 5), 2)
    delay = round(random.uniform(0, 3), 2)
    size = random.randint(6, 12)
    color = random.choice(colors)

    confetti_html += f"""
    <div class="confetti" style="
        left: {left}vw;
        background-color: {color};
        animation-duration: {duration}s;
        animation-delay: {delay}s;
        width: {size}px;
        height: {size}px;
    "></div>
    """

st.markdown(confetti_html, unsafe_allow_html=True)


# Load and play your local mp3
st.write("Some music 😝💕")
audio_file = open("music.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mp3", start_time=0)

st.markdown("## 💌 I love everything about you")
# st.write("""

# """)


def resize_image(image_path, max_width=300):
    img = Image.open(image_path)
    img.thumbnail((max_width, max_width))  # Keeps aspect ratio
    return img


def show_heart_rain():
    st.markdown(
        """
    <style>
    @keyframes fall {
      0% {transform: translateY(-10vh) rotate(0deg); opacity: 1;}
      100% {transform: translateY(110vh) rotate(360deg); opacity: 0;}
    }
    .heart {
      position: fixed;
      top: -10vh;
      font-size: 24px;
      animation-name: fall;
      animation-timing-function: linear;
      z-index: 9999;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    heart_html = ""
    for _ in range(70):
        left = random.randint(0, 100)
        duration = round(random.uniform(3, 7), 4)
        delay = round(random.uniform(0, 4), 2)
        size = random.randint(16, 32)
        heart_html += f"""
        <div class="heart" style="
            left: {left}vw;
            animation-duration: {duration}s;
            animation-delay: {delay}s;
            font-size: {size}px;
        ">❤️</div>
        """
    st.markdown(heart_html, unsafe_allow_html=True)


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
with st.expander("👀 Our First Eye Catch"):
    img1 = Image.open(
        "./her/the_day.JPG",
    ).rotate(180, expand=True)

    # Create two columns
    left_col, right_col = st.columns([1, 2])

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

with st.expander("💬 Not a day without you"):
    st.write(
        "However, it would be hard to see you only at volleyball. Fortunatelly, we have the goat here."
    )

    img1 = Image.open(
        "./her/the_lectures.PNG",
    )

    # Create two columns
    left_col, right_col = st.columns([2, 1])

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


with st.expander("✨ Our first night"):
    st.write("Would you like some sushi? Yes/no?")

    if st.button("Click Me!"):
        show_heart_rain()
        st.success("This was the moment our hearts began to fall❤️")

    st.write("Funny thing is, we had one day off. It was unbearable.")

    img1 = Image.open(
        "./her/the_first_night.jpg",
    ).rotate(-90, expand=True)

    # Create two columns
    left_col, right_col = st.columns([2, 1])
    with left_col:
        st.markdown("### Inst the WINGMAN")
        st.write("""
        There is NO day that went without thinking about you. I could't handle the urge to write to you, to talk to you. 
        Even if it was just one day, just the first week to know each other, even if I had work to do. I love you. 
        I was amazed how cute you are and it was really hard to not to tell you that the day I met you, and especially that night.
        
        I loved how we went all around the campus and talked about everything. I loved to be with you and I was really happy to be able to talk to you everyday.
        I loved that we could spend time just the two us.
        
        Сенің жаныңда мен өзімді шынайы бахытты сезіндім. Сенімен өткізген жаз менің ең көңілді әрі әсерлі естеліктерімнің бірі. Тек сенің жаныңда
        мен өзімді сонша сабырлы және уайымсыз сезіне аламын. Өмірімде не болып жатса да, сен жанымда болсаң, маған артық дым қажет емес.
        Менің қазір аңсап жүретінім, тек сенің құшағың. Түн сайын сені түстерімде көріп, армандап жүрмін. 
        Жаным менің, мен сені қатты сағындым, сенен жақынырақ, сенен артығырақ түсінетін адам жоқ бұл әлемде.
        Алтыным менің, күнім, айым менің, мен сені қатты жақсы көремін. Сенсіз менің өмірімнің мәні әлі де сұрақ болып жүретін еді.
        Ия, мен жұмыс жасаймын, еңбек етемін, бірақ бұның бәрі сенсіз түкке тұрмас еді. Сен үшін әлемнің кез келген жеріне бару маған мәселе емес, әрдайым жаныңда болуға жолын табамын.
        Сен менің басты арманым да мақсатымсың.
        
        Болашақта саған барымды бергім келеді. Барлық қамқорлық пен жағдайды жасағым келеді. Сені қатты сүйемін, біздің күніміз құтты болсын❤️
        
        Күлкіңнен айналайын алтыным менің. Қаттыыы сені жақсы көреміііін❤️❤️❤️
        """)

    with right_col:
        st.image(img1, use_container_width=True, caption="09.06.2024")

# List of videos with titles and descriptions
videos = [
    {
        "file": "./her/video1.MOV",
        "title": "❣️ My lovely yapper",
        "desc": "Even with my dead ass lips, you kissed me",
    },
    {
        "file": "./her/video4.MOV",
        "title": "🌷 Flowers fit you",
        "desc": "A day of laughter, sunsets, and sandy toes",
    },
    {
        "file": "./her/video3.MOV",
        "title": "🚅 Through the ice and fire to you",
        "desc": "Shymkent's wonder of the world",
    },
    {
        "file": "./her/video2.MOV",
        "title": "🌹 I love you",
        "desc": "Tough day, even though, I love you",
    },
    {
        "file": "./her/video5.MOV",
        "title": "👨‍🍳 Your personal chef",
        "desc": "I love to cook you food, I want to always cook it for you",
    },
]


# Helper function
def render_video(file, title, desc):
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h4 style="color: #FF69B4;">{title}</h4>
            <p style="font-size: 15px; color: #666;">{desc}</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    with open(file, "rb") as f:
        st.video(f.read())


# First row (3 videos)
row1 = st.columns(3)
for i in range(3):
    with row1[i]:
        render_video(videos[i]["file"], videos[i]["title"], videos[i]["desc"])

# Second row (2 videos centered)
row2 = st.columns([1, 3, 1, 3, 1])  # Center 2 videos
with row2[1]:
    render_video(videos[3]["file"], videos[3]["title"], videos[3]["desc"])
with row2[3]:
    render_video(videos[4]["file"], videos[4]["title"], videos[4]["desc"])
