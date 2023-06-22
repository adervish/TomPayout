#
# % for i in 0 1 5 10 15 20 40 50000; do
# >   echo P1 has $i and P2 has 10 with a pot of 25. Payout is:
# >   ./payout.py $i 10 25
# > done;
# P1 has 0 and P2 has 10 with a pot of 25. Payout is:
# P1: 0
# P2: 25
# P1 has 1 and P2 has 10 with a pot of 25. Payout is:
# P1: 5
# P2: 20
# P1 has 5 and P2 has 10 with a pot of 25. Payout is:
# P1: 10
# P2: 15
# P1 has 10 and P2 has 10 with a pot of 25. Payout is:
# P1: 10
# P2: 15
# P1 has 15 and P2 has 10 with a pot of 25. Payout is:
# P1: 15
# P2: 10
# P1 has 20 and P2 has 10 with a pot of 25. Payout is:
# P1: 15
# P2: 10
# P1 has 40 and P2 has 10 with a pot of 25. Payout is:
# P1: 20
# P2: 5
# P1 has 50000 and P2 has 10 with a pot of 25. Payout is:
# P1: 20
# P2: 5

import math
import streamlit as st
import locale 

locale.setlocale(locale.LC_ALL, '')


st.title("Winning Payout Calculator 2023")

with st.form("my_form"):
    p1 = int(st.number_input('Player one chips:'))
    p2 = int(st.number_input('Player two chips:'))
    pot = int(st.number_input('Total dollars:'))
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
    
