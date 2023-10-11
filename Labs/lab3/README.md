# Lab 3

The task can be found in the PDF file. Here's an initial UML chart before beginning to code:

![Initial UML Diagram](./assets/Labb3UML.drawio.png)

To install the geometry_shapes package, navigate inside the top geometry_shapes directory, then run

```pip install -e .```

This tells pip to install the Python package in the current directory. The ``-e`` flag tells pip to install the package in editable mode, which means that any changes you make to the package will be reflected in the installed package.

### Still to do
* Spheres and cubes
* Unit testing
* Docstrings
* Drawing more independent, perhaps ax subplot() etc in Common supershape class, passing on plt and ax to all children, plt.show() in .draw() ? 