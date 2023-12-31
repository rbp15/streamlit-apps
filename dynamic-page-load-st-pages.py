# https://app-apps-niujdksqmrtkz6vy99twww.streamlit.app/

import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

"## Declaring the pages in your app:"

show_pages(
    [
        Page("example_app/streamlit_app_sections.py", "Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("example_app/example_one.py", "Example One", ":books:"),
        # Since this is a Section, all the pages underneath it will be indented
        # The section itself will look like a normal page, but it won't be clickable
        Section(name="Cool apps", icon=":pig:"),
        # The pages appear in the order you pass them
        Page("example_app/example_four.py", "Example Four", "📖"),
        Page("example_app/example_two.py", "Example Two", "✏️"),
        Section(name="Other apps", icon=":horse:"),
        # Will use the default icon and name based on the filename if you don't
        # pass them
        Page("example_app/example_three.py"),
        # You can also pass in_section=False to a page to make it un-indented
        Page("example_app/example_five.py", "Example Five", "🧰", in_section=False),
    ]
)

add_page_title()  # Optional method to add title and icon to current page
