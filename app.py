import streamlit as st
import epitran

epi = epitran.Epitran('kor-Hang')

st.title("한국어 → IPA 변환기")

text = st.text_area("텍스트 입력", placeholder="예: 반갑습니다")

if st.button("변환하기"):
    if text:
        ipa = epi.transliterate(text)
        st.success(f"IPA: {ipa}")
    else:
        st.warning("텍스트를 입력해주세요")
