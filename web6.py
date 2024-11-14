import streamlit as st
st.title("Điền thông tin giới thiệu bản thân")
mybar = st.progress(0)
quiz = ["Họ và tên:",
        "Ngày tháng năm sinh",
        "Nơi sinh",
        "Sở thích"]
answers = []
lenquiz = len(quiz)
for i in range (lenquiz):
    answer = st.text_input( quiz[i],"")
    if answer !="":
        answers.append(answer)
if st.button("Confirm"):
    if len(answers) ==lenquiz:
        mybar.progress(100)
        st.write("Bạn đã điền đầy đủ thông tin!")
        st.balloons()
    else:
        mybar.progress(len(answers)/lenquiz)
        st.write("Bạn chưa điền đầy đủ thông tin!")

for i in range (len(answers)):

    st.write(":white_check_mark: ",quiz[i],answers[i])
