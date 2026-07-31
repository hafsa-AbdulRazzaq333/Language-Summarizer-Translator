# cd "C:\Users\ALL AtoZ\Desktop\Main Projects\Language-Translator-main"
# venv\Scripts\activate
# streamlit run app.py

import streamlit as st
from utils.controller import summarize_and_translate

st.set_page_config(
    page_title="LingoFlow AI",
    page_icon="✦",
    layout="wide",
)

if "view" not in st.session_state:
    st.session_state.view = "landing"

if "result_summary" not in st.session_state:
    st.session_state.result_summary = ""

if "result_translation" not in st.session_state:
    st.session_state.result_translation = ""

st.markdown(
    """
    <style>
    :root {
        --bg: #f6f8ff;
        --surface: #ffffff;
        --surface-2: #f9fbff;
        --border: #e6ebf8;
        --text: #111827;
        --muted: #64748b;
        --primary: #5467ff;
        --primary-dark: #3f53d8;
        --accent: #8b5cf6;
        --success: #0f766e;
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f8faff 0%, #f4f7ff 100%);
    }

    .block-container {
        padding-top: 0.85rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    .landing-shell {
        padding: 0.55rem 0 1.2rem;
        animation: fadeIn 420ms ease;
    }

    .hero-card {
        background: linear-gradient(135deg, rgba(84,103,255,0.11), rgba(139,92,246,0.10));
        border: 1px solid var(--border);
        border-radius: 28px;
        padding: 1.45rem 1.6rem 1.3rem;
        box-shadow: 0 20px 48px rgba(15, 23, 42, 0.06);
        margin-bottom: 0.85rem;
    }

    .brand-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        background: rgba(255,255,255,0.9);
        border: 1px solid rgba(84,103,255,0.14);
        color: var(--primary);
        border-radius: 999px;
        padding: 0.45rem 0.8rem;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.85rem;
    }

    .hero-title {
        font-size: clamp(2rem, 3.2vw, 2.75rem);
        line-height: 1.08;
        font-weight: 800;
        color: var(--text);
        margin-bottom: 0.55rem;
        letter-spacing: -0.03em;
        max-width: 760px;
    }

    .hero-copy {
        font-size: 0.98rem;
        color: var(--muted);
        line-height: 1.7;
        max-width: 720px;
        margin-bottom: 0.9rem;
    }

    .hero-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 0.7rem;
        margin-top: 0.25rem;
    }

    .hero-card .stButton > button,
    .workspace-shell .stButton > button,
    .workspace-shell .stDownloadButton > button {
        border: none !important;
        border-radius: 999px !important;
        padding: 0.78rem 1.15rem !important;
        background: linear-gradient(135deg, var(--primary), var(--accent)) !important;
        color: white !important;
        font-weight: 700 !important;
        box-shadow: 0 12px 24px rgba(84,103,255,0.22) !important;
        transition: transform 180ms ease, box-shadow 180ms ease !important;
    }

    .hero-card .stButton > button:hover,
    .workspace-shell .stButton > button:hover,
    .workspace-shell .stDownloadButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 28px rgba(84,103,255,0.26) !important;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.8rem;
        margin-top: 0.35rem;
    }

    .feature-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 0.95rem 1rem;
        box-shadow: 0 12px 32px rgba(15, 23, 42, 0.05);
    }

    .feature-card h4 {
        margin: 0.2rem 0 0.4rem;
        font-size: 1rem;
        color: var(--text);
    }

    .feature-card p {
        margin: 0;
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.6;
    }

    .workspace-shell {
        animation: fadeIn 420ms ease;
    }

    .workspace-topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.4rem 0 1rem;
        gap: 0.8rem;
    }

    .workspace-brand {
        font-size: 1.05rem;
        font-weight: 800;
        color: var(--text);
        letter-spacing: -0.02em;
    }

    .workspace-grid {
        display: grid;
        grid-template-columns: 1.05fr 0.95fr;
        gap: 1rem;
        align-items: start;
    }

    .panel-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 1.1rem;
        box-shadow: 0 18px 44px rgba(15, 23, 42, 0.05);
    }

    .panel-label {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: var(--primary);
        text-transform: uppercase;
        margin-bottom: 0.55rem;
    }

    .panel-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 0.25rem;
    }

    .panel-copy {
        font-size: 0.92rem;
        color: var(--muted);
        line-height: 1.6;
        margin-bottom: 0.9rem;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: rgba(15,118,110,0.08);
        color: var(--success);
        border: 1px solid rgba(15,118,110,0.12);
        border-radius: 999px;
        padding: 0.4rem 0.7rem;
        font-size: 0.82rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }

    .stTextArea textarea,
    .stTextInput input {
        border-radius: 14px !important;
    }

    .stSpinner > div {
        border-color: var(--primary) transparent transparent transparent !important;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 1000px) {
        .workspace-grid {
            grid-template-columns: 1fr;
        }

        .hero-card {
            padding: 1.25rem 1.3rem 1.1rem;
        }

        .feature-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }

    @media (max-width: 768px) {
        .hero-card {
            padding: 1.1rem;
            border-radius: 20px;
        }

        .feature-grid {
            grid-template-columns: 1fr;
        }

        .workspace-topbar {
            flex-direction: column;
            align-items: flex-start;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_landing_page():

    st.markdown("<div class='hero-card'>", unsafe_allow_html=True)
    st.markdown("<div class='brand-pill'>✦ LingoFlow AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-title'>Premium translation and summarization for modern teams.</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='hero-copy'>Turn complex content into clear summaries and fluent translations with a calm, intelligent experience designed for speed, clarity, and trust.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("<div class='hero-actions'>", unsafe_allow_html=True)
    if st.button("Get Started", key="landing_cta", use_container_width=False):
        st.session_state.view = "workspace"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class='feature-card'>
                <div class='panel-label'>⚡ Fast</div>
                <h4>Instant AI output</h4>
                <p>Generate a polished summary and translation in a single focused step.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='feature-card'>
                <div class='panel-label'>🌍 Global</div>
                <h4>Multi-language support</h4>
                <p>Work seamlessly across a wide range of languages with a clear destination selection.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class='feature-card'>
                <div class='panel-label'>🧠 Refined</div>
                <h4>Calm, premium workflow</h4>
                <p>Designed to feel elegant, focused, and effortless from first prompt to final output.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


def render_workspace():
    st.markdown("<div class='workspace-shell'>", unsafe_allow_html=True)

    top_col1, top_col2 = st.columns([1.3, 0.4])
    with top_col1:
        st.markdown(
            """
            <div class='workspace-topbar'>
                <div class='workspace-brand'>LingoFlow AI Workspace</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with top_col2:
        if st.button("← Back home", use_container_width=True):
            st.session_state.view = "landing"
            st.session_state.result_summary = ""
            st.session_state.result_translation = ""
            st.rerun()

    st.markdown("<div class='workspace-grid'>", unsafe_allow_html=True)
    left_col, right_col = st.columns([1.02, 0.98], gap="large")

    with left_col:
        st.markdown("<div class='panel-card'>", unsafe_allow_html=True)
        st.markdown("<div class='panel-label'>✍️ Input</div>", unsafe_allow_html=True)
        st.markdown("<div class='panel-title'>Create your translation task</div>", unsafe_allow_html=True)
        st.markdown("<div class='panel-copy'>Paste your source text, choose a destination language, and generate your refined result in one pass.</div>", unsafe_allow_html=True)

        with st.form(key="translate_form"):
            sentence = st.text_area(
                "Text to summarize and translate",
                height=220,
                placeholder="Paste your article, message, or notes here...",
            )

            languages = [
                "French",
                "Spanish",
                "German",
                "Chinese",
                "Japanese",
                "Russian",
                "Arabic",
                "Portuguese",
                "Hindi",
                "Urdu",
                "Bengali",
                ]

            col_a, col_b = st.columns([1.1, 0.9])
            with col_a:
                target_language = st.selectbox("Target language", languages)
            with col_b:
                if target_language == "Other":
                    custom_language = st.text_input(
                        "Specify language",
                        placeholder="e.g. Korean",
                    )
                else:
                    custom_language = ""

            submit = st.form_submit_button("Generate result", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        st.markdown("<div class='panel-card'>", unsafe_allow_html=True)
        st.markdown("<div class='panel-label'>✨ Output</div>", unsafe_allow_html=True)
        if st.session_state.result_summary and st.session_state.result_translation:
            st.markdown("<div class='status-pill'>✓ Ready to review</div>", unsafe_allow_html=True)
            st.markdown("<div class='panel-title'>Summary</div>", unsafe_allow_html=True)
            st.markdown("<div class='panel-copy'>A concise, polished version of the original content.</div>", unsafe_allow_html=True)
            st.text_area("Summary", value=st.session_state.result_summary, height=130, disabled=True)

            st.markdown("<div class='panel-title'>Translation</div>", unsafe_allow_html=True)
            st.markdown("<div class='panel-copy'>The translated version of the summarized text.</div>", unsafe_allow_html=True)
            st.text_area("Translated text", value=st.session_state.result_translation, height=170, disabled=True)

            st.download_button(
                "Download translation as TXT",
                data=st.session_state.result_translation,
                file_name="translation.txt",
                mime="text/plain",
                use_container_width=True,
            )
        else:
            st.markdown("<div class='panel-title'>Your results will appear here</div>", unsafe_allow_html=True)
            st.markdown("<div class='panel-copy'>Generate a summary and translation to view a premium output experience with clear formatting and export support.</div>", unsafe_allow_html=True)
            st.info("The workspace stays focused on one task at a time: input, generate, review.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if submit:
        selected_language = custom_language if target_language == "Other" else target_language
        if sentence.strip() and selected_language.strip():
            with st.spinner("Crafting your summary and translation..."):
                summary, translation = summarize_and_translate(sentence, selected_language)
            st.session_state.result_summary = summary
            st.session_state.result_translation = translation
            st.success("Completed successfully")
        else:
            st.error("Please enter your text and select a target language.")


if st.session_state.view == "landing":
    render_landing_page()
else:
    render_workspace()
