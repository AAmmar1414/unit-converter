import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Enchanced Unit Converter",layout="wide")

#custom class
st.markdown("""
    <style>
    .main {
        background-color: #000000; /* Black background */
    }
    .stButton>button {
        background-color: #FF5733; /* Vibrant orange */
        color: #FFFFFF; /* White text */
        border-radius: 10px;
        padding: 10px 20px;
        border: 2px solid #FFC300; /* Yellow border */
    }
    .stSelectbox {
        border-radius: 10px;
        background-color: #333333; /* Dark grey background */
        color: #FFFFFF; /* White text */
    }
    .success-message {
        padding: 20px;
        border-radius: 10px;
        background-color: #1D8348; /* Dark green */
        border: 1px solid #28B463; /* Bright green border */
        color: #D5F5E3; /* Soft green text */
    }
    </style>
    """, unsafe_allow_html=True)

def lenghtconverter(value,from_unit,to_unit):
    length_units={
         'meters': 1,
    'kilometers': 0.001,
    'centimeters': 100,
    'millimeters': 1000,
    'miles': 0.000621371,
    'yards': 1.09361,
    'feet': 3.28084,
    'inches': 39.3701,
    'nanometers': 1e9,  # Added new units
    'micrometers': 1e6,
    'light years': 1.057e-16
    }
    value_in_meters =value/length_units[from_unit]
    return value_in_meters * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1,
        'grams': 1000,
        'milligrams': 1000000,
        'pounds': 2.20462,
        'ounces': 35.274,
        'metric tons': 0.001,  # Added new units
        'stone': 0.157473,
        'grains': 15432.4
    }
    value_in_kg = value / weight_units[from_unit]
    return value_in_kg * weight_units[to_unit]


def temp_converter(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value


def get_chatbot_response(query):
    # Simple chatbot responses
    responses = {
        "hello": "Hi! How can I help you with unit conversion today?",
        "help": "I can help you convert between different units of length, weight, and temperature. Just select the conversion type and units!",
        "thank": "You're welcome! Let me know if you need any other help.",
        "bye": "Goodbye! Come back anytime for more conversions!",
    }
    
    query = query.lower()
    for key in responses:
        if key in query:
            return responses[key]
    return "I'm here to help with unit conversions. Try asking about length, weight, or temperature conversions!"


def main():
    st.markdown("""
    <div style='background: linear-gradient(45deg, #000000, #333333); padding: 20px; border-radius: 15px;'>
        <h1 style='color: #FF5733; text-align: center;'>✨ Enhanced Unit Converter ✨</h1>
    </div>
""", unsafe_allow_html=True)

# Sidebar with gradient background
with st.sidebar:
    st.markdown("""
        <div style='background: linear-gradient(45deg, #1D8348, #28B463); padding: 10px; border-radius: 10px;'>
            <h2 style='color: #D5F5E3; text-align: center;'>Settings</h2>
        </div>
    """, unsafe_allow_html=True)
    
    conversion_type = st.selectbox(
        "Choose conversion type",
        ["Length", "Weight", "Temperature"]
    )

# Main conversion interface
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style='background: #000000; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
            <h3 style='color: #FF5733;'>Convert Units</h3>
        </div>
    """, unsafe_allow_html=True)


value = st.number_input("Enter value to convert", value=0.0)

if conversion_type == "Length":
            units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches", 
                    "nanometers", "micrometers", "light years"]
            from_unit = st.selectbox("From", units)
            to_unit = st.selectbox("To", units)
            
            if st.button("Convert!", key="length"):
                result = lenghtconverter(value, from_unit, to_unit)
                st.balloons()  # Celebration effect
                st.markdown(f"""
                    <div class='success-message'>
                        <h3>🎉 Result:</h3>
                        <p>{value} {from_unit} = {result:.4f} {to_unit}</p>
                    </div>
                """, unsafe_allow_html=True)


elif conversion_type == "Weight":
            units = ["kilograms", "grams", "milligrams", "pounds", "ounces", "metric tons", "stone", "grains"]
            from_unit = st.selectbox("From", units)
            to_unit = st.selectbox("To", units)
            
            if st.button("Convert!", key="weight"):
                result = weight_converter(value, from_unit, to_unit)
                st.balloons()  # Celebration effect
                st.markdown(f"""
                    <div class='success-message'>
                        <h3>🎉 Result:</h3>
                        <p>{value} {from_unit} = {result:.4f} {to_unit}</p>
                    </div>
                """, unsafe_allow_html=True)
                
elif conversion_type == "Temperature":
            units = ["celsius", "fahrenheit", "kelvin"]
            from_unit = st.selectbox("From", units)
            to_unit = st.selectbox("To", units)
            
            if st.button("Convert!", key="temp"):
                result = temp_converter(value, from_unit, to_unit)
                st.balloons()  # Celebration effect
                st.markdown(f"""
                    <div class='success-message'>
                        <h3>🎉 Result:</h3>
                        <p>{value} {from_unit} = {result:.4f} {to_unit}</p>
                    </div>
                """, unsafe_allow_html=True)

                # AI Chatbot interface
with col2:
    st.markdown("""
        <div style='background: #000000; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
            <h3 style='color: #FF5733;'>AI Conversion Assistant 🤖</h3>
        </div>
    """, unsafe_allow_html=True)
    
    user_input = st.text_input("Ask me anything about unit conversion!", key="chat_input")
    if user_input:
        response = get_chatbot_response(user_input)
        st.markdown(f"""
            <div style='background: #333333; color: #FFFFFF; padding: 15px; border-radius: 10px; margin-top: 10px;'>
                <p><strong>🤖 Assistant:</strong> {response}</p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 30px; padding: 20px; background: #000000; border-radius: 10px; color: #FFFFFF;'>
        <p>Made with ❤️ | Current time: {}</p>
    </div>
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)
