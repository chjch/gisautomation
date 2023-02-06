# Basics of Jupyter Notebook

## What is Jupyter Notebook

1. An Integrated Development Environment (**IDE**) embedded in web browser.
2. Experiment with your codes dynamically (run your codes CELL BY CELL).
3. A light-weight application runs inside ArcGIS Pro or a **_web browser_**.
4. Powerful in sharing, visualizing, and presenting ideas and results of analysis.

```{image} _static/images/new_py_nb.png
:class: shadow mb-1 border
:alt: new_py_nb
```

## How to create a new Python Notebook

- **Analysis** (_tab_) -> **Geoprocessing** (_group_) -> **Python Notebook**.

  ```{image} _static/images/py_nb_menubar.png
  :class: shadow mb-2 border
  :alt: py_nb_menubar
  :scale: 50%
  ```

- **Save** the notebook.

  ```{image} _static/images/save_py_nb.png
  :class: shadow mb-2 border
  :alt: save_py_nb
  :scale: 50%
  ```

- **Rename** the notebook (`.ipynb`) in the **Catalog Pane**.

## How to run codes in a cell

1. `Ctrl+Enter`: run a cell and stay focus on the current cell.
2. `Shift+Enter`: run a cell and move selection to the next cell.
3. `Alt+Enter`: run a cell and insert a new cell below the current cell.

## Two types of cell

- **Code** cell: contains _Python_ codes ready to run, indicated by `In [ ]`.

  ```{image} _static/images/code_cell.png
  :class: shadow mb-2 border
  :alt: code_cell
  ```

- **Markdown** cell: contains _Markdown_ codes, without `In [ ]`.

  ```{image} _static/images/md_cell_before.png
  :class: shadow mb-2 border
  :alt: md_cell_before
  ```

  ```{image} _static/images/md_cell_after.png
  :class: shadow mb-2 border
  :alt: md_cell_after
  ```

```{tip}

Follow the same way mentioned above to **run** both _Markdown_ cell and _Code_ cell.
```

## Two cell modes

Cells in Jupyter Notebook can be in either one of two modes:

- **Command** mode: indicated by a <b><span style="color:dodgerblue">*blue*</span></b> vertical bar; press `Esc` key to enable.
- **Edit** mode: indicated by a <b><span style="color:forestgreen">*green*</span></b> vertical bar; press `Enter` to enable or simply click the cell.

## Useful shortcuts (only when in command mode)

1. `A`/`B`: Create a new cell above/below the current cell.
2. `UP`/`DOWN`: Arrow key to navigate between cells.
3. `M`: Convert a cell from code mode to markdown code.
4. `Y`: Convert a cell from markdown mode to code mode.
5. `D,D`: Delete a cell.
6. `L`: Toggle line number.
7. `F`: Find and replace text in markdown.
8. `H`: Show all keyboard shortcuts.

```{tip}

**Multi-cursor support** in Jupyter Notebook

- `Ctrl` + mouse click
- `Alt` + mouse click
- [Helpful tricks in Jupyter Notebook](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

```

**<center>[Top 20](https://en.wikipedia.org/wiki/List_of_largest_cities) largest city in the world</center>**

| Name           | Country        | Continent     | UN Estimation (2018) | Urban Area |
|----------------|----------------|---------------|----------------------|------------|
| Tokyo          |  Japan         | Asia          | 37,400,068           | 4,751      |
| Delhi          |  India         | Asia          | 28,514,000           | 14,272     |
| Shanghai       |  China         | Asia          | 25,582,000           | 5,436      |
| Sao Paulo      |  Brazil        | South America | 21,650,000           | 6,949      |
| Mexico City    |  Mexico        | South America | 21,581,000           | 9,017      |
| Cairo          |  Egypt         | Africa        | 20,076,000           | 9,844      |
| Mumbai         |  India         | Asia          | 19,980,000           | 22,010     |
| Beijing        |  China         | Asia          | 19,618,000           | 4,659      |
| Dhaka          |  Bangladesh    | Asia          | 19,578,000           | 36,928     |
| Osaka          |  Japan         | Asia          | 19,281,000           | 5,129      |
| New York       |  United States | North America | 18,819,000           | 684        |
| Karachi        |  Pakistan      | Asia          | 15,400,000           | 14,648     |
| Buenos Aires   |  Argentina     | South America | 14,967,000           | 5,033      |
| Chongqing      |  China         | Asia          | 14,838,000           | 5,378      |
| Istanbul       |  Turkey        | Europe        | 14,751,000           | 11,135     |
| Kolkata        |  India         | Asia          | 14,681,000           | 13,830     |
| Manila         |  Philippines   | Asia          | 13,482,000           | 12,798     |
| Lagos          |  Nigeria       | Africa        | 13,463,000           | 7,877      |
| Rio de Janeiro |  Brazil        | South America | 13,293,000           | 6,181      |
| Tianjin        |  China         | Asia          | 13,215,000           | 3,886      |