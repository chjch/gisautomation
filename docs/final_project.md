# Final Project

**PROJECT OBJECTIVE**: Use Python to create an ArcGIS Pro _Script Tool_ that
assists planners in the area of land use and transportation coordination
focused on improving traffic safety.

**NEEDS/SPECIFICATIONS**: Alachua County Planning Department and Metropolitan
Planning Organization (MPO) are coordinating their efforts to develop
transportation and built environment interventions intended to **reduce traffic
crashes** in the county's roadways. Due to limited budget, they must be
strategic on how they target the intervention areas and prioritize their
resources. They require some assistance to identify priority areas that are
expected to provide most improvements for their effort.

## Script Tool Description

You are asked to create a script tool, namely Traffic Safety Analysis (TSA)
in ArcGIS Pro that can identify **census block groups** based on 3 criteria.

### 1. Block groups with high crash rate

_Crash rate_ can be calculated as **number of crashes per liner roadway mile**.
Only consider crashes that are **within 300 feet of major roads**. This rate
should be calculated for every block group. Only block groups within the
Alachua county should be considered. The block groups are classified into
**3 classes** by crash rate. The classification is performed as following:
- **Low**: crash rate between `min` and `(mean + min)/2`
- **Medium**: crash rate between `(mean + min)/2` and `(max + mean)/2`
- **High**: crash rate greater than `(max + mean)/2`

```{note}
Use NumPy to obtain `min`, `max`, and `mean` of the crash rate.
```

All intervals are **right-inclusive**.

```{image} https://live.staticflickr.com/65535/51917422725_c153074a44_o.jpg
:class: mb-3
:alt: high crash blkgrp
:width: 600
```

### 2. Areas with suitable land uses and proximity

This part of the analysis should be raster-based using the concept of raster
overlays also generally referred to as suitability modeling.
- For the purpose of this exercise, suitable areas are considered those that
  are in **proximity to schools**, in **proximity to residential** land use,
  in **proximity to commercial** land use (from the **landuse** feature class
  in `class_data.gdb`), and **distant from the hospitals**.
  Based on these requirements, create suitability raster grids for each of
  these proximity layers and categorize them in 9 classes (1 to 9) by using
  “**natural breaks**” classification. The extent and mask for all raster
  geoprocessing are the county boundary and the **cell size** is **30** (meters).
- Then, create the Final Suitability Raster by considering all four individual
  proximity suitability and apply the following weights: **30%** for proximity
  to schools, **30%** for proximity to residential, **30%** for proximity to
  commercial, and **10%** for the hospital suitability.
- Next, convert the output from floating point raster into an integer raster.

The outcome of this step will produce the **MOST SUITABLE AREAS**. These will
be areas that have the value of **_9_** in the Final Suitability Raster. These
areas should be converted to vector (polygons). These areas are considered to
have higher potential for successful investment to reduce the traffic crashes
when concerning the proximity factors.

```{image} https://live.staticflickr.com/65535/51916899953_a164d8cfd9_o.jpg
:class: mb-3
:alt: suitable areas
:width: 600
```

### 3. Final selection 

These are those **HIGH CRASH RATE BLOCK GROUPS** in which the **MOST SUITABLE
AREAS** occupy **more than 50%** of the block group area.

```{image} https://live.staticflickr.com/65535/51917130374_54030f63b9_o.jpg
:class: mb-3
:alt: final output
:width: 784
```

## Part I: Develop the model with ModelBuilder

**DELIVERABLE**: Submit the model and the resulting feature class produced by
your model.

**DUE**: see schedule

## PART II - Python scripting (hard code)

**DELIVERABLE**: The complete python script in Jupyter Notebook. Make sure that
your script is well commented.

**DUE**: see schedule

## PART III - Develop a script tool

The tool should include a front-end graphical user interface (GUI) that will
allow the user to select the input data and adjust the input parameters.

The required **parameters** of the script tool are:

- input gdb (workspace),
- input feature classes - block groups, major roads, crashes, hospitals,
  schools, and land uses,
- ability to select the `landuse` (commercial and residential),
- name of the output feature class,
- output path (if it differs from the input gdb),
- an overwrite output checkbox,
- analysis extent and analysis mask,
- cell size,
- weights for each suitability raster.

You may also include other parameters of your choice (not mandatory) such as
buffer distance from road, slice reclassification type, etc.

Additionally, the tool should be documented with a Help page to make the use of
it self-explanatory, like any other ArcGIS tool. As a reminder, this can be
done by going to right-click on the tool -> metadata -> Edit.

Below is shown an illustration of the tool interface:

```{image} https://live.staticflickr.com/65535/51916887948_c13d34a7cb_o.png
:class: mb-3
:alt: tool interface
:width: 448
```

The tool should be packaged in order to be shared with the County and the MPO.
The package should be in ArcGIS Pro folder including the Toolbox with the tool
in it, the python script file, the input geodatabase and the ArcGIS Pro project
file (the .aprx) that shows the input data. Include a readme.txt file that
explains to the user how to open and run the tool.

**DELIVERABLE**: presentation (see guideline below) and packaged tool files.

**DUE**: See schedule

### Presentation Guideline

- **Length**: maximum **7** minutes.
- **Presentation Focus**: The purpose of the presentation is to share your
  experience with your peers, and not necessarily present your work to the
  instructors. Given the problem is the same for everyone, there is no need to
  go in detail for every single step. More or less, the method used by most
  students are very similar. Therefore, the focus on the presentation should be
  to show the tool in operation, to share the parts of the project that were
  more challenging and how you solved them, and to reflect on the learning
  experience.
- **Presentation Content** (5-7 slides max)
    + Title Slide
    + Select two challenging parts of the project that you struggled or that
      show some interesting solution that we either did not cover in class or
      that was not required, but you think adds value to this project. Explain
      them and share with the class your solution. Use 1 to 2 slides for each.
      E.g. one slide shows the problem and the other shows the solution.
    + Final remarks slides (1 or 2 slides): Bullet list of main lessons learned
      in this project – be specific. Share with the instructor what worked
      well, what didn’t, and what would you do differently next time.
- **Presentation Media**: It could be a combination of slides, source code,
  ArcGIS Pro file etc. Select whatever would be most effective within the
  limits of available time.

## PART IV

**ASSIGNMENT**: Write an **executive summary document** about this tool. The
document should include the objectives, method, data used, results, discussion,
and conclusions. The summary should be **minimum 1,000 words** without counting
any pictures or figures.

**DELIVERABLE**: Three folders with respective files (see below) packaged as a
zip folder.

```{image} https://live.staticflickr.com/65535/51915845047_f7f47afcec_o.png
:class: mb-3
:alt: deliverable1
:width: 380
```
```{image} https://live.staticflickr.com/65535/51917139679_a7a8bc85fc_o.png
:class: mb-3
:alt: deliverable2
:width: 380
```
```{image} https://live.staticflickr.com/65535/51916813011_ca3bcea41f_o.png
:class: mb-3
:alt: deliverable3
:width: 380
```

**DUE**: see syllabus.