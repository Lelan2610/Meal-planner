import openai
import streamlit as st

st.title("Meal Planner")
st.write("Chào mừng bạn đến với ứng dụng lập kế hoạch bữa ăn!")

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

    # Sử dụng API mới của OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Hoặc bạn có thể thay bằng "gpt-3.5-turbo" nếu muốn tiết kiệm chi phí
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    
    return response.choices[0].message['content']
