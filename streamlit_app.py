import streamlit
import snowflake.connector
import pandas
import requests
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')


#pick up fruits
fruits_selected=streamlit.multiselect("pick some fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]    


streamlit.dataframe(my_data_row)


streamlit.header('fruity vice fruit advice')
try:
    fruit_choice =streamlit.text_input("Enter Fruit you want to add:")
    if not fruit_choice:
      streamlit.error("Please select fruit")
    else:
        fruity_vice_response=requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
        fruity_vice_normalized=pandas.json_normalize(fruity_vice_response.json())
        streamlit.dataframe( fruity_vice_normalized)
except url_error as e:
  streamlit.error()
 
streamlit.stop()
                                                                                 
streamlit.dataframe(fruits_to_show)
my_cnx= snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
my_data_row=my_cur.fetchall()
streamlit.text("Hello from Snowflake:")

