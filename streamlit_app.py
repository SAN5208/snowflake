import streamlit
import snowflake.connector
import pandas
import requests

def get_fruity_voice_data(this_fruit_choice):
        fruity_vice_response=requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
        fruity_vice_normalized=pandas.json_normalize(fruity_vice_response.json())
        return fruity_vice_normalized
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values (new_fruit)")     
        return "Thanks for adding " +new_fruit

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')


#pick up fruits
fruits_selected=streamlit.multiselect("pick some fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]    





streamlit.header('fruity vice fruit advice')
try:
    fruit_choice =streamlit.text_input("Enter Fruit you want to add:")
    if not fruit_choice:
      streamlit.error("Please select fruit")
    elif streamlit.button('Add a fruit to the list'):
                my_cnx= snowflake.connector.connect(**streamlit.secrets["snowflake"])
                #back_from_function=get_fruity_voi(ce_data(fruit_choice)
                back_from_function=insert_row_snowflake(fruit_choice)
                streamlit.text(back_from_function)
               
except:
     streamlit.error("Please check")   
