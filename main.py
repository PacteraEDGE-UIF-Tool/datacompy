
from requests import head, options
import streamlit.components.v1 as components
import this
from tkinter import N
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import numpy as np
# for generate unique widget key
from uuid import uuid4
import streamlit.components.v1 as components
import pathlib
import os

#Page title
st.title('Log comparison and analysis')


# Global variables
first_df = None
second_df = None
result_df = None
DATA_MAX_NUMBER = 10000
DATAFRME_DISPLAY_WIDTH = None
LIST_COLUMNS_HAVE_BEEN_SELECT = None

# =======================================================
# # Declare the callback function is used to execute the comparison logic.
# =======================================================

def onComparisonButtonClick():
  if first_df is None:
    st.error("There is error in generating the first dataframe, please check the format of the uploaded file.")
  elif second_df is None:
    st.error("There is error in generating the second dataframe, please check the format of the uploaded file.")
  else:
    # Create a text element and let the reader know the data is loading.
    # data_load_state = st.text('comparing data...')
    with st.spinner('comparing data ....'):
    # result = difference between two data frame
    # left_result_df=pd.merge(first_df, second_df, how='left', indicator=True)
    # left_result_df=left_result_df.drop(left_result_df[left_result_df._merge=="both"].index)
      result_df = pd.concat([first_df, second_df], keys=[
                            "first", "second"]).drop_duplicates(keep=False)

      num_different_data = len(result_df.index)
      st.write("The number of different data is:" + str(num_different_data))

      # Get the ID(index) by the name of the different dataset
      the_list_of_left_index = list(result_df.loc['first'].index)
      the_list_of_right_index = list(result_df.loc['second'].index)

      # Notify the reader that the data was successfully loaded.
      # data_load_state.text('Comparing data...done!')

      # split the display screen into left and right
      col1, col2 = st.columns(2)

      # highlight the different data with ID
      with col1:
        st.header("Form 1")
        st.dataframe(first_df.style.apply(
            highlight, the_list=the_list_of_left_index, axis=1), width=DATAFRME_DISPLAY_WIDTH)
      with col2:
        st.header("Form 2")
        st.dataframe(second_df.style.apply(
            highlight, the_list=the_list_of_right_index, axis=1), width=DATAFRME_DISPLAY_WIDTH)
    st.success('Done!')
    # draw dataframe
    st.header("Difference message in detail.")
    st.dataframe(result_df)
    
    current_path=pathlib.Path(__file__).parent.resolve()
    #========================================================
    #Show the save button only result_df!=0
    #========================================================
    output_file_name = st.text_input('Output file name', 'compare_result.csv')
      # Make folder picker dialog appear on top of other windows
    if len(output_file_name) == 0:
        output_file_name="compare_result.csv"
    out_file_path=os.path.join(current_path, output_file_name)
    st.write(out_file_path)
    st.button("savefile", key=str("save_button"), help=None,  disabled=False, on_click=saveFile(out_file_path, result_df))

def saveFile(file_path, df):
  open(file_path, 'w+', encoding="utf-8").write(df.to_csv())


# ========================================================
# Generate pandas dataframe style, render the background into yellow,
# if the row id in the list
# ========================================================
def highlight(s, the_list):
    if s.name in the_list:
        return ['background-color: yellow'] * len(s)
    else:
        return ['background-color: white'] * len(s)


# =======================================================
# Uploader for the first file
# =======================================================
first_uploaded_file = st.file_uploader("Choose a file", key="first_uploader")
if first_uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    try:
      origin_first_df = pd.read_csv(first_uploaded_file, encoding='utf8')
    except IOError as e:
      print(f"There is an error occur while parsing the csv file. error message \n {e}")
      st.write("There is an error occur while parsing the csv file. please check the file format first.")

    # this will show the header
    header_of_first_df=origin_first_df.columns.values
    #show the original header
    #st.write(header_of_first_df)

    #multiple selector, the return value type is a list
    first_file_options = st.multiselect(
      'Please select the column that you want to conduct comparision process.',
      options=list(header_of_first_df),
      default=list(header_of_first_df)
      )
    st.write('You selected:', first_file_options)

    #drop the non-selected columns from the original one.
    first_not_been_select_list=[x for x in origin_first_df if x not in first_file_options]
    first_df=origin_first_df
    first_df=first_df.drop(columns=first_not_been_select_list)
  

    #select the range of number going to be processed
    first_row_data_number=first_df.shape[0]

    first_recommend_data_number=first_row_data_number 
    if first_recommend_data_number> DATA_MAX_NUMBER:
      first_recommend_data_number=DATA_MAX_NUMBER

    first_range_values = st.slider(
     'Select a range of index number',
     0, first_row_data_number, (0, first_recommend_data_number))
    st.write('Values:', first_range_values)
    first_df=first_df.loc[first_range_values[0]:first_range_values[1]]
    st.dataframe(first_df)


# =======================================================
# Uploader for the second file
# =======================================================
second_uploaded_file = st.file_uploader("Choose a file", key="second_uploader")
if second_uploaded_file is not None:
    try:
      origin_second_df = pd.read_csv(second_uploaded_file, encoding='utf8')
    except IOError as e:
      print(f"There is an error occur while parsing the csv file. error message \n {e}")
      st.write("There is an error occur while parsing the csv file. please check the file format first.")

    #Original header of the second dataframe
    header_of_second_df = origin_second_df.columns.values

    #multiple selector, the return value type is a list
    #the default value is the columns been selected in first step.


    #if the user upload the second file first, some variable will become not defined,
    #the following is a mitigation approach to such problem.
    try:
      second_file_options = st.multiselect(
        'Please select the column that you want to conduct comparion process.',
        options=list(header_of_first_df),
        default=list(first_file_options)
        )
      st.write('You selected:', second_file_options)
      if first_file_options != second_file_options:
        st.warning('The selected columns is not the same, make sure what you are doing before continue.')
    except NameError:
        second_file_options = st.multiselect(
        'Please select the column that you want to conduct comparion process.',
        options=list(header_of_second_df),
        default=list(header_of_second_df)
        )


    #drop the non-selected columns from the original one.
    second_not_been_select_list=[x for x in origin_second_df if x not in second_file_options]
    second_df=origin_second_df
    second_df=second_df.drop(columns=second_not_been_select_list)

   
    #select the range of number going to be processed
    second_row_data_number=second_df.shape[0]

    second_recommend_data_number=second_row_data_number 
    if second_recommend_data_number> DATA_MAX_NUMBER:
      second_recommend_data_number=DATA_MAX_NUMBER

    second_range_values = st.slider(
     'Select a range of index number',
     0, second_row_data_number, (0, second_recommend_data_number))
    st.write('Values:', second_range_values)

    second_df=second_df.loc[second_range_values[0]:second_range_values[1]]

    st.dataframe(second_df)



# =======================================================
# Create a button that can be clicked by user
# =======================================================
st.button("execute the comparison proccess", key=str(uuid4()), help=None, on_click=onComparisonButtonClick, disabled=False)







def material_login(title, key=None):
    return _material_login(title=title, key=key)


USERNAME = "a@a.com"
PASSWORD = "test"

_material_login = components.declare_component(
    "material_login", url="http://localhost:3001",
)

logged_in_data = material_login("Insert your account")

#st.write(logged_in_data)
