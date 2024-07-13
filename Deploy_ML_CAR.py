import streamlit as st
import joblib
# load the model
model = joblib.load('car-price-predictor')

st.title('Car-price-predictor')
symboling = st.number_input(
    'Enter symboling', min_value=-2, max_value=3, value=0)
doornumber = st.number_input(
    'Enter Door number 2/4', min_value=2, max_value=4, value=2)
wheelbase = st.number_input(
    'Enter wheel base', min_value=85, max_value=130, value=100)
carlength = st.number_input(
    'Enter car length', min_value=140, max_value=210, value=180)
carwidth = st.number_input(
    'Enter car width', min_value=60, max_value=73, value=65)
carheight = st.number_input(
    'Enter car height', min_value=45, max_value=60, value=50)
curbweight = st.number_input(
    'Enter curb weight', min_value=1000, max_value=4500, value=3000)
cylindernumber = st.number_input(
    'Enter cylinder number', min_value=2, max_value=12, value=5)
enginesize = st.number_input(
    'Enter engine size', min_value=60, max_value=330, value=200)
boreratio = st.number_input(
    'Enter bore ratio', min_value=2, max_value=4, value=3)
stroke = st.number_input('Enter no. of stroke',
                         min_value=2, max_value=5, value=3)
compressionratio = st.number_input(
    'Enter compression ratio', min_value=5, max_value=25, value=15)
horsepower = st.number_input(
    'Enter horse power', min_value=40, max_value=300, value=150)
peakrpm = st.number_input(
    'Enter peak rpm', min_value=4000, max_value=7000, value=5500)
citympg = st.number_input(
    'Enter city mpg', min_value=10, max_value=55, value=35)
highwaympg = st.number_input(
    'Enter highway mpg', min_value=15, max_value=60, value=40)

enginesize = st.number_input(
    'Enter engine size', min_value=130, max_value=175, value=150)
horsepower = st.number_input(
    'enter horse power', min_value=100, max_value=150, value=125)
car_company = st.selectbox('Select Car Company', ['toyota', 'nissan', 'mazda', 'mitsubishi', 'honda', 'volkswagen', 'subaru', 'peugeot', 'volvo',
                           'dodge', 'buick', 'bmw', 'audi', 'plymouth', 'saab', 'porsche', 'isuzu', 'jaguar', 'chevrolet', 'alfa-romero', 'renault', 'mercury'])

fueltype = st.selectbox('Select Fuel type', ['diesel', 'gas'])
aspiration = st.selectbox('Select Aspiration', ['std', 'turbo'])
carbody = st.selectbox(
    'Select Carbody', ['sedan', 'hatchback', 'wagon', 'hardtop', 'convertible'])
drivewheel = st.selectbox('Select Drive wheel', ['fwd', 'rwd', '4wd'])
enginelocation = st.selectbox('Select engine location', ['front', 'rear'])
enginetype = st.selectbox('Select engine type', [
                          'ohc', 'ohcf', 'dohc', 'l', 'rotor', 'dohcv'])
fuelsystem = st.selectbox('Select fuel system', [
                          'mpfi', '2bbl', 'idi', '1bbl', 'spdi', '4bbl', 'mfi', 'spfi'])
if car_company == 'toyota':
    car_company_encode = 19
elif car_company == 'nissan':
    car_company_encode = 12
elif car_company == 'mazda':
    car_company_encode = 9
elif car_company == 'mitsubishi':
    car_company_encode = 11
elif car_company == 'honda':
    car_company_encode = 6
elif car_company == 'volkswagen':
    car_company_encode = 20
elif car_company == 'subaru':
    car_company_encode = 18
elif car_company == 'peugeot':
    car_company_encode = 13
elif car_company == 'volvo':
    car_company_encode = 21
elif car_company == 'dodge':
    car_company_encode = 5
elif car_company == 'buick':
    car_company_encode = 3
elif car_company == 'bmw':
    car_company_encode = 2
elif car_company == 'audi':
    car_company_encode = 1
elif car_company == 'plymouth':
    car_company_encode = 14
elif car_company == 'saab':
    car_company_encode = 17
elif car_company == 'porsche':
    car_company_encode = 15
elif car_company == 'isuzu':
    car_company_encode = 7
elif car_company == 'jaguar':
    car_company_encode = 8
elif car_company == 'chevrolet':
    car_company_encode = 4
elif car_company == 'alfa-romero':
    car_company_encode = 0
elif car_company == 'renault':
    car_company_encode = 16
else:
    car_company_encode = 10

if fueltype == 'diesel':
    fueltype_encode = 0
else:
    fueltype_encode = 1

if aspiration == 'turbo':
    aspiration_encode = 1
else:
    aspiration_encode = 0

if carbody == 'convertible':
    carbody_encode = 0
elif carbody == 'hardtop':
    carbody_encode = 1
elif carbody == 'hatchback':
    carbody_encode = 2
elif carbody == 'sedan':
    carbody_encode = 3
else:
    carbody_encode = 4

if drivewheel == '4wd':
    drivewheel_encode = 0
elif drivewheel == 'fwd':
    drivewheel_encode = 1
else:
    gender_encode = 2

if enginelocation == 'front':
    enginelocation_encode = 0
else:
    gender_encode = 1

if enginetype == 'dohc':
    enginetype_encode = 0
elif enginetype == 'dohcv':
    enginetype_encode = 1
elif enginetype == 'l':
    enginetype_encode = 2
elif enginetype == 'ohc':
    enginetype_encode = 3
elif enginetype == 'ohcf':
    enginetype_encode = 4
elif enginetype == 'ohcv':
    enginetype_encode = 5
else:
    gender_encode = 6

if fuelsystem == '1bbl':
    fuelsystem_encode = 0
elif fuelsystem == '2bbl':
    fuelsystem_encode = 1
elif fuelsystem == '4bbl':
    fuelsystem_encode = 2
elif fuelsystem == 'idi':
    fuelsystem_encode = 3
elif fuelsystem == 'mfi':
    fuelsystem_encode = 4
elif fuelsystem == 'mpfi':
    fuelsystem_encode = 5
elif fuelsystem == 'spdi':
    fuelsystem_encode = 6
else:
    fuelsystem_encode = 7

if st.button("Predict price"):
    input = [[car_company_encode, symboling, fueltype_encode, aspiration_encode, doornumber, carbody_encode, drivewheel_encode, enginelocation_encode, wheelbase, carlength, carwidth,
              carheight, curbweight, enginetype_encode, cylindernumber, enginesize, fuelsystem_encode, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg]]
    result = model.predict(input)[0]
    st.write('The predicted price in dollors is', result)
