#import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards

#...............................................................................................................................

#Setting page
st.set_page_config(page_title="Cluster_Dashboard", page_icon=":school:", layout="wide")
#main page title
#st.title("🎓CLUSTER_DASHBOARD📊")
st.markdown(
    "<h1 style='text-align: center;'>📊CLUSTER_ANALYSIS_DASHBOARD</h1>",
    unsafe_allow_html=True
)
st.markdown('<style>h1{padding-top:2rem;}</style>', unsafe_allow_html=True)
#st.subheader("📂 Upload Excel or CSV Score File for Analysis")

# File uploader
uploaded_file = st.sidebar.file_uploader("📂:⬆:Upload CSV or Excel file:", type=["csv", "xlsx", "xls"])

@st.cache_data
def get_data(file):
    if file:
        try:
            if file.name.endswith('.csv'):
                return pd.read_csv(file)
            else:
                return pd.read_excel(file)
        except Exception as e:
            st.error(f"An error occurred while reading the file: {e}")
    return None

if uploaded_file:
    data = get_data(uploaded_file)
    if data is not None:
        with open('style.css') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        st.subheader("COUNT_SUMMARY:")
        st.sidebar.subheader('Filter_Here:')

        if 'GENDER' in data.columns and 'GRADE' in data.columns:
            gender = st.sidebar.radio("Select_Gender:", options=data['GENDER'].unique())
            st.sidebar.subheader('Population_Per_Grade')
            grade = st.sidebar.multiselect("Select_Grade:", options=data['GRADE'].unique(), default=data['GRADE'].unique())
            #Sidebar for streams
            streams = st.sidebar.multiselect('Population_Per_Stream:', options = data['STREAM'].unique(), default = data['STREAM'].unique())
            #.........................................................................................................................

            df_selected = data.query('GENDER == @gender and GRADE == @grade & STREAM == @streams')

            def metrics():
                left, mid, right = st.columns(3)
                left.metric("🧍_🧍‍♀️All_Learners:", value=data.ID.count(), delta='All_Learners')
                mid.metric("🧍Boys_Count:", value=df_selected[df_selected['GENDER'] == 'Boy'].shape[0], delta='Boys_Count')
                right.metric("🧍‍♀️Girls_Count:", value=df_selected[df_selected['GENDER'] == 'Girl'].shape[0], delta='Girls_Count')
                style_metric_cards(background_color="#121270", border_left_color="#c750a3", box_shadow="3px")

            st.divider()
            metrics()
            st.divider()
            #st.subheader("📊 ASSESSMENT_RUBRICS_VISUALIZATION:")
            st.markdown(
                        "<h1 style='text-align: center;'>📊 ASSESSMENT_SCORE_DISTRIBUTION:</h1>",
                        unsafe_allow_html=True
            )

            # Additional plotting and option menu logic goes here...
            #.....................................................................................................................................
    #Sidebar for Grades
            st.sidebar.subheader('Assessment_Per_Grade')
            grades=   st.sidebar.multiselect("Pick_Grade:", options=data['GRADE'].unique(), default=data['GRADE'].unique())
            #Sidebar for streams
            stream = st.sidebar.multiselect('Assessment_Per_Stream:', options = data['STREAM'].unique(), default = data['STREAM'].unique())
            #.....................................................................................................................................
            #Querying the grades
            df_selected=data.query('GRADE==@grades& STREAM==@stream & GRADE==@grade')
            #.....................................................................................................................................
            #Visualizing
            div1,div2,div3,div4=st.columns(4)

            #math
            def bar_math():
                theme_plotly = None  # None or streamlit
                
                with div1:  # Assuming div1 is a valid Streamlit container or section in your code
                    # Create the bar plot using Plotly Express
                    fig = px.bar(df_selected, 
                                y='MATHS',  # The column for Y-axis
                                x='MATHS',  # The column for X-axis
                                text_auto='.2s',     # Automatically display text on the bars
                                title="MATHS")
                    
                    # Replace x-axis numeric values (1, 2, 3, 4) with custom labels
                    custom_labels = {
                        1: "B.E",
                        2: "A.E",
                        3: "M.E",
                        4: "E.E"
                    }
                    
                    # Update x-axis with custom labels
                    fig.update_layout(
                        xaxis=dict(
                            tickmode='array',  # Set to 'array' for custom ticks
                            tickvals=[1, 2, 3, 4],  # X-axis values that need to be replaced
                            ticktext=[custom_labels[1], custom_labels[2], custom_labels[3], custom_labels[4]]  # Corresponding custom labels
                        )
                    )
                    
                    # Customize text appearance for the bars
                    fig.update_traces(
                        textfont_size=18,  # Font size for the text
                        textangle=0,       # Angle of the text on the bars
                        textposition="outside",  # Position the text outside the bars
                        cliponaxis=False,   # Prevent clipping of text
                        marker=dict(color='#fcba03')
                    )
                    
                    # Display the plot in the Streamlit app
                    st.plotly_chart(fig, use_container_width=True, theme="streamlit")
            #....................................................................................................................................................................................
            #bar chart
            def bar_eng():
                #theme_plotly = None  # None or streamlit
                
                with div2:  # Assuming div1 is a valid Streamlit container or section in your code
                    # Create the bar plot using Plotly Express
                    fig = px.bar(df_selected, 
                                y='ENGLISH',  # The column for Y-axis
                                x='ENGLISH',  # The column for X-axis
                                text_auto='.2s',     # Automatically display text on the bars
                                title="ENGLISH")
                    
                    # Replace x-axis numeric values (1, 2, 3, 4) with custom labels
                    custom_labels = {
                        1: "B.E",
                        2: "A.E",
                        3: "M.E",
                        4: "E.E"
                    }
                    
                    # Update x-axis with custom labels
                    fig.update_layout(
                        xaxis=dict(
                            tickmode='array',  # Set to 'array' for custom ticks
                            tickvals=[1, 2, 3, 4],  # X-axis values that need to be replaced
                            ticktext=[custom_labels[1], custom_labels[2], custom_labels[3], custom_labels[4]]  # Corresponding custom labels
                        )
                    )
                    
                    # Customize text appearance for the bars
                    fig.update_traces(
                        textfont_size=18,  # Font size for the text
                        textangle=0,       # Angle of the text on the bars
                        textposition="outside",  # Position the text outside the bars
                        cliponaxis=False,  # Prevent clipping of text
                        marker=dict(color='#03fc13')
                    )
                    
                    # Display the plot in the Streamlit app
                    st.plotly_chart(fig, use_container_width=True, theme="streamlit")

            #kiswahili
            def bar_kisw():
                theme_plotly = None  # None or streamlit
                
                with div3:  # Assuming div1 is a valid Streamlit container or section in your code
                    # Create the bar plot using Plotly Express
                    
                    fig = px.bar(df_selected, 
                                y='KISWAHILI',  # The column for Y-axis
                                x='KISWAHILI',  # The column for X-axis
                                text_auto='.2s',     # Automatically display text on the bars
                                title="KISWAHILI")
                    
                    # Replace x-axis numeric values (1, 2, 3, 4) with custom labels
                    custom_labels = {
                        1: "B.E",
                        2: "A.E",
                        3: "M.E",
                        4: "E.E"
                    }
                    
                    # Update x-axis with custom labels
                    fig.update_layout(
                        xaxis=dict(
                            tickmode='array',  # Set to 'array' for custom ticks
                            tickvals=[1, 2, 3, 4],  # X-axis values that need to be replaced
                            ticktext=[custom_labels[1], custom_labels[2], custom_labels[3], custom_labels[4]]  # Corresponding custom labels
                        )
                    )
                    
                    # Customize text appearance for the bars
                    fig.update_traces(
                        textfont_size=18,  # Font size for the text
                        textangle=0,       # Angle of the text on the bars
                        textposition="outside",  # Position the text outside the bars
                        cliponaxis=False,   # Prevent clipping of text
                        marker=dict(color='#4254f5')
                    )
                    
                    # Display the plot in the Streamlit app
                    st.plotly_chart(fig, use_container_width=True, theme="streamlit")

            #science
            def bar_scie():
                theme_plotly = None  # None or streamlit
                
                with div4:  # Assuming div1 is a valid Streamlit container or section in your code
                    # Create the bar plot using Plotly Express
                    fig = px.bar(df_selected, 
                                y='SCIENCE_TECH',  # The column for Y-axis
                                x='SCIENCE_TECH',  # The column for X-axis
                                text_auto='.2s',     # Automatically display text on the bars
                                title="SCIENCE_TECHNOLOGY")
                    
                    # Replace x-axis numeric values (1, 2, 3, 4) with custom labels
                    custom_labels = {
                        1: "B.E",
                        2: "A.E",
                        3: "M.E",
                        4: "E.E"
                    }
                    
                    # Update x-axis with custom labels
                    fig.update_layout(
                        xaxis=dict(
                            tickmode='array',  # Set to 'array' for custom ticks
                            tickvals=[1, 2, 3, 4],  # X-axis values that need to be replaced
                            ticktext=[custom_labels[1], custom_labels[2], custom_labels[3], custom_labels[4]]  # Corresponding custom labels
                        )
                    )
                    
                    # Customize text appearance for the bars
                    fig.update_traces(
                        textfont_size=18,  # Font size for the text
                        textangle=0,       # Angle of the text on the bars
                        textposition="outside",  # Position the text outside the bars
                        cliponaxis=False   # Prevent clipping of text
                    )
                    
                    # Display the plot in the Streamlit app
                    st.plotly_chart(fig, use_container_width=True, theme="streamlit")
            st.divider()
            #pie chart
            col1, col2, col3, col4, col5=st.columns(5)
            def pie_cre():
                # None or streamlit
                with col1:
                    fig = px.pie(df_selected, values='CRE', names='CRE',title="CRE")
                    fig.update_layout(legend_title="CRE_Scores", legend_y=1)
                    #fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
                    fig.update_traces(textinfo='percent+label', textposition='inside')
                    st.plotly_chart(fig, use_container_width=True, theme="streamlit")
                    

                #pie chart
            def pie_cr():
                # None or streamlit
                    with col2:
                            fig = px.pie(df_selected, values='CREATIVE_ARTS', names='CREATIVE_ARTS',title="CREATIVE_ART")
                            fig.update_layout(legend_title="Creative_Arts_Scores", legend_y=1)
                            fig.update_traces(textinfo='percent+label', textposition='inside')
                        #fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
                            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

            def pie_sst():
                    with col3:
                        fig = px.pie(df_selected, values='SST', names='SST', title='SOCIAL_STUDIES/ENVIRON..')
                        fig.update_layout(legend_title="SST_Scores", legend_y=1)
                        fig.update_traces(textinfo='percent+label', textposition='inside')
                        st.plotly_chart(fig, use_container_width=True)
             
            #pie chart
            def pie_pre():
                    with col4:
                            fig = px.pie(df_selected, values='PRE_TECH', names='PRE_TECH',title="PRE_TECHNICAL")
                            fig.update_layout(legend_title="pre_Technical_Scores", legend_y=1)
                            fig.update_traces(textinfo='percent+label', textposition='inside')
                            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

                #pie chart
            def pie_agri():
                        with col5:
                                fig = px.pie(df_selected, values='AGRICULTURE', names='AGRICULTURE',title="AGRICULTURE")
                                fig.update_layout(legend_title="Agriculture_Scores", legend_y=1)
                                fig.update_traces(textinfo='percent+label', textposition='inside')
                                st.plotly_chart(fig, use_container_width=True, theme="streamlit")

                    
            #......................................................................................................................................................................................
            #invoking the functions to display the plotted charts
            def table():
                with st.expander("Tabular"):
            #st.dataframe(df_selection,use_container_width=True)
                    shwdata = st.multiselect('Filter :', data.columns, default=["GENDER","GRADE","MATHS","ENGLISH","KISWAHILI","SCIENCE_TECH","CRE","SST","CREATIVE_ARTS"])
                    st.dataframe(df_selected[shwdata],use_container_width=True)
            #......................................................................................................................................................................................
            #option menu
            from streamlit_option_menu import option_menu
            with st.sidebar:
                    selected=option_menu(
                    menu_title="Main Menu",
                    #menu_title=None,
                    options=["Home","Table"],
                    icons=["house","book"],
                    menu_icon="cast", #option
                    default_index=0, #option
                    orientation="vertical",



                    

                    )

            if selected=="Home":
                
                bar_math()
                bar_eng()
                bar_kisw()
                bar_scie()
            

                col1, col2,col3,col4,col5 = st.columns(5)
                with col1:
                    pie_sst()
                with col2:
                    pie_cr()
                with col3:
                    pie_cre()
                with col4:
                     pie_pre()
                with col5:
                     pie_agri()


            if selected=="Table":
                metrics()
                table()
            #st.dataframe(df_selected.describe().T,use_container_width=True)

            #............................................................................................................................................................................................
        else:
            st.warning("The uploaded file must contain 'GENDER' and 'GRADE' columns.")
    else:
        st.error("Failed to load data. Please upload a valid file.")
else:
    st.info("Please upload a CSV or Excel file to get started.")   