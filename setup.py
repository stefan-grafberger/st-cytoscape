import setuptools

setuptools.setup(
    name="st-cytoscape",
    version="0.0.5",
    author="",
    author_email="",
    description="A Streamlit component to display a Cytoscape.js graph",
    long_description="A Streamlit component to display a Cytoscape.js graph with the selected nodes and edges in return",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
