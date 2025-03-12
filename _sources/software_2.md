# Use Notebook in a Browser

So far, we have been using **Python** (Jupyter) **Notebook** from ArcGIS Pro.
The benefit of this approach is that it integrates well with the GIS software.

However, this approach currently has a big limitation is that you **cannot
force** shutdown or terminate the Kernel of Jupyter Notebook without **closing
and reopening** ArcGIS Pro altogether.

In a situation like an "_endless loop_", intentional or not, terminating a
running Jupyter kernel is definitely of great usage.

Fortunately, we can open the Jupyter Notebook from your web browser.

**Step 1**: Open **_Python Command Prompt_**.

```{image} _static/images/python_cmd.png
:class: mb-2
:alt: python_cmd
:align: center
:scale: 40%
```

**Step 2**: Run Jupyter Notebook command.

Type the `jupyter notebook` in the command line. Note there is a space in
between the two words. Then, follow by the specific path from which you want to
start Jupyter. For example, you may want to open it from a path where you have
an existing notebook that you want to edit or work with.

```{image} _static/images/run_jupyter.png
:class: mb-2
:alt: run_jupyter
:align: center
```

```{note}
Separate the command `jupyter notebook` and the path **by a space**.
Use double quotes, e.g., `"to/my/path"`, to enclose the path (from where you
want to open Jupyter Notebook) in case there are **spaces in the path** name.
```

**Step 3**: Use Jupyter Notebook

```{image} _static/images/jupyter_browser.png
:class: mb-2
:alt: jupyter_browser
:align: center
```