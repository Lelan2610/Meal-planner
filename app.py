import streamlit as st
import openai

# Thêm API Key của bạn vào đây
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_meal_plan(goal, mood, meal_time):
    prompt = f"""
    Tạo 5 món ăn phù hợp với:
    - Mục tiêu: {goal}
    - Tâm trạng: {mood}
    - Bữa ăn: {meal_time}
    
    Với mỗi món hãy cung cấp:
    - Tên món
    - Nguyên liệu
    - Cách làm
    - Loại món (mặn/chay)
    - Độ khó
    - Mục tiêu dinh dưỡng
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content

st.title("Trình tạo danh sách món ăn AI")

goal = st.selectbox("Mục tiêu", ["giảm cân", "giữ cân", "tăng cân"])
mood = st.selectbox("Tâm trạng", ["vui", "bình thường", "buồn"])
meal_time = st.selectbox("Bữa ăn", ["sáng", "trưa", "tối"])

if st.button("Tạo danh sách món ăn"):
    with st.spinner("Đang tạo danh sách..."):
        meal_plan = generate_meal_plan(goal, mood, meal_time)
        st.text_area("Danh sách món ăn được đề xuất:", meal_plan, height=400)
