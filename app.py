import streamlit as st
import openai
import os

# Lấy API key từ secret
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_meal_plan(goal, mood, meal_time):
    prompt = f"""
    Tạo 2 món ăn phù hợp với các tiêu chí sau:
    - Mục tiêu: {goal}
    - Tâm trạng: {mood}
    - Bữa ăn: {meal_time}
    
    Mỗi món hãy liệt kê:
    - Tên món
    - Nguyên liệu
    - Cách làm
    - Độ khó (đơn giản hoặc cầu kỳ)
    - Loại món (mặn hoặc chay)
    - Phù hợp bữa nào (sáng/trưa/tối)
    
    Xuất dưới dạng JSON array.
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Bạn là một đầu bếp Việt giỏi."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

# Giao diện người dùng
st.title("AI Gợi ý món ăn theo tâm trạng & mục tiêu")

goal = st.selectbox("Mục tiêu", ["giảm cân", "giữ cân", "tăng cân"])
mood = st.selectbox("Tâm trạng", ["vui", "bình thường", "buồn"])
meal_time = st.selectbox("Bữa ăn", ["sáng", "trưa", "tối"])

if st.button("Gợi ý món ăn"):
    with st.spinner("Đang tạo thực đơn..."):
        meal_plan = generate_meal_plan(goal, mood, meal_time)
        st.json(meal_plan)
