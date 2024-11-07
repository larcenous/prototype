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
# 탭 구성
tab1, tab2, tab3, tab4 = st.tabs(["정보/소개", "포트폴리오", "수익률", "최근 보고서"])

with tab1:
    st.markdown("### 정보/소개")
    st.write("이 페이지에서는 ETF의 정보와 소개를 제공합니다.")

with tab2:
    st.markdown("### 포트폴리오")
    st.write("이 페이지에서는 ETF의 포트폴리오 구성 정보를 제공합니다.")

with tab3:
    st.markdown("### 수익률")
    st.write("이 페이지에서는 ETF의 수익률 정보를 제공합니다.")

with tab4:
    st.markdown("### 최근 보고서")
    st.write("이 페이지에서는 ETF의 최근 보고서를 제공합니다.")