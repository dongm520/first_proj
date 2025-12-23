import os
import streamlit as st
from kakao import *
from holiday import *
from streamlit_app import *


# 세션 상태 초기화
if "view" not in st.session_state:
    st.session_state.view = "home"

if "selected_tool" not in st.session_state:
    st.session_state.selected_tool = None

# 홈 화면
if st.session_state.view == "home":
    st.title("1조 프로젝트 결과물 짜라쨘")

    if st.button("시작하기", key="start_btn"):
        st.session_state.view = "tool"
        st.rerun()


# 툴 선택 화면

else:
    #  홈 버튼
    if st.button("홈으로 돌아가기", key="home_btn"):
        st.session_state.view = "home"
        st.session_state.selected_tool = None
        st.rerun()

   # 사이드바
    st.sidebar.title("주제 선택")

    st.session_state.selected_tool = st.sidebar.radio(
        "실행할 주제를 선택하세요",
        ("카카오톡 내용 분석", "타로 운세 보기", "공휴일 관련 노래 재생"),
        key="tool_radio"
    )

    # 선택 결과 실행
    if st.session_state.selected_tool == "카카오톡 내용 분석":
        kakao()

    elif st.session_state.selected_tool == "타로 운세 보기":
        tarot_app()

    elif st.session_state.selected_tool == "공휴일 관련 노래 재생":
        holiday()


