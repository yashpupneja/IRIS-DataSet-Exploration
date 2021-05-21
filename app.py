import streamlit as st

#Component Pkgs
import streamlit.components.v1 as components 

import base64

#Pkgs - Files
import DS_EDA_App
def main():
	st.set_option('deprecation.showPyplotGlobalUse', False)
	
	# Css.local_css("style.css")
	DS_EDA_App.main()

if __name__ == '__main__':
	main()
