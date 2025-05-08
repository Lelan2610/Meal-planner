import streamlit as st
import openai
import os
import time
from openai import RateLimitError

# Thiết lập API key từ secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Hàm gọi API OpenAI để tạo món ăn
def generate_meal_plan(goal, mood, meal_time):
    prompt = f"""
    Tạo 1 món ăn phù hợp với:
    - Mục tiêu: {goal}
    - Tâm trạng: {mood}
    - Bữa: {meal_time}

    Mỗi món ăn hãy trình bày:
    - Tên món
    - Nguyên liệu
    - Cách làm
    - Độ khó (đơn giản/cầu kỳ)
    - Loại món (mặn/chay)
    - Mục tiêu dinh dưỡng
    """

    for attempt in range(3):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Bạn là một đầu bếp Việt chuyên nghiệp."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content

        except RateLimitError:
            time.sleep(5)
        except Exception as e:
            return f"Đã xảy ra lỗi: {e}"

    return "API đang quá tải. Vui lòng thử lại sau."

# Giao diện người dùng với Streamlit
st.set_page_config(page_title="Meal Planner AI", page_icon="🍽️")

st.title("Trợ lý thực đơn thông minh")
st.markdown("Chọn tiêu chí bên dưới để gợi ý món ăn:")

goal = st.selectbox("Mục tiêu", ["giảm cân", "giữ cân", "tăng cân"])
mood = st.selectbox("Tâm trạng", ["vui", "bình thường", "buồn", "mệt mỏi"])
meal_time = st.selectbox("Bữa ăn", ["sáng", "trưa", "tối"])

if st.button("Gợi ý món ăn"):
    with st.spinner("Đang tạo món ăn..."):
        meal_plan = generate_meal_plan(goal, mood, meal_time)
    st.markdown("### Gợi ý món ăn:")
    st.markdown(meal_plan)
