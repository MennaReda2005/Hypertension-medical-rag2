import streamlit as st

from src.rag.pipeline import ask_medical_question


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# =========================================================
# SIMPLE CSS
# =========================================================

st.markdown("""
<style>

    /* Page */
    .stApp {
        background-color: #f5faff;
    }

    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hide Streamlit menu/footer */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Main title */
    .main-title {
        text-align: center;
        color: #123b5d;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #607d8b;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Info boxes */
    .info-box {
        background-color: white;
        border: 1px solid #dcecf5;
        border-radius: 15px;
        padding: 18px;
        text-align: center;
        height: 120px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
    }

    .info-icon {
        font-size: 25px;
    }

    .info-title {
        color: #123b5d;
        font-weight: 700;
        margin-top: 5px;
    }

    .info-text {
        color: #78909c;
        font-size: 12px;
        margin-top: 5px;
    }

    /* Question title */
    .question-title {
        color: #123b5d;
        font-size: 25px;
        font-weight: 800;
        margin-top: 35px;
        margin-bottom: 5px;
    }

    .question-subtitle {
        color: #78909c;
        font-size: 14px;
        margin-bottom: 15px;
    }

    /* Answer */
    .answer-box {
        background-color: white;
        border: 1px solid #dcecf5;
        border-left: 5px solid #2196f3;
        border-radius: 15px;
        padding: 25px;
        margin-top: 25px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    }

    .answer-title {
        color: #123b5d;
        font-size: 21px;
        font-weight: 800;
        margin-bottom: 15px;
    }

    .answer-text {
        color: #37474f;
        font-size: 16px;
        line-height: 1.8;
    }

    /* Disclaimer */
    .disclaimer {
        background-color: #fff8e1;
        border: 1px solid #ffe082;
        border-radius: 12px;
        padding: 15px;
        margin-top: 30px;
        color: #795548;
        font-size: 12px;
        text-align: center;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🩺 MediGuide AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Medical Information Assistant powered by RAG & Gemini'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FEATURES
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:
    st.markdown("""
    <div class="info-box">
        <div class="info-icon">🔎</div>
        <div class="info-title">Smart Retrieval</div>
        <div class="info-text">
            Finds relevant medical information
            from the knowledge base.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="info-box">
        <div class="info-icon">🧠</div>
        <div class="info-title">Gemini AI</div>
        <div class="info-text">
            Generates a clear response
            using the retrieved context.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("""
    <div class="info-box">
        <div class="info-icon">📚</div>
        <div class="info-title">Evidence-Based</div>
        <div class="info-text">
            Answers are grounded in
            your medical documents.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# QUESTION
# =========================================================

st.markdown(
    '<div class="question-title">Ask a Medical Question</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="question-subtitle">'
    'Ask a question related to the medical knowledge available in the system.'
    '</div>',
    unsafe_allow_html=True
)


question = st.text_area(
    "Your question",
    placeholder=(
        "Example:\n"
        "What lifestyle changes are recommended "
        "for managing hypertension?"
    ),
    height=140,
    label_visibility="collapsed"
)


# =========================================================
# BUTTON
# =========================================================

if st.button(
    "🔎 Get Answer",
    use_container_width=True
):

    # -----------------------------------------
    # EMPTY QUESTION
    # -----------------------------------------

    if not question.strip():

        st.warning(
            "Please enter a medical question first."
        )

    else:

        # -----------------------------------------
        # PROCESS
        # -----------------------------------------

        with st.spinner(
            "🔎 Searching medical knowledge and generating answer..."
        ):

            try:

                answer = ask_medical_question(
                    question.strip()
                )

                # ---------------------------------
                # CHECK RESPONSE
                # ---------------------------------

                if not answer:

                    st.warning(
                        "No answer was generated."
                    )

                else:

                    # -----------------------------
                    # ANSWER
                    # -----------------------------

                    st.markdown(
                        '<div class="answer-box">',
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        '<div class="answer-title">'
                        '🩺 Medical Guidance'
                        '</div>',
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        answer
                    )

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

            except Exception as e:

                st.error(
                    "❌ The system could not process your question."
                )

                st.warning(
                    "The problem may be related to "
                    "the medical retrieval system, Gemini API, "
                    "or the API key."
                )

                with st.expander(
                    "🔧 Show technical error"
                ):

                    st.exception(e)


# =========================================================
# EXAMPLE QUESTIONS
# =========================================================

st.markdown("---")

st.markdown(
    "### 💡 Example Questions"
)

examples = [
    "What lifestyle changes are recommended for managing hypertension?",
    "What are the common risk factors for hypertension?",
    "What complications can uncontrolled hypertension cause?"
]


for example in examples:

    st.markdown(
        f"- {example}"
    )


# =========================================================
# DISCLAIMER
# =========================================================

st.markdown("""
<div class="disclaimer">

⚠️ <b>Important:</b>
MediGuide AI provides medical information for educational purposes only.
It does not replace professional medical diagnosis or treatment.

</div>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    "<p style='text-align:center; color:#90a4ae; "
    "font-size:12px; margin-top:25px;'>"
    "MediGuide AI • RAG Medical Knowledge Assistant"
    "</p>",
    unsafe_allow_html=True
)