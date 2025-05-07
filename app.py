import openai
import streamlit as st

# Cấu hình API key của OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Lấy API key từ Streamlit Secrets

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

    # Gọi API OpenAI ChatCompletion (phiên bản mới)
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Hoặc bạn có thể thay bằng "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    
    # Trả về kết quả
    return response.choices[0].message['content']

# Streamlit UI
st.title("Meal Planner with AI")
goal = st.selectbox("Mục tiêu dinh dưỡng", ["Giảm cân", "Giữ cân", "Tăng cân"])
mood = st.selectbox("Tâm trạng", ["Vui", "Bình thường", "Mệt mỏi", "Khỏe mạnh"])
meal_time = st.selectbox("Bữa ăn", ["Sáng", "Trưa", "Tối"])

if st.button("Tạo thực đơn"):
    meal_plan = generate_meal_plan(goal, mood, meal_time)
    st.write(meal_plan)
