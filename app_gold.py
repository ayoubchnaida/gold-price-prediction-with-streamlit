import pickle
import streamlit as st
import pandas as pd
import RandomForestRegressor
# Load the Model
model = pickle.load(open('Gold.sav', 'rb'))

# Streamlit Page
st.title('GOLD Price Prediction')

# Collect User Input in the Sidebar
st.sidebar.header('Feature Selection')
SPX = st.sidebar.number_input('SPX')
USO = st.sidebar.number_input('USO')
SLV = st.sidebar.number_input('SLV')
EUR_USD = st.sidebar.number_input('EUR/USD')


# Prepare Features for Prediction
data = {'SPX': [SPX], 'USO': [USO], 'SLV': [SLV], 'EUR_USD': [EUR_USD]}
df = pd.DataFrame(data)

# Show User Input Features DataFrame under an Info Message
st.info('User Input Features:')
st.write(df)
st.title('price predicted  is :')
# Make Predictions
if st.sidebar.button('Predict'):
    prediction = model.predict(df)
    st.success(f'Predicted GOLD Price: ${prediction[0]:.2f}')
