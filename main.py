import datetime
import io
import os
import random
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass
from pprint import pprint
from typing import Final
import joblib
import concurrent.futures

import cachetools
import pandas as pd
import streamlit as st
from colorama import Fore
from dotenv import load_dotenv
 
load_dotenv()

with open('static/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def load_model(model_file):
    return joblib.load(model_file)
col1,col2,col3 = st.columns([1,2,1])
col2.image("static/logo.png", width=300)


# st.image("static/stand.png")
st.title("AI Infrastructure for Model training")

model_name = st.text_input("Enter a model name: ", value=f"model-{uuid.uuid1()}")

python_code: str


# with open('examples/linear-regression.py', 'r') as f1:
#     python_code = f1.read()


python_code = st.file_uploader("Upload Python Code", type=["py"])
pretrained_model = st.file_uploader("Upload Pretrained Model", type=["sav"])
dataset = st.file_uploader("Upload Dataset", type=["csv"])
requirements_txt = st.file_uploader("Upload requirements.txt", type=["txt"])

# dataset: str = dataset or 'examples/canada_per_capita_income.csv'


if st.button('Train'):

    if requirements_txt:
        requirements = requirements_txt.getvalue().decode().split('\n')


        def install(package):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        # Use a ThreadPoolExecutor to install the packages in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(install, requirements)

        # for package in requirements:
        #     subprocess.check_call([sys.executable, "-m", "pip", "install", package])


    loaded_model = None

    if pretrained_model:
        loaded_model = load_model(pretrained_model)
        st.write("Loaded pretrained model.")
    # Load dataset
    if not dataset:
        st.write("Please upload a dataset.")

    if python_code and dataset:
        train_model = lambda dataset, pretrained_model: {}
        exec(python_code.getvalue())
        # exec(python_code)
        start_time = time.time()
        model = train_model(dataset, loaded_model)
        end_time = time.time()

        elapsed_time = end_time-start_time

        print(f"{Fore.GREEN} Elapsed time: {elapsed_time:.6f} seconds")

        fName = f"trained-{model_name}-{str(datetime.datetime.now())} {elapsed_time:.6f}s.sav"

        model_bytes = io.BytesIO()
        joblib.dump(model, model_bytes)
        model_bytes.seek(0)

        st.write("Trained a new model")

        st.download_button(
            label="Download trained model",
            data=model_bytes,
            file_name=fName,
        )
    else:
        st.write("Please upload Python code to train the model.")

