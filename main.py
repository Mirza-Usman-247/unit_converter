import streamlit as st


# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversions = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
    }
    lenghth = value * conversions[from_unit]
    return lenghth / conversions[to_unit]


def convert_weight(value, from_unit, to_unit):
    conversions = {"mg": 0.001, "g": 1.0, "kg": 1000.0, "lb": 453.592, "ton": 907185}
    grams = value * conversions[from_unit]
    return grams / conversions[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == "°F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        celsius = value

    # Convert from Celsius to target unit
    if to_unit == "°F":
        return celsius * 9 / 5 + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        return celsius


def main():
    st.title("📏 Universal Unit Converter")

    category = st.selectbox(
        "Select conversion category",
        ["Length", "Weight", "Temperature"],
    )

    if category == "Length":
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter value", min_value=0.0, value=1.0)
            from_unit = st.selectbox(
                "From unit", ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"]
            )
        with col2:
            to_unit = st.selectbox(
                "To unit", ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"]
            )
            result = convert_length(value, from_unit, to_unit)

    elif category == "Weight":
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter value", min_value=0.0, value=1.0)
            from_unit = st.selectbox("From unit", ["mg", "g", "kg", "lb", "ton"])
        with col2:
            to_unit = st.selectbox("To unit", ["mg", "g", "kg", "lb", "ton"])
            result = convert_weight(value, from_unit, to_unit)

    elif category == "Temperature":
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter temperature", value=0.0)
            from_unit = st.selectbox("From unit", ["°C", "°F", "K"])
        with col2:
            to_unit = st.selectbox("To unit", ["°C", "°F", "K"])
            result = convert_temperature(value, from_unit, to_unit)

    # Display result
    st.metric("Converted Value", f"{value} {to_unit}")


if __name__ == "__main__":
    main()
