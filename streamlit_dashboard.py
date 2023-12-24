import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset from CSV
file_path = './nvDataFrame2/data.csv'
df = pd.read_csv(file_path)

# Convert 'pub_date' to datetime format
df['pub_date'] = pd.to_datetime(df['pub_date'])

# Format 'pub_date' to display only the date
df['pub_date'] = df['pub_date'].dt.date

# Streamlit app
st.title('News Sentiment Analysis')

st.set_option('deprecation.showPyplotGlobalUse', False)

# Display the table
st.subheader('Table of Data')
st.write(df)

# Number of positive sentiments per day
st.subheader('Number of Positive Sentiments per Day')
df_positv_per_day = df.groupby('pub_date')['numPositv'].sum()
st.bar_chart(df_positv_per_day, use_container_width=True)

# Number of negative sentiments per day
st.subheader('Number of Negative Sentiments per Day')
df_negative_per_day = df.groupby('pub_date')['numNegative'].sum()
st.bar_chart(df_negative_per_day, use_container_width=True)

# Average sentiment per day
st.subheader('Average Sentiment per Day')
df_avg_sentiment_per_day = df.groupby('pub_date')['AVGsentiment'].mean()
st.line_chart(df_avg_sentiment_per_day)

# Total Articles per day
st.subheader('Number of Articles per Day')
df_total_sentences_per_day = df.groupby('pub_date')['TotalSentences'].sum()
st.bar_chart(df_total_sentences_per_day)

# Distribution of Sentiment Scores
st.subheader('Distribution of Sentiment Scores')
plt.hist(df['AVGsentiment'], bins=20, edgecolor='black')
st.pyplot()

# # Source Distribution
# st.subheader('Source Distribution')
# source_counts = df['source'].value_counts()
# st.bar_chart(source_counts, use_container_width=True)

# # Document Type Distribution
# st.subheader('Document Type Distribution')
# doc_type_counts = df['document_type'].value_counts()
# st.bar_chart(doc_type_counts, use_container_width=True)

# # Section Name Distribution
# st.subheader('Section Name Distribution')
# section_counts = df['section_name'].value_counts()
# st.bar_chart(section_counts, use_container_width=True)

# Section Name Distribution (Top N)
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame
# If not, you should load your DataFrame first

# Convert 'pub_date' to datetime format
df['pub_date'] = pd.to_datetime(df['pub_date'])

# Format 'pub_date' to display only the date
df['pub_date'] = df['pub_date'].dt.date

# Sections to count occurrences
sections_to_count = ['U.S.', 'New York', 'Crosswords & Games', 'Climate', 'World', 'Arts', 'The Learning Network', 'Briefing', 'Business Day', 'Corrections', 'Podcasts', 'Science', 'Movies', 'Style', 'Opinion', 'Magazine', 'Books', 'Travel', 'Well', 'Technology', 'Reader Center', 'Real Estate', 'Special Series', 'Food', 'T Magazine']

# Assign colors to each section
section_colors = {
    'U.S.': 'skyblue',
    'New York': 'orange',
    'Crosswords & Games': 'green',
    'Climate': 'red',
    'World': 'purple',
    'Arts': 'brown',
    'The Learning Network': 'pink',
    'Briefing': 'cyan',
    'Business Day': 'lime',
    'Corrections': 'gray',
    'Podcasts': 'magenta',
    'Science': 'yellow',
    'Movies': 'teal',
    'Style': 'blue',
    'Opinion': 'gold',
    'Magazine': 'olive',
    'Books': 'indigo',
    'Travel': 'violet',
    'Well': 'coral',
    'Technology': 'salmon',
    'Reader Center': 'lightblue',
    'Real Estate': 'darkgreen',
    'Special Series': 'darkred',
    'Food': 'khaki',
    'T Magazine': 'plum',
    # Add more sections and colors as needed
}

# Count occurrences for each section
section_counts = {section: df['section_name'].str.contains(section).sum() for section in sections_to_count}

# Streamlit app
st.title('Section Occurrences Count')

# Display the counts
st.subheader('Occurrences Count for Each Section')
st.write(pd.DataFrame(list(section_counts.items()), columns=['Section', 'Occurrences']))

# Plot the data with different colors
st.subheader('Occurrences Count Bar Chart')
fig, ax = plt.subplots(figsize=(15, 8))

# Bar chart with different colors
for section, color in section_colors.items():
    plt.bar(section, section_counts.get(section, 0), color=color)

plt.xticks(rotation=45, ha='right')
ax.set_xlabel('Section')
ax.set_ylabel('Occurrences')

st.pyplot(fig)



# Word Cloud of Abstracts
st.subheader('Word Cloud of Abstracts')
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['abstract']))

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')

# Display the Matplotlib plot using st.pyplot()
st.pyplot(fig)

