import streamlit as st
from send_email import send_email

message = f"""
Subject: Message sent from {user_email}


From: {user_email}
Topic: {topic}
{raw_message}
"""

