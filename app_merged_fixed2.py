import streamlit as st
import streamlit.components.v1 as components
import base64
import json
import re
from pathlib import Path


# =========================================================
# STREAMLIT SETTINGS
# =========================================================

st.set_page_config(
    page_title="A Little Surprise ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Remove Streamlit outer spacing
st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

[data-testid="stAppViewContainer"] {
    padding: 0 !important;
}

[data-testid="stHeader"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# YOUR PHOTO
# =========================================================

IMAGE_PATH = Path(__file__).parent / "WhatsApp Image 2026-10-12 at 11.14.11.jpeg"

with open(IMAGE_PATH, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode()


# =========================================================
# COMPLETE PAGE
# =========================================================

html_code = f"""

<!DOCTYPE html>

<html>

<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">


<style>


/* =====================================================
   RESET
   ===================================================== */

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}


html,
body {{
    width: 100%;
    height: 100%;
    overflow: hidden;
}}


body {{
    background: #650909;
    font-family: Georgia, serif;
}}


/* =====================================================
   MAIN SCREEN
   ===================================================== */

.screen {{

    width: 100vw;
    height: 100vh;

    min-height: 650px;

    position: relative;

    overflow: hidden;

    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(255,255,255,0.07),
            transparent 25%
        ),

        radial-gradient(
            circle at 80% 75%,
            rgba(0,0,0,0.22),
            transparent 32%
        ),

        #650909;
}}


/* =====================================================
   COFFEE / PAPER TEXTURE
   ===================================================== */

.screen::after {{

    content: "";

    position: absolute;

    inset: 0;

    opacity: 0.08;

    pointer-events: none;

    background-image:
        repeating-linear-gradient(
            45deg,
            transparent 0px,
            transparent 7px,
            rgba(255,255,255,0.15) 8px
        );
}}


/* =====================================================
   TORN PAPER CORNERS
   ===================================================== */

.paper-corner {{

    position: absolute;

    z-index: 1;

    background:
        linear-gradient(
            135deg,
            #e5d0aa,
            #c5a47b
        );

    opacity: 0.95;

    box-shadow:
        0 3px 10px rgba(0,0,0,0.18);

    pointer-events: none;
}}


/* TOP LEFT */

.corner-top-left {{

    top: -25px;
    left: -25px;

    width: 350px;
    height: 130px;

    clip-path: polygon(
        0 0,
        100% 0,
        87% 24%,
        72% 18%,
        60% 35%,
        45% 22%,
        32% 42%,
        18% 25%,
        0 45%
    );

    transform: rotate(-2deg);
}}


/* TOP RIGHT */

.corner-top-right {{

    top: -25px;
    right: -25px;

    width: 350px;
    height: 130px;

    clip-path: polygon(
        0 0,
        100% 0,
        100% 48%,
        83% 31%,
        70% 43%,
        55% 23%,
        40% 38%,
        25% 20%,
        10% 34%
    );

    transform: rotate(2deg);
}}


/* BOTTOM LEFT */

.corner-bottom-left {{

    bottom: -25px;
    left: -25px;

    width: 380px;
    height: 145px;

    clip-path: polygon(
        0 50%,
        18% 37%,
        31% 50%,
        46% 30%,
        60% 45%,
        76% 27%,
        89% 39%,
        100% 20%,
        100% 100%,
        0 100%
    );

    transform: rotate(2deg);
}}


/* BOTTOM RIGHT */

.corner-bottom-right {{

    bottom: -25px;
    right: -25px;

    width: 380px;
    height: 145px;

    clip-path: polygon(
        0 40%,
        13% 28%,
        27% 42%,
        42% 25%,
        56% 44%,
        70% 30%,
        85% 43%,
        100% 25%,
        100% 100%,
        0 100%
    );

    transform: rotate(-2deg);
}}


/* =====================================================
   COFFEE STAINS
   ===================================================== */

.coffee-stain {{

    position: absolute;

    border-radius: 50%;

    border: 3px solid rgba(111,73,37,0.18);

    box-shadow:
        inset 0 0 12px rgba(93,54,25,0.15);

    z-index: 2;

    pointer-events: none;
}}


.stain-one {{

    width: 100px;
    height: 65px;

    left: 5%;
    bottom: 12%;

    transform: rotate(-18deg);
}}


.stain-two {{

    width: 75px;
    height: 48px;

    left: 35%;
    top: 7%;

    transform: rotate(12deg);
}}


/* =====================================================
   DECORATIVE HEARTS
   ===================================================== */

.heart {{

    position: absolute;

    z-index: 3;

    font-family: Georgia, serif;

    pointer-events: none;
}}


.heart-one {{

    top: 8%;
    left: 43%;

    color: #f5c0b8;

    font-size: 46px;

    transform: rotate(-15deg);
}}


.heart-two {{

    top: 18%;
    left: 47%;

    color: #fff4e8;

    font-size: 30px;
}}


.heart-three {{

    bottom: 10%;
    left: 45%;

    color: #efb2a9;

    font-size: 42px;
}}


.heart-four {{

    top: 25%;
    right: 5%;

    color: #f0aaa0;

    font-size: 30px;
}}


.heart-five {{

    bottom: 12%;
    right: 7%;

    color: #efb2a9;

    font-size: 38px;
}}


/* =====================================================
   FLOWERS
   ===================================================== */

.flower {{

    position: absolute;

    z-index: 5;

    pointer-events: none;
}}


.flower-left {{

    left: 4%;
    bottom: 5%;

    font-size: 75px;
}}


.flower-top {{

    left: 4%;
    top: 8%;

    font-size: 46px;
}}


/* =====================================================
   ROSE
   ===================================================== */

.rose {{

    position: absolute;

    z-index: 6;

    left: 13%;
    bottom: 12%;

    font-size: 72px;

    transform: rotate(-12deg);
}}


/* =====================================================
   KISS
   ===================================================== */

.kiss {{

    position: absolute;

    z-index: 7;

    left: 39%;
    bottom: 15%;

    font-size: 48px;

    transform: rotate(-12deg);

    pointer-events: none;
}}


/* =====================================================
   BIG BIRTHDAY SCRAPBOOK DECORATIONS
   ===================================================== */

.birthday-sticker {{

    position: absolute;

    z-index: 12;

    pointer-events: none;

    user-select: none;
}}


/* BIG CAKE */

.bday-cake {{

    left: 3.5%;
    top: 35%;

    font-size: 105px;

    transform: rotate(-7deg);

    filter:
        drop-shadow(
            0 8px 8px
            rgba(0,0,0,0.28)
        );
}}


/* BIG BALLOON 1 */

.balloon-one {{

    left: 19%;
    top: 27%;

    font-size: 78px;

    transform: rotate(-12deg);

    filter:
        drop-shadow(
            0 6px 7px
            rgba(0,0,0,0.20)
        );
}}


/* BIG BALLOON 2 */

.balloon-two {{

    left: 28%;
    top: 38%;

    font-size: 70px;

    transform: rotate(10deg);

    filter:
        drop-shadow(
            0 6px 7px
            rgba(0,0,0,0.20)
        );
}}


/* BIG BALLOON 3 */

.balloon-three {{

    left: 9%;
    top: 61%;

    font-size: 65px;

    transform: rotate(-8deg);

    filter:
        drop-shadow(
            0 6px 7px
            rgba(0,0,0,0.20)
        );
}}


/* BIG TEDDY */

.big-teddy {{

    left: 27%;
    bottom: 18%;

    font-size: 95px;

    transform: rotate(6deg);

    filter:
        drop-shadow(
            0 8px 8px
            rgba(0,0,0,0.25)
        );
}}


/* BIG GIFT */

.big-gift {{

    left: 5%;
    bottom: 27%;

    font-size: 78px;

    transform: rotate(-8deg);

    filter:
        drop-shadow(
            0 7px 7px
            rgba(0,0,0,0.25)
        );
}}


/* =====================================================
   BIG SPARKLES
   ===================================================== */

.big-sparkle-one {{

    left: 30%;
    top: 25%;

    font-size: 50px;

    color: #f8df9b;

    transform: rotate(12deg);

    filter:
        drop-shadow(
            0 3px 4px
            rgba(0,0,0,0.2)
        );
}}


.big-sparkle-two {{

    left: 34%;
    top: 51%;

    font-size: 58px;

    color: #f8df9b;

    transform: rotate(-10deg);
}}


.big-sparkle-three {{

    left: 14%;
    top: 43%;

    font-size: 43px;

    color: #f8df9b;
}}


/* =====================================================
   SPECIAL BIRTHDAY STICKER
   ===================================================== */

.special-sticker {{

    position: absolute;

    z-index: 15;

    left: 7%;
    top: 49%;

    padding: 10px 22px;

    background:
        linear-gradient(
            145deg,
            #f7e5c5,
            #ead0a5
        );

    color: #711313;

    border: 3px solid #e7c99e;

    border-radius: 15px;

    font-family:
        "Brush Script MT",
        "Segoe Script",
        cursive;

    font-size: 27px;

    font-weight: 600;

    transform: rotate(-7deg);

    box-shadow:
        0 8px 15px rgba(0,0,0,0.25);

    pointer-events: none;

    white-space: nowrap;
}}


/* =====================================================
   BIRTHDAY BOY STICKER
   ===================================================== */

.birthday-label {{

    position: absolute;

    z-index: 15;

    left: 25%;
    bottom: 31%;

    padding: 9px 19px;

    background: #f4dfbb;

    color: #711313;

    border: 2px solid #e1bd8c;

    border-radius: 12px;

    font-family:
        "Brush Script MT",
        "Segoe Script",
        cursive;

    font-size: 24px;

    transform: rotate(6deg);

    box-shadow:
        0 7px 13px rgba(0,0,0,0.23);

    pointer-events: none;
}}


/* =====================================================
   RIBBON
   ===================================================== */

.big-ribbon {{

    position: absolute;

    z-index: 16;

    left: 34%;
    bottom: 21%;

    font-size: 58px;

    transform: rotate(10deg);

    pointer-events: none;
}}


/* =====================================================
   HEART STICKER
   ===================================================== */

.big-heart {{

    position: absolute;

    z-index: 16;

    left: 31%;
    bottom: 10%;

    font-size: 65px;

    transform: rotate(-10deg);

    filter:
        drop-shadow(
            0 7px 6px
            rgba(0,0,0,0.25)
        );

    pointer-events: none;
}}


/* =====================================================
   LITTLE STARS
   ===================================================== */

.star-one {{

    position: absolute;

    left: 16%;
    top: 35%;

    font-size: 38px;

    color: #f7d98d;

    z-index: 13;

    pointer-events: none;
}}


.star-two {{

    position: absolute;

    left: 36%;
    bottom: 29%;

    font-size: 42px;

    color: #f7d98d;

    z-index: 13;

    pointer-events: none;
}}


/* =====================================================
   PAPER NOTES
   ===================================================== */

.note {{

    position: absolute;

    z-index: 8;

    background:
        linear-gradient(
            145deg,
            #f3e3c2,
            #e5cfa6
        );

    color: #681111;

    padding: 12px 22px;

    font-family:
        "Brush Script MT",
        "Segoe Script",
        cursive;

    font-size: 25px;

    box-shadow:
        0 7px 16px rgba(0,0,0,0.24);

    pointer-events: none;
}}


/* Favourite note */

.note-favourite {{

    left: 7%;
    top: 9%;

    transform: rotate(-7deg);

    clip-path: polygon(
        0 5%,
        97% 0,
        100% 90%,
        88% 100%,
        65% 93%,
        45% 100%,
        20% 92%,
        0 100%
    );
}}


/* Made With Love note */

.note-you-me {{

    left: 20%;
    bottom: 8%;

    transform: rotate(5deg);

    clip-path: polygon(
        2% 0,
        100% 7%,
        96% 94%,
        78% 100%,
        55% 92%,
        30% 100%,
        0 91%
    );
}}


/* =====================================================
   MAIN CONTENT
   ===================================================== */

.content {{

    position: absolute;

    inset: 0;

    z-index: 20;

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 75px;

    padding: 35px 6%;
}}


/* =====================================================
   LEFT PHOTO AREA
   ===================================================== */

.photo-area {{

    width: 48%;

    height: 100%;

    display: flex;

    align-items: center;

    justify-content: center;

    position: relative;
}}


/* Large Polaroid */

.polaroid {{

    width: 410px;

    background: #f7f0e2;

    padding: 14px 14px 62px 14px;

    position: relative;

    transform: rotate(-5deg);

    box-shadow:
        0 20px 40px rgba(0,0,0,0.38);

    z-index: 30;
}}


/* Tape */

.tape {{

    position: absolute;

    top: -18px;

    left: 130px;

    width: 150px;

    height: 39px;

    background:
        rgba(211,182,138,0.84);

    transform: rotate(2deg);

    z-index: 40;
}}


/* Photo */

.photo {{

    display: block;

    width: 100%;

    height: 330px;

    object-fit: cover;

    border: 1px solid #ddd2bd;
}}


/* Polaroid bottom */

.polaroid-caption {{

    position: absolute;

    bottom: 10px;

    left: 0;

    width: 100%;

    text-align: center;

    color: #681111;

    font-family:
        "Brush Script MT",
        "Segoe Script",
        cursive;

    font-size: 29px;

    font-weight: 600;
}}


/* Teddy on Polaroid */

.polaroid-kiss {{

    position: absolute;

    right: -38px;

    bottom: 27px;

    font-size: 54px;

    transform: rotate(-10deg);

    z-index: 50;
}}


/* =====================================================
   RIGHT SIDE
   ===================================================== */

.password-area {{

    width: 42%;

    max-width: 520px;

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    position: relative;
}}


/* =====================================================
   TITLE
   ===================================================== */

.title {{

    color: white;

    font-family:
        "Brush Script MT",
        "Segoe Script",
        cursive;

    font-size: 61px;

    line-height: 1;

    text-align: center;

    margin-bottom: 16px;
}}


/* =====================================================
   CLUE
   ===================================================== */

.clue {{

    color: #f9e7e7;

    font-size: 18px;

    text-align: center;

    margin-bottom: 20px;
}}


/* =====================================================
   FOUR CIRCLES
   ===================================================== */

.password-circles {{

    display: flex;

    justify-content: center;

    gap: 15px;

    margin-bottom: 22px;
}}


.circle {{

    width: 19px;

    height: 19px;

    border: 2px solid white;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    color: #650909;

    font-size: 10px;
}}


.circle.filled {{

    background: white;
}}


/* =====================================================
   KEYPAD
   ===================================================== */

.keypad {{

    display: grid;

    grid-template-columns:
        repeat(4, 58px);

    gap: 12px;

    justify-content: center;
}}


.key {{

    width: 58px;

    height: 58px;

    border-radius: 50%;

    border: 2px solid white;

    background: #fff8f3;

    color: #a20c0c;

    font-size: 20px;

    font-weight: 600;

    cursor: pointer;

    box-shadow:
        0 5px 12px rgba(0,0,0,0.22);

    transition:
        transform 0.12s ease,
        background 0.12s ease;
}}


.key:hover {{

    transform: scale(1.07);

    background: white;
}}


.key:active {{

    transform: scale(0.93);
}}


/* =====================================================
   ACTION BUTTONS
   ===================================================== */

.actions {{

    width: 268px;

    display: flex;

    justify-content: space-between;

    margin-top: 12px;
}}


.action {{

    width: 58px;

    height: 58px;

    border-radius: 50%;

    border: 2px solid white;

    background: #fff8f3;

    color: #a20c0c;

    font-size: 20px;

    cursor: pointer;

    box-shadow:
        0 5px 12px rgba(0,0,0,0.22);
}}


/* =====================================================
   ERROR
   ===================================================== */

.message {{

    margin-top: 16px;

    padding: 7px 20px;

    background: #efb7b0;

    color: #6b1111;

    font-family:
        "Brush Script MT",
        "Segoe Script",
        cursive;

    font-size: 23px;

    transform: rotate(-1deg);

    box-shadow:
        0 5px 10px rgba(0,0,0,0.15);

    display: none;
}}


/* =====================================================
   SUCCESS
   ===================================================== */

.success {{

    margin-top: 16px;

    color: white;

    font-family:
        "Brush Script MT",
        "Segoe Script",
        cursive;

    font-size: 27px;

    display: none;
}}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 900px) {{

    .screen {{
        min-height: 700px;
    }}

    .content {{

        flex-direction: column;

        gap: 25px;

        padding: 25px 15px;

        overflow: hidden;
    }}

    .photo-area {{

        width: 100%;

        height: auto;
    }}

    .password-area {{

        width: 100%;

        max-width: 430px;
    }}

    .polaroid {{

        width: 290px;
    }}

    .photo {{

        height: 220px;
    }}

    .title {{

        font-size: 47px;
    }}

    .note,
    .decor,
    .flower,
    .rose,
    .kiss,
    .birthday-sticker,
    .special-sticker,
    .birthday-label,
    .big-ribbon,
    .big-heart,
    .star-one,
    .star-two {{
        display: none;
    }}

}}


</style>

</head>


<body>


<div class="screen">


    <!-- =================================================
         TORN PAPER CORNERS
         ================================================= -->

    <div class="paper-corner corner-top-left"></div>

    <div class="paper-corner corner-top-right"></div>

    <div class="paper-corner corner-bottom-left"></div>

    <div class="paper-corner corner-bottom-right"></div>


    <!-- =================================================
         COFFEE STAINS
         ================================================= -->

    <div class="coffee-stain stain-one"></div>

    <div class="coffee-stain stain-two"></div>


    <!-- =================================================
         DECORATIONS
         ================================================= -->

    <div class="heart heart-one">♡</div>

    <div class="heart heart-two">♥</div>

    <div class="heart heart-three">♡</div>

    <div class="heart heart-four">♡</div>

    <div class="heart heart-five">♥</div>

    <div class="heart heart-six">♡</div>

    <div class="heart heart-seven">♥</div>

    <div class="heart heart-eight">♡</div>


    <div class="flower flower-left">🌺</div>

    <div class="flower flower-top">🌸</div>

    <div class="rose">🌹</div>

    <div class="kiss">💋</div>

    <div class="heart heart-nine">♡</div>


    <!-- =================================================
         BIG BIRTHDAY SCRAPBOOK STICKERS
         ================================================= -->

    <div class="birthday-sticker bday-cake">
        🎂
    </div>


    <div class="birthday-sticker balloon-one">
        🎈
    </div>


    <div class="birthday-sticker balloon-two">
        🎈
    </div>


    <div class="birthday-sticker balloon-three">
        🎈
    </div>



    <div class="birthday-sticker big-gift">
        🎁
    </div>


    <div class="birthday-sticker big-sparkle-one">
        ✨
    </div>


    <div class="birthday-sticker big-sparkle-two">
        ✨
    </div>


    <div class="birthday-sticker big-sparkle-three">
        ✦
    </div>


    <!-- =================================================
         SPECIAL STICKERS
         ================================================= -->

    <div class="special-sticker">
        For You ♡
    </div>



    <div class="star-one">
        ✦
    </div>


    <div class="star-two">
        ✧
    </div>


    <!-- =================================================
         NOTES
         ================================================= -->

    <div class="note note-favourite">
        My Favourite Person ❤️
    </div>


    <div class="note note-you-me">
        Made With Love, Just for You ♡
    </div>


    <!-- =================================================
         MAIN CONTENT
         ================================================= -->

    <div class="content">


        <!-- =============================================
             PHOTO
             ============================================= -->

        <div class="photo-area">


            <div class="polaroid">


                <div class="tape"></div>


                <img
                    class="photo"
                    src="data:image/png;base64,{image_data}"
                >


                <div class="polaroid-caption">
                    Today Is All About You ♡
                </div>


                <div class="polaroid-kiss">
                    🧸
                </div>


            </div>


        </div>


        <!-- =============================================
             PASSWORD
             ============================================= -->

        <div class="password-area">


            <div class="title">
                Enter Passcode
            </div>


            <div class="clue">
                Our Meeting Date &amp; Month ❤️
            </div>


            <!-- FOUR PASSWORD CIRCLES -->

            <div
                class="password-circles"
                id="circles"
            >


                <div class="circle"></div>

                <div class="circle"></div>

                <div class="circle"></div>

                <div class="circle"></div>


            </div>


            <!-- KEYPAD -->

            <div class="keypad">


                <button
                    class="key"
                    onclick="press('1')"
                >
                    1
                </button>


                <button
                    class="key"
                    onclick="press('2')"
                >
                    2
                </button>


                <button
                    class="key"
                    onclick="press('3')"
                >
                    3
                </button>


                <button
                    class="key"
                    onclick="press('4')"
                >
                    4
                </button>


                <button
                    class="key"
                    onclick="press('5')"
                >
                    5
                </button>


                <button
                    class="key"
                    onclick="press('6')"
                >
                    6
                </button>


                <button
                    class="key"
                    onclick="press('7')"
                >
                    7
                </button>


                <button
                    class="key"
                    onclick="press('8')"
                >
                    8
                </button>


                <button
                    class="key"
                    onclick="press('*')"
                >
                    *
                </button>


                <button
                    class="key"
                    onclick="press('9')"
                >
                    9
                </button>


                <button
                    class="key"
                    onclick="press('0')"
                >
                    0
                </button>


                <button
                    class="key"
                    onclick="press('#')"
                >
                    #
                </button>


            </div>


            <!-- CLEAR / ENTER -->

            <div class="actions">


                <button
                    class="action"
                    onclick="clearCode()"
                >
                    ×
                </button>


                <button
                    class="action"
                    onclick="checkCode()"
                >
                    ✓
                </button>


            </div>


            <!-- ERROR -->

            <div
                class="message"
                id="errorMessage"
            >
                Hmm… try again ❤️
            </div>


            <!-- SUCCESS -->

            <div
                class="success"
                id="successMessage"
            >
                Correct ❤️
            </div>


        </div>


    </div>


</div>


<!-- =====================================================
     JAVASCRIPT
     ===================================================== -->

<script>


let enteredCode = "";

const correctCode = "3008";


function press(number) {{

    if (enteredCode.length >= 4) {{
        return;
    }}


    if (!/^[0-9]$/.test(number)) {{
        return;
    }}


    enteredCode += number;


    updateCircles();


    document.getElementById(
        "errorMessage"
    ).style.display = "none";


    document.getElementById(
        "successMessage"
    ).style.display = "none";

}}


function updateCircles() {{

    const circles =
        document.querySelectorAll(
            ".circle"
        );


    circles.forEach(
        (circle, index) => {{

            if (
                index <
                enteredCode.length
            ) {{

                circle.classList.add(
                    "filled"
                );


                circle.innerHTML = "♥";


            }} else {{

                circle.classList.remove(
                    "filled"
                );


                circle.innerHTML = "";

            }}

        }}
    );

}}


function clearCode() {{

    enteredCode = "";


    updateCircles();


    document.getElementById(
        "errorMessage"
    ).style.display = "none";


    document.getElementById(
        "successMessage"
    ).style.display = "none";

}}


function checkCode() {{

    if (
        enteredCode === correctCode
    ) {{

        document.getElementById(
            "successMessage"
        ).style.display = "block";

        document.getElementById(
            "errorMessage"
        ).style.display = "none";

        setTimeout(() => {{
            window.parent.postMessage({{ type: "birthday-navigate", page: "page2" }}, "*");
        }}, 650);


    }} else {{

        document.getElementById(
            "errorMessage"
        ).style.display = "block";


        document.getElementById(
            "successMessage"
        ).style.display = "none";


        enteredCode = "";


        updateCircles();

    }}

}}


</script>


</body>

</html>

"""


# =========================================================
# MERGED MULTI-PAGE WEBSITE
# =========================================================

PAGE2_PATH = Path(__file__).parent / "page2.html"
PAGE3_PATH = Path(__file__).parent / "page3.html"
PAGE4_PATH = Path(__file__).parent / "page4.html"
GIFT_IMAGE_PATH = Path(__file__).parent / "WhatsApp Image 2026-10-11 at 19.18.35.jpeg"

page2_html = PAGE2_PATH.read_text(encoding="utf-8")
page3_html = PAGE3_PATH.read_text(encoding="utf-8")
page4_html = PAGE4_PATH.read_text(encoding="utf-8")

# Connect the Next button on Page 2 to Page 3.
page2_html = re.sub(
    r"function goToNextPage\(\) \{.*?\n\}",
    'function goToNextPage() {\n    window.parent.postMessage({ type: "birthday-navigate", page: "page3" }, "*");\n}',
    page2_html,
    count=1,
    flags=re.S,
)

# Connect YES on Page 3 to Page 4 after the celebratory message.
page3_html = page3_html.replace(
    "    // We'll connect this to Page 4 when we build it.",
    '    setTimeout(() => { window.parent.postMessage({ type: "birthday-navigate", page: "page4" }, "*"); }, 900);',
)

def image_data_uri(path):
    suffix = path.suffix.lower()
    mime = "image/png" if suffix == ".png" else "image/jpeg"
    with open(path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("ascii")
    return f"data:{mime};base64,{encoded}"

# Keep the gift photo embedded inside the page so it works in the merged iframe.
page4_html = page4_html.replace(
    'src="WhatsApp Image 2026-10-11 at 19.18.35.jpeg"',
    'src="GIFT_IMAGE_DATA_URI_PLACEHOLDER"'
)
page4_html = page4_html.replace(
    "GIFT_IMAGE_DATA_URI_PLACEHOLDER",
    image_data_uri(GIFT_IMAGE_PATH)
)

# The pages are isolated in iframes so their existing CSS/designs do not affect each other.
pages = {
    "page1": html_code,
    "page2": page2_html,
    "page3": page3_html,
    "page4": page4_html,
}
# Escape '<' so page markup cannot prematurely close the parent script element.
pages_json = json.dumps(pages, ensure_ascii=False).replace("<", "\\u003c")

shell_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; }}
.page-frame {{ position: fixed; inset: 0; width: 100%; height: 100%; border: 0; display: none; background: #650909; }}
.page-frame.active {{ display: block; }}
</style>
</head>
<body>
<iframe class="page-frame active" id="frame-page1" title="Birthday passcode"></iframe>
<iframe class="page-frame" id="frame-page2" title="Birthday letter"></iframe>
<iframe class="page-frame" id="frame-page3" title="Birthday surprise question"></iframe>
<iframe class="page-frame" id="frame-page4" title="Birthday surprises"></iframe>
<script>
const pageDocuments = {pages_json};
const loadedFrames = new Set();
function showPage(pageId) {{
    document.querySelectorAll('.page-frame').forEach(frame => frame.classList.remove('active'));
    const frame = document.getElementById('frame-' + pageId);
    if (!frame) return;
    frame.classList.add('active');
    if (!loadedFrames.has(pageId)) {{
        frame.srcdoc = pageDocuments[pageId];
        loadedFrames.add(pageId);
    }}
}}
window.addEventListener('message', event => {{
    const data = event.data;
    if (data && data.type === 'birthday-navigate' && ['page2','page3','page4'].includes(data.page)) {{
        showPage(data.page);
    }}
}});
// Load the first page using the same isolated-frame setup as the other pages.
const firstFrame = document.getElementById('frame-page1');
firstFrame.srcdoc = pageDocuments.page1;
loadedFrames.add('page1');
</script>
</body>
</html>
"""

components.html(shell_html, height=760, scrolling=False)
