import sys
sys.path.append("C:\\path\\to\\streamlit_calendar")

from asyncio import events
import streamlit as st
import streamlit_calendar as st_calendar
import datetime
from datetime import datetime
from datetime import timedelta
import pandas as pd

dt_now = datetime.now()
# タイトル
st.title("タスク管理アプリ(仮)")


if 'item_name_1' not in st.session_state:
  st.session_state.item_name_1 = ''

if 'due_date_1' not in st.session_state:
  st.session_state.due_date_1 = ''

if 'event_calc_list' not in st.session_state:
  st.session_state["event_calc_list"] = [
    [],
    [],
    [],
  ]

if 'event_list' not in st.session_state:
  st.session_state["event_list"] = []

if 'cal' not in st.session_state:
  st.session_state.cal = ""

if 'dt_calc' not in st.session_state:
  st.session_state.dt_calc = ''


col1, col2 = st.columns(2)

with col1:
  st.session_state.item_name_1 = st.text_input("追加したい予定名", key='item1')
  if st.button('予定を追加', type = 'primary'):
    if st.session_state.item_name_1 == '':
      st.write('予定名を入力してください')
    else:
      st.session_state['event_calc_list'][0].append(str(st.session_state.item_name_1))
      st.session_state['event_calc_list'][1].append(st.session_state.due_date_1)
      event = {
      'id': '1',
      'title': str(st.session_state.item_name_1),
      'start': str(st.session_state.due_date_1),
      }
      st.session_state["event_list"].append(event)

with col2:
  st.session_state.due_date_1 = st.date_input("追加したい予定の期限日", key='limitd1')
  if st.button('予定を削除', type = 'primary'):
    try:
      event = {
      'id': '1',
      'title': str(st.session_state.item_name_1),
      'start': str(st.session_state.due_date_1),
      }
      st.session_state["event_list"].remove(event)
    except:
      st.write('その予定は存在しません')
    else:
      st.session_state['event_calc_list'][0].remove(str(st.session_state.item_name_1))
      st.session_state['event_calc_list'][1].remove(st.session_state.due_date_1)
  
for i in range(len(st.session_state['event_calc_list'][0])):
  date_string = str(st.session_state['event_calc_list'][1][i])
  date_event = datetime.strptime(date_string, '%Y-%m-%d').date()
  datetime_event = datetime.combine(date_event, datetime.min.time())
  dt_calc = datetime_event - dt_now
  event_name_2 = st.session_state['event_calc_list'][0][i]
  st.sidebar.write(f'予定名:{event_name_2}\n残り日数:{str(dt_calc.days + 1)}')
option = {
'initialviaw': 'multiMonthYear'
}
st_calendar.calendar(events = st.session_state["event_list"], options = option)
  
