import math
import streamlit as st
import locale 

locale.setlocale(locale.LC_ALL, '')


st.title("Winning Payout Calculator 2023")

with st.form("my_form"):
    p1 = int(st.number_input('Player one chips:', format="%d", value=0))
    p2 = int(st.number_input('Player two chips:', format="%d", value=0))
    pot = int(st.number_input('Total dollars:', format="%d", value=0))
    p = [p1, p2]
    submitted = st.form_submit_button("Submit")
    
    if submitted:

        r = float(min(p)) / sum(p)
        low_payout = math.ceil(r * pot/5.) * 5
        payouts = [low_payout, pot - low_payout]
        if p2 == min(p): payouts = list(reversed(payouts))
        p1_dollars = locale.currency(payouts[0], grouping=True)
        p2_dollars = locale.currency(payouts[1], grouping=True)
        st.write(f"P1: {p1_dollars}")
        st.write(f"P2: {p2_dollars}")
    
