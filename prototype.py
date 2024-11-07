import streamlit as st

# 페이지 초기 설정
if 'page' not in st.session_state:
    st.session_state.page = "메인"

st.markdown("""
    <div style="text-align: left;">
        <h1 style="margin-bottom: 0;">NVDL</h1>
        <p style="font-size:14px; color:gray; margin-top: 0;">GraniteShares 2x Long NVDA Daily ETF</p>
    </div>
""", unsafe_allow_html=True)

# 페이지 전환 버튼
if st.session_state.page == "메인":
    col1, col2 = st.columns(2)
    with col1:
        if st.button("정보/소개"):
            st.session_state.page = "정보"
        if st.button("포트폴리오"):
            st.session_state.page = "포트폴리오"
        
    with col2:
        if st.button("수익률"):
            st.session_state.page = "수익률"
        if st.button("최근 보고서"):
            st.session_state.page = "보고서"
            
elif st.session_state.page == "정보":
    st.markdown("## 정보/소개 페이지")
    st.write("이 페이지에서는 ETF 정보와 소개를 제공합니다.")
    if st.button("메인으로 돌아가기"):
        st.session_state.page = "메인"

elif st.session_state.page == "포트폴리오":
    st.markdown("## 포트폴리오 페이지")
    st.write("이 페이지에서는 ETF의 포트폴리오 구성 정보를 제공합니다.")
    if st.button("메인으로 돌아가기"):
        st.session_state.page = "메인"

elif st.session_state.page == "수익률":
    st.markdown("## 수익률 페이지")
    st.write("이 페이지에서는 ETF의 수익률 정보를 제공합니다.")
    if st.button("메인으로 돌아가기"):
        st.session_state.page = "메인"

elif st.session_state.page == "보고서":
    st.markdown("## 최근 보고서 페이지")
    st.write("이 페이지에서는 최근 보고서를 제공합니다.")
    if st.button("메인으로 돌아가기"):
        st.session_state.page = "메인"