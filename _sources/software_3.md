# Fix missing buttons in Jupyter Notebook

In ArcGIS Pro's Jupyter Notebook, two useful buttons in the menu bar are
missing: **Files** and **Kernel**.

These two buttons give you access to several key functions, such as
**_Restart Kernel_** and **_Download Notebook as Python file_**.

A solution to fix the missing buttons is presented below. The answer is based
on this [post](https://community.esri.com/t5/arcgis-online-questions/juypter-notebook-via-arcpro-missing-menu-bar/td-p/1118984/page/3).

<div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff">
<strong>Step 1:</strong> Navigate to the following folder.
</div>

`C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\share\jupyter\kernels\ArcGISPro\default`

<div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff">
<strong>Step 2:</strong> Copy the two files below.
</div>

1. `messsages.css`
2. `messages.js`

```{image} https://live.staticflickr.com/65535/51888195506_7591dc13fe_o.png
:class: mb-3
:alt: jupyter files
:width: 620
```

<div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff">
<strong>Step 3:</strong> Paste the two files into the following folder.
</div>

`C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\Lib\site-packages\notebook\static\custom`

<div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff">
<strong>Step 4:</strong> Restart the Jupyter Notebook. (restart the _Python Command Prompt_ if necessary)
</div>